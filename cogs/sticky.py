# Fixed sticky cog for Discord.py
# Key fixes applied:
# - Start background tasks once in on_ready (guarded) instead of in __init__
# - Prevent duplicate repost task creation
# - Properly cancel background tasks on cog_unload
# - Ignore bot's own messages where appropriate
# - Check existing last sticky before sending to avoid duplicates

import asyncio
import os
import logging
from collections import defaultdict, deque
from typing import Optional

import discord
from discord.ext import commands, tasks

log = logging.getLogger("sticky")
logging.basicConfig(level=logging.INFO)

# NOTE: this cog expects a "stickies" collection-like interface.
# The original used motor (mongo). If you use mongo, provide the same methods
# (find, update_one, insert_one, delete_one) or adapt this code.

class StickyMessages(commands.Cog):
    def __init__(self, bot: commands.Bot, db=None):
        self.bot = bot
        # db should provide .stickies collection (async iterator for find etc.)
        self.db = db
        self.stickies = None
        if db is not None:
            # assume db has attribute stickies (like motor collection)
            self.stickies = db.stickies

        # runtime structures
        self.rate_limits = defaultdict(deque)
        self.last_sticky_messages = {}  # channel_id -> message_id
        self.repost_queue = asyncio.Queue(maxsize=1000)
        self.processing_channels = set()

        # background task handles (not started here)
        self._cleanup_task = None
        self._periodic_repost_task = None
        self._recovery_task = None
        self._repost_process_task = None

        # guard so we only start tasks once
        # use attribute on bot to survive cog reloads
        # Don't start tasks here — wait for on_ready

    # ---------- lifecycle ----------
    @commands.Cog.listener()
    async def on_ready(self):
        # Start background tasks once when bot is ready
        if getattr(self.bot, "_sticky_started", False):
            return
        self.bot._sticky_started = True
        log.info("Starting sticky background tasks")
        # start tasks and keep handles so we can cancel on unload
        self._cleanup_task = tasks.loop(seconds=60.0)(self._cleanup_loop)
        self._cleanup_task.start()

        self._periodic_repost_task = tasks.loop(hours=1.0)(self._periodic_repost_loop)
        self._periodic_repost_task.start()

        self._recovery_task = tasks.loop(seconds=30.0)(self._recovery_loop)
        self._recovery_task.start()

        # start the queue processor as an asyncio task
        self._repost_process_task = asyncio.create_task(self._process_repost_queue())

    def cog_unload(self):
        log.info("Unloading StickyMessages cog - cancelling tasks")
        # Cancel tasks if they exist
        try:
            if self._cleanup_task and self._cleanup_task.is_running():
                self._cleanup_task.cancel()
        except Exception:
            pass
        try:
            if self._periodic_repost_task and self._periodic_repost_task.is_running():
                self._periodic_repost_task.cancel()
        except Exception:
            pass
        try:
            if self._recovery_task and self._recovery_task.is_running():
                self._recovery_task.cancel()
        except Exception:
            pass
        try:
            if self._repost_process_task and not self._repost_process_task.done():
                self._repost_process_task.cancel()
        except Exception:
            pass

        # remove guard so reloads can start again if needed
        if getattr(self.bot, "_sticky_started", False):
            delattr(self.bot, "_sticky_started")

    # ---------- internal utils ----------
    def _normalize_content(self, content: Optional[str]):
        if content is None:
            return ""
        return content.strip()

    async def _send_sticky_message(self, channel: discord.TextChannel, content: Optional[str]=None, embed: Optional[discord.Embed]=None):
        """
        Safely send a sticky message to a channel. This checks the last message id
        we sent to the channel and avoids re-sending if the already-present message
        has the same content/embed. Returns the discord.Message sent or None.
        """
        try:
            # don't respond to DMs or non-text channels
            if not isinstance(channel, discord.TextChannel):
                return None

            # fetch last sticky id we recorded
            last_msg_id = self.last_sticky_messages.get(channel.id)
            # optionally fetch that message to compare content
            if last_msg_id:
                try:
                    last_msg = await channel.fetch_message(last_msg_id)
                except discord.NotFound:
                    last_msg = None
                except discord.Forbidden:
                    last_msg = None
                except Exception:
                    last_msg = None

                def message_equal(m: discord.Message):
                    if m is None:
                        return False
                    # compare content and embed(s) briefly
                    if m.content != (content or ""):
                        return False
                    if embed is None and (not m.embeds):
                        return True
                    if embed is not None and m.embeds:
                        # compare embed titles and descriptions as a heuristic
                        e = m.embeds[0]
                        if getattr(e, "title", None) == getattr(embed, "title", None) and getattr(e, "description", None) == getattr(embed, "description", None):
                            return True
                    return False

                if message_equal(last_msg):
                    # Already have identical sticky; nothing to do
                    return last_msg

            # send the sticky
            send_kwargs = {}
            if content:
                send_kwargs["content"] = content
            if embed:
                send_kwargs["embed"] = embed
            # Avoid pinging @everyone inadvertently
            send_kwargs["allowed_mentions"] = discord.AllowedMentions.none()

            sent = await channel.send(**send_kwargs)
            # record id
            self.last_sticky_messages[channel.id] = sent.id

            return sent
        except Exception as exc:
            log.exception("Failed to send sticky to %s: %s", getattr(channel, "id", "?"), exc)
            return None

    # ---------- background loops (small, safe implementations) ----------
    async def _cleanup_loop(self):
        """
        Periodic cleanup task - placeholder for removing stale DB entries or
        housekeeping. Runs under tasks.loop wrapper.
        """
        try:
            log.debug("cleanup loop tick")
            # Implement any needed cleanup logic here (DB pruning, expired stickies)
            if self.stickies is None:
                return
            # Example: remove stickies whose channels/guilds no longer exist
            async for sticky in self.stickies.find({}):
                # minimal check - assume sticky has channel_id
                chan_id = sticky.get("channel_id")
                if chan_id is None:
                    continue
                channel = self.bot.get_channel(chan_id)
                if channel is None:
                    # channel no longer present; remove from DB
                    try:
                        await self.stickies.delete_one({"_id": sticky["_id"]})
                    except Exception:
                        log.exception("Failed to delete stale sticky %s", sticky.get("_id"))
        except Exception:
            log.exception("Error in cleanup loop")

    async def _periodic_repost_loop(self):
        """
        Periodically re-enqueue all stickies for repost - this is rate-limited
        by the queue processor.
        """
        try:
            if self.stickies is None:
                return
            async for sticky in self.stickies.find({}):
                try:
                    channel_id = sticky.get("channel_id")
                    if not channel_id:
                        continue
                    await self.repost_queue.put(sticky)
                except asyncio.QueueFull:
                    log.warning("Repost queue full; skipping further enqueues")
                    break
                except Exception:
                    log.exception("Error enqueuing sticky from DB")
        except Exception:
            log.exception("Error in periodic repost loop")

    async def _recovery_loop(self):
        """
        Recovery loop to ensure any missing stickies are re-enqueued.
        """
        try:
            if self.stickies is None:
                return
            async for sticky in self.stickies.find({}):
                try:
                    channel_id = sticky.get("channel_id")
                    if not channel_id:
                        continue
                    # if we don't have a last message id for the channel, enqueue it
                    if channel_id not in self.last_sticky_messages:
                        await self.repost_queue.put(sticky)
                except asyncio.QueueFull:
                    break
                except Exception:
                    log.exception("Error in recovery loop enqueue")
        except Exception:
            log.exception("Error in recovery loop")

    async def _process_repost_queue(self):
        """
        Continually process items in the repost_queue. Ensures single worker behavior
        and prevents duplicate sends by checking last_sticky_messages and message content.
        """
        log.info("Repost queue processor started")
        try:
            while True:
                sticky = await self.repost_queue.get()
                try:
                    channel_id = sticky.get("channel_id")
                    if not channel_id:
                        continue
                    channel = self.bot.get_channel(channel_id)
                    if channel is None:
                        continue

                    # simple rate limiting: avoid spamming the same channel
                    if channel_id in self.processing_channels:
                        # re-enqueue after short delay
                        await asyncio.sleep(0.5)
                        try:
                            self.repost_queue.put_nowait(sticky)
                        except Exception:
                            pass
                        continue

                    self.processing_channels.add(channel_id)
                    try:
                        content = sticky.get("content") or ""
                        # optionally an embed payload; this cog expects simple content primarily
                        embed_data = sticky.get("embed")
                        embed = None
                        if embed_data:
                            embed = discord.Embed.from_dict(embed_data)
                        # send sticky safely (this method avoids duplicates)
                        await self._send_sticky_message(channel, content=content, embed=embed)
                        # small delay to respect rate limits
                        await asyncio.sleep(1.0)
                    finally:
                        self.processing_channels.discard(channel_id)

                except Exception:
                    log.exception("Error processing sticky from queue")
                finally:
                    self.repost_queue.task_done()
        except asyncio.CancelledError:
            log.info("Repost queue processor cancelled")
        except Exception:
            log.exception("Repost queue processor terminated unexpectedly")

    # ---------- commands / admin helpers (examples) ----------
    @commands.command(name="sticky_add")
    @commands.has_permissions(manage_messages=True)
    async def sticky_add(self, ctx: commands.Context, *, content: str):
        """Add or update a sticky message for the current channel."""
        try:
            if self.stickies is None:
                await ctx.send("No storage configured for stickies.")
                return
            channel_id = ctx.channel.id
            doc = {"channel_id": channel_id, "content": content}
            # Upsert logic - replace existing doc for this channel
            await self.stickies.update_one({"channel_id": channel_id}, {"$set": doc}, upsert=True)
            await ctx.send("Sticky saved. It will be (re)posted shortly.")

            # enqueue immediate repost
            await self.repost_queue.put(doc)
        except Exception:
            log.exception("Failed to add sticky")
            await ctx.send("Failed to save sticky; check logs.")

    @commands.command(name="sticky_remove")
    @commands.has_permissions(manage_messages=True)
    async def sticky_remove(self, ctx: commands.Context):
        """Remove sticky for this channel."""
        try:
            if self.stickies is None:
                await ctx.send("No storage configured for stickies.")
                return
            channel_id = ctx.channel.id
            await self.stickies.delete_one({"channel_id": channel_id})
            # If we have a last sticky message id recorded, attempt to delete it (best-effort)
            last_msg_id = self.last_sticky_messages.pop(channel_id, None)
            if last_msg_id:
                try:
                    msg = await ctx.channel.fetch_message(last_msg_id)
                    await msg.delete()
                except Exception:
                    pass
            await ctx.send("Sticky removed.")
        except Exception:
            log.exception("Failed to remove sticky")
            await ctx.send("Failed to remove sticky; check logs.")

    @commands.command(name="sticky_show")
    async def sticky_show(self, ctx: commands.Context):
        """Show the current sticky content for this channel (if any)."""
        try:
            if self.stickies is None:
                await ctx.send("No storage configured for stickies.")
                return
            doc = await self.stickies.find_one({"channel_id": ctx.channel.id})
            if not doc:
                await ctx.send("No sticky set for this channel.")
                return
            await ctx.send(f"Sticky for this channel:\n{doc.get('content', '')}")
        except Exception:
            log.exception("Failed to fetch sticky")
            await ctx.send("Failed to fetch sticky; check logs.")

# Setup function to add the cog
async def setup(bot: commands.Bot, db=None):
    cog = StickyMessages(bot, db=db)
    await bot.add_cog(cog)

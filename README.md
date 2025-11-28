<div align="center">

![Banner](template.gif)

# 🤖 Poison Bot
### *Feature-Rich Discord Server Management*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Discord.py](https://img.shields.io/badge/discord.py-2.0+-blue.svg)](https://github.com/Rapptz/discord.py)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/vasud3v/poison/graphs/commit-activity)
[![MongoDB](https://img.shields.io/badge/MongoDB-Required-green.svg)](https://www.mongodb.com/)
[![Cogs](https://img.shields.io/badge/Cogs-30+-orange.svg)](#)
[![Commands](https://img.shields.io/badge/Commands-100+-brightgreen.svg)](#)

*A powerful, modular Discord bot with extensive server management and engagement features*

[Features](#-features) • [Installation](#-installation) • [Configuration](#-configuration) • [Commands](#-commands) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

A comprehensive Discord bot built with discord.py, featuring a modular cog-based architecture for easy maintenance and scalability. Designed with performance and reliability in mind, the bot includes advanced features for server management, user engagement, moderation, and entertainment.

### 🎯 Key Highlights

<table>
<tr>
<td width="50%">

**🚀 Performance**
- Optimized async operations
- MongoDB connection pooling
- Smart caching systems
- Memory leak prevention

**🔧 Modular Design**
- 30+ independent cogs
- Hot-reload support
- Easy to extend
- Clean architecture

**🛡️ Production Ready**
- Comprehensive error handling
- Automatic retries
- Rate limit protection
- Graceful degradation

</td>
<td width="50%">

**🎨 Highly Customizable**
- Per-server configurations
- Custom emojis & colors
- Configurable cooldowns
- Flexible permissions

**📊 Resource Efficient**
- Automatic cleanup tasks
- Connection pooling
- Cache management
- Low memory footprint

**🔄 Smart Command Sync**
- Exponential backoff
- Automatic recovery
- Status monitoring
- Zero manual intervention

</td>
</tr>
</table>

## ✨ Features

<div align="center">

### 🎯 Feature Overview

| Category | Features | Commands | Database |
|----------|----------|----------|----------|
| 🛡️ **Moderation** | 7 systems | 20+ | MongoDB + SQLite |
| 📊 **Tracking** | 4 systems | 15+ | MongoDB |
| 👥 **Engagement** | 8 systems | 25+ | MongoDB + SQLite |
| 🎤 **Voice** | 4 systems | 15+ | MongoDB |
| 🎮 **Entertainment** | 3 systems | 10+ | MongoDB |
| 🎨 **Utility** | 7 systems | 20+ | SQLite |

**Total: 33 Systems • 105+ Commands • 50+ Features**

</div>

### 🛡️ Moderation & Management

- **� Verifnication System** - Ticket-based verification with transcript support and customizable workflows
- **� Quarantinme System** - Advanced mute system with:
  - Jail channel for isolated communication
  - Case tracking with unique IDs
  - Appeal system with Discord modals
  - Auto-unmute with duration support (s/m/h/d)
  - DM notifications to muted users
  - Moderator role configuration
- **🗑️ Purge Commands** - Bulk message deletion with filters:
  - Delete by bots
  - Delete by specific users
  - Delete your own messages
  - Respects Discord's 14-day limitation
- **🔨 Ban Management** - Enhanced ban system with:
  - Custom ban commands per server
  - Random sarcastic DM messages to banned users
  - Customizable ban responses from file
  - Real-time file watching for response updates

### � Activyity Tracking & Engagement

- **📈 Leaderboards** - Comprehensive activity tracking:
  - **Chat Leaderboard**: Track message activity
  - **Voice Leaderboard**: Track voice channel time
  - Daily, weekly, monthly, and all-time statistics
  - Live-updating leaderboard messages (every 5 minutes)
  - Star of the week highlights
  - Historical archives with TTL
  - Timezone support for accurate resets
  - Pagination for large leaderboards
  
- **🔢 Counting Game** - Sequential counting system:
  - Validation to prevent same user counting twice
  - Custom emoji reactions
  - Statistics and leaderboards
  - Record tracking
  - Ban system for rule breakers
  - Auto-reset on wrong numbers
  - Rate limit protection
  
- **💀 Skullboard** - Reaction-based message highlighting:
  - Configurable threshold and emoji
  - Auto-threading for popular posts
  - Milestone announcements (10, 25, 50 reactions)
  - Author and reactor statistics
  - User and channel blacklists
  - Live count updates
  - Anti-spam protection
  - Full media support (images, GIFs, videos)

### 👥 User Engagement

- **� AFK Sysmtem** - Comprehensive AFK management:
  - Global or server-specific AFK modes
  - Automatic nickname prefixing with [AFK]
  - Mention tracking while AFK
  - Paginated mention summary on return
  - Colorful embeds with jump links
  - Cooldown system
  - MongoDB-backed with caching
  
- **🤫 Confession System** - Anonymous confessions:
  - Modal-based submission with image support
  - Reply system with automatic threading
  - Report system (3 reports = auto-remove)
  - Ban system for abusers
  - Customizable embed colors
  - Log channel for moderation
  - Persistent button views
  
- **🤖 Auto Responder** - Keyword-based responses:
  - Exact message matching
  - Placeholder support ({user}, {server}, {channel}, {date}, {time})
  - SQLite database with migration from JSON
  - Modal-based configuration
  - Multi-line response support
  - Duplicate response prevention
  
- **👋 Greeting System** - Welcome messages:
  - 10 randomized default greetings
  - Custom greeting messages
  - Configurable cooldown per channel
  - Auto-delete after specified time
  - Placeholder support
  - Test command for verification
  - Error tracking and logging
  
- **📌 Sticky Messages** - Two systems available:
  - **Simple Sticky**: Basic persistent messages
  - **Sticky Button**: Interactive buttons with Discohook JSON embeds
    - Up to 20 buttons per sticky
    - Ephemeral responses
    - Auto-repost to stay at bottom
    - Periodic checks every minute
    - Queue system for race condition prevention
  
- **🔍 Snipe Commands** - Message recovery (Admin only)
- **🎁 Giveaways** - Feature-rich giveaway system:
  - Reaction-based entry
  - Fake participant filling
  - Force winner selection
  - Duration extension
  - Statistics tracking
  - Pagination for entries
  
- **💎 Drops** - Random reward drops with cooldown management

### 🎤 Voice Channel Features

- **🎙️ VC Manager** - Comprehensive voice management:
  - `.pull <user>` - Pull user to your channel
  - `.push <user> <channel>` - Push user to another channel
  - `.kick <user>` - Kick user from voice
  - `.vcmute <user>` - Voice mute user
  - `.vcunmute <user>` - Voice unmute user
  - `.lock` - Lock your voice channel
  - `.unlock` - Unlock your voice channel
  - `.summon <user>` / `/summon` - Summon user via DM
  - All commands have 5-second cooldowns
  
- **🎭 VC Roles** - Automatic role assignment:
  - Configure roles for specific voice channels
  - Manual sync command
  - Persistent role tracking
  
- **🔊 Always VC** - Persistent voice channel monitoring
- **🎵 Drag Me** - Voice channel movement commands

### 🎮 Entertainment & Games

- **🎯 Match Making** - Advanced matchmaking system:
  - Queue management
  - Team balancing
  - Report channel configuration
  - Pause/resume functionality
  - Statistics tracking
  - Queue panel display
  
- **📢 Bulk Ping** - Mass mention system with cooldowns
- **🧵 Thread Management** - Auto-thread creation:
  - Toggle per channel
  - Status viewing
  - Statistics tracking

### 🎨 Utility & Customization

- **🖼️ Avatar Commands** - Display user avatars
- **🌟 Status Changer** - Dynamic bot status rotation
- **📸 Media Commands** - Media-only channel enforcement:
  - Toggle media-only mode
  - Set log channel
  - View configuration
  
- **ℹ️ Info Commands**:
  - `.si` / `.serverinfo` - Detailed server information
  - `.roleinfo <role>` - Role details
  - `.mc` / `.membercount` - Member count
  - `.settimezone <tz>` - Set server timezone
  
- **📊 Stats Tracking** - Comprehensive server statistics with 15-second cooldown
- **😎 Steal Emojis** - Copy emojis from other servers (requires Manage Emojis permission)
- **🎫 Request Role** - User-initiated role requests:
  - Custom role name mapping
  - Multi-role support
  - Role descriptions
  - Log channel configuration
  - List and search functionality
  
- **📎 Attachment React** - Auto-react to attachments in specific channels

## ⚡ Quick Start

### 5-Minute Setup

```bash
# 1. Clone and install
git clone https://github.com/vasud3v/poison.git
cd poison
pip install -r requirements.txt

# 2. Configure
cp .env.example .env  # Create from template
nano .env             # Add your tokens

# 3. Run
python main.py

# 4. Setup in Discord
/setup-mute @Moderator
/setup-verify #verify #logs
/greet_enable #welcome
```

### First Commands to Try

```bash
.ping              # Check bot status
.cogs              # View loaded features
.syncstatus        # Check command sync
/count settings    # Setup counting game
/confess           # Try confession system
```

## 🚀 Installation

### Prerequisites

```diff
+ Python 3.8 or higher
+ pip (Python package manager)
+ MongoDB (for database features)
+ A Discord Bot Token
```

> 💡 **Get your Discord Bot Token** at [Discord Developer Portal](https://discord.com/developers/applications)

### Step 1: Clone the Repository
```bash
git clone https://github.com/vasud3v/poison.git
cd poison
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
Create a `.env` file in the root directory:
```env
DISCORD_TOKEN=your_discord_bot_token_here
WEBHOOK_URL=your_webhook_url_for_error_reporting
MONGO_URL=mongodb://localhost:27017/
AUTO_SYNC_COMMANDS=true  # Set to false to disable auto-sync
```

### Step 4: Run the Bot
```bash
python main.py
```

## ⚙️ Configuration

### Environment Variables
| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `DISCORD_TOKEN` | Your Discord bot token | ✅ Yes | - |
| `WEBHOOK_URL` | Webhook URL for error reporting | ✅ Yes | - |
| `MONGO_URL` | MongoDB connection URL | ✅ Yes | - |
| `AUTO_SYNC_COMMANDS` | Auto-sync slash commands | ❌ No | `true` |

### Bot Intents
The bot requires the following intents (configured in main.py):
- `members` - For member tracking and verification
- `presences` - For status monitoring
- `message_content` - For command processing and content moderation

### Directory Structure
```
├── cogs/                    # Bot command modules
│   ├── counting/           # Counting game system
│   │   ├── counting.py
│   │   └── README.md
│   ├── giveaways/          # Giveaway management
│   │   ├── giveaway_core.py
│   │   ├── giveaway_admin.py
│   │   ├── config.py
│   │   └── README.md
│   ├── leaderboard/        # Activity tracking
│   │   ├── chat_leaderboard_cog.py
│   │   ├── voice_leaderboard_cog.py
│   │   ├── star_of_the_week_cog.py
│   │   ├── leaderboard_config.py
│   │   ├── utils.py
│   │   └── README.md
│   ├── purge/              # Message deletion
│   │   ├── purge.py
│   │   └── README.md
│   ├── quarantine/         # Mute & appeal system
│   │   ├── quarantine_system.py
│   │   ├── appeal_system.py
│   │   ├── config.py
│   │   └── README.md
│   ├── skullboard/         # Message highlighting
│   │   ├── skull.py
│   │   └── README.md
│   ├── sticky-button/      # Sticky messages with buttons
│   │   ├── sticky_buttons.py
│   │   └── README.md
│   └── *.py                # Individual cog files
├── logs/                    # Auto-generated log files
├── database/                # Database storage (SQLite & MongoDB)
├── main.py                  # Bot entry point
├── requirements.txt         # Python dependencies
├── responses.txt            # Custom ban responses
├── .env                     # Environment variables (create this)
└── .gitignore              # Git ignore rules
```

## 📝 Commands

### Prefix Commands (`.` prefix)

#### Bot Management (Owner Only)
- `.ping` - Check bot latency and response time
- `.sync` - Manually sync slash commands
- `.cogs` - List all loaded cogs
- `.reload [cog]` - Reload specific cog or all cogs
- `.syncstatus` - Check command sync status

#### Voice Management
- `.pull <user>` - Pull user to your voice channel
- `.push <user> <channel>` - Push user to another channel
- `.kick <user>` - Kick user from voice
- `.vcmute <user>` - Voice mute user
- `.vcunmute <user>` - Voice unmute user
- `.lock` - Lock your voice channel
- `.unlock` - Unlock your voice channel
- `.summon <user>` - Summon user to your channel

#### Utility
- `.si` / `.serverinfo` - Server information
- `.roleinfo <role>` - Role details
- `.mc` / `.membercount` - Member count
- `.stats` - Server statistics
- `.snipe` - View deleted messages (Admin only)
- `.steal` - Copy emojis from other servers
- `.settimezone <tz>` - Set server timezone

#### Role Management
- `.setupreqrole <role>` - Setup role request system
- `.setrole <name> <role> [description]` - Map custom role
- `.removerole <name> [role]` - Remove role mapping
- `.role` / `.roles` - View available roles
- `.rolelist` - List all custom roles
- `.roledesc <name>` - Show role description
- `.clearroles <user>` - Clear user's custom roles
- `.setupmultirole <name> <roles...>` - Setup multi-role
- `.resetserver` - Reset server role config
- `.deletemappedrole <role_id>` - Delete mapped role
- `.setlogchannel <channel>` - Set log channel

#### Sticky Messages
- `.sticky_add <content>` - Add sticky message
- `.sticky_remove` - Remove sticky message
- `.sticky_show` - Show current sticky

#### AFK
- `.afk [reason]` - Set AFK status (opens choice menu)

#### Quarantine (Moderation)
- `!qmute <user> <duration> [reason]` - Mute user
- `!qunmute <user> [reason]` - Unmute user
- `!mutelist` - View all active mutes
- `!case <case_id>` - View case details
- `!jailhistory <user>` - View jail messages
- `!setmodrole <role>` - Set moderator role (Admin)

### Slash Commands

#### Setup & Configuration
- `/setup-verify` - Setup verification system
- `/setup-mute <moderator_role>` - Setup quarantine system
- `/setup-confess` - Configure confession system
- `/check-muteperms` - Verify mute system
- `/reset-muteconfig CONFIRM` - Reset mute config
- `/reapply-mute-perms` - Reapply permission overwrites
- `/setban <command>` - Set custom ban command

#### Activity & Engagement
- `/count view` - View counting statistics
- `/count settings` - Configure counting system
- `/skull-setup <channel>` - Setup skullboard
- `/skull-config` - View skullboard config
- `/skull-blacklist-user <user>` - Toggle user blacklist
- `/skull-blacklist-channel <channel>` - Toggle channel blacklist
- `/skull-stats [type]` - View skullboard statistics
- `/skull-remove` - Remove skullboard
- `/skull-style <style>` - Set embed style
- `/skull-autothread <enabled>` - Toggle auto-threading
- `/skull-milestones <enabled>` - Toggle milestones

#### Giveaways
- `/giveaway-edit` - Interactive giveaway management
- `/drop` - Create reward drop
- `/reset_cooldown [user]` - Reset drop cooldown

#### Greetings
- `/greet_enable <channel>` - Enable greetings
- `/greet_disable <channel>` - Disable greetings
- `/greet_list` - List greeting channels
- `/test_greet [channel] [user]` - Test greeting

#### Confessions
- `/confess` - Submit anonymous confession
- `/confess-ban <user> <action>` - Ban/unban from confessions

#### Auto Responder
- `/autoresponder add` - Add autoresponse (modal)
- `/autoresponder remove <trigger>` - Remove autoresponse
- `/autoresponder list` - List all autoresponses
- `/autoresponder placeholders` - Show placeholders

#### Voice
- `/summon <user>` - Summon user to your channel
- `/vc-role` - Configure voice channel roles
- `/vc-role-sync` - Manually sync VC roles

#### Thread Management
- `/thread_channel` - Toggle auto-thread creation
- `/thread_status` - View thread configurations
- `/thread_stats` - View thread statistics

#### Media & Utility
- `/media-only` - Setup media-only channels
- `/mm` - Configure matchmaking system
- `/autoreact` - Manage auto-react system

#### Appeals
- `/appeal-status [appeal_id]` - Check appeal status
- `/appeal-list` - List pending appeals (Moderator)
- `/appeal-review <appeal_id>` - Review appeal (Moderator)

## 🏗️ Architecture

### Modular Cog System

The bot uses a modular architecture where each feature is implemented as a separate cog:

- ✅ Easy feature addition/removal
- ✅ Independent testing and debugging
- ✅ Clean code organization
- ✅ Hot-reloading with `.reload` command
- ✅ Shared MongoDB connection pooling

### 🔑 Key Technical Features

| Feature | Description |
|---------|-------------|
| ⏱️ **Global Cooldown System** | Prevents command spam (1 command per 0.2s per user) |
| 🚫 **Duplicate Response Prevention** | Avoids double responses with tracking system (5-minute cleanup) |
| 📡 **Automatic Error Reporting** | Webhook-based error notifications for monitoring |
| 🛑 **Graceful Shutdown** | Proper cleanup on exit with signal handlers |
| 🧹 **Periodic Resource Cleanup** | Automatic memory management every 5 minutes |
| 📝 **Rotating Log Files** | Automatic log rotation with 7-day retention |
| 🔄 **Smart Command Sync** | Rate limit handling with exponential backoff (1h → 2h → 4h → 8h → 24h max) |
| 🗄️ **Shared MongoDB Connection** | Connection pooling across all cogs with extended timeouts |
| 🎨 **Pretty Terminal Output** | Colorful terminal display with ASCII art (pyfiglet) |
| 🔒 **Thread-Safe Operations** | Asyncio locks for database transactions |
| 📊 **Caching Systems** | In-memory caching with TTL for performance |

### Smart Command Sync System

The bot includes an intelligent command sync system that:
- Detects command changes automatically via MD5 hashing
- Implements exponential backoff on rate limits (1h → 2h → 4h → 8h → 24h max)
- Caches sync status in JSON file to persist across restarts
- Auto-retries after backoff periods with background scheduler
- Minimum 1-hour interval between syncs to avoid rate limits
- Can be disabled via `AUTO_SYNC_COMMANDS=false`
- Provides `.syncstatus` command for monitoring

### Database Architecture

- **MongoDB**: Used for complex features (AFK, Confessions, Counting, Giveaways, Leaderboards, Quarantine, Skullboard, Sticky Buttons)
- **SQLite**: Used for simpler features (Auto Responder, Ban Config, Greetings)
- **Shared Connection**: Single MongoDB client shared across all cogs
- **Connection Pooling**: Optimized settings for unreliable networks
- **TTL Indexes**: Automatic cleanup of old data
- **Compound Indexes**: Fast queries for complex operations

## 🛠️ Development

### Adding New Cogs
1. Create a new Python file in the `cogs/` directory
2. Implement your cog class extending `commands.Cog`
3. Add the `setup()` function at the end
4. The bot will automatically load it on startup

Example:
```python
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def mycommand(self, ctx):
        await ctx.send("Hello!")

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

### Hot Reloading
Use `.reload [cog_name]` to reload cogs without restarting:
```
.reload counting          # Reload counting cog
.reload giveaways        # Reload all giveaway cogs
.reload                  # Reload all cogs
```

### Logging
- Logs are stored in `logs/bot.log`
- Automatic rotation at midnight (UTC)
- 7-day retention
- Console shows errors only
- File logs show INFO level and above
- Pymongo and motor logs suppressed to CRITICAL

### Custom Ban Responses
Edit `responses.txt` to customize ban messages:
- One response per line
- Use `@user` for user mention
- Use `[reason]` for ban reason
- File is watched in real-time (no restart needed)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/AmazingFeature

# 3. Commit your changes
git commit -m 'Add some AmazingFeature'

# 4. Push to the branch
git push origin feature/AmazingFeature

# 5. Open a Pull Request
```

### 📋 Contribution Guidelines

- 🐛 Report bugs with detailed reproduction steps
- 💡 Suggest features with clear use cases
- 📝 Update documentation for any changes
- ✅ Ensure code follows existing style patterns
- 🧪 Test your changes thoroughly
- 📚 Add README files for new cog folders

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💡 Support

| Method | Link |
|--------|------|
| 📖 **Documentation** | Check the README and cog-specific READMEs |
| 🐛 **Bug Reports** | [Open an Issue](https://github.com/vasud3v/poison/issues) |
| 📚 **Cog Documentation** | See individual README files in `cogs/` folders |

## � Advanced gConfiguration

### MongoDB Optimization

The bot uses optimized MongoDB settings for unreliable networks:

```python
# Connection settings in main.py
serverSelectionTimeoutMS=60000    # 60 seconds
connectTimeoutMS=60000             # 60 seconds  
socketTimeoutMS=180000             # 3 minutes
maxPoolSize=50                     # Maximum connections
minPoolSize=1                      # Minimum connections
maxIdleTimeMS=600000               # 10 minutes keep-alive
heartbeatFrequencyMS=60000         # Check every 60 seconds
```

### Custom Emoji Configuration

Many features use custom emojis. To customize them, edit the emoji IDs in the respective cog files:

**Common Emojis Used:**
- `<a:white_tick:1426439810733572136>` - Success indicator
- `<:ogs_cross:1427918018196930642>` - Error indicator
- `<:ogs_bell:1427918360401940552>` - Warning/notification
- `<:ogs_info:1427918257226121288>` - Information
- `<a:reddot:1427539828521697282>` - Error/failure

### Performance Tuning

**For Large Servers (10k+ members):**
- Leaderboard cog uses optimized queries with limits
- Giveaway system supports fake participant filling
- Connection pooling prevents database overload
- Cache systems reduce database queries

**Memory Management:**
- Automatic cache cleanup every 5-30 minutes
- Processed message tracking with size limits
- Old data cleanup with TTL indexes
- Graceful shutdown with proper cleanup

### Rate Limit Handling

The bot implements multiple layers of rate limit protection:

1. **Global Cooldown**: 1 command per 0.2s per user
2. **Command-Specific Cooldowns**: 5-15 seconds per command
3. **Message Deletion Queue**: 250ms delay between deletions
4. **Database Semaphores**: Limit concurrent operations
5. **Exponential Backoff**: For command sync failures

## 📊 Feature Comparison

| Feature | Database | Persistent | Auto-Cleanup | Cooldown |
|---------|----------|------------|--------------|----------|
| AFK System | MongoDB | ✅ | 7 days | Per-channel |
| Confessions | MongoDB | ✅ | None | None |
| Auto Responder | SQLite | ✅ | None | None |
| Greetings | SQLite | ✅ | None | Configurable |
| Counting | MongoDB | ✅ | 30 days backup | Per-message |
| Leaderboards | MongoDB | ✅ | 1 year archive | None |
| Skullboard | MongoDB | ✅ | None | 3 seconds |
| Giveaways | MongoDB | ✅ | None | None |
| Quarantine | MongoDB | ✅ | 7 days jail logs | None |

## 🐛 Troubleshooting

### Common Issues

**Bot not responding to commands:**
- Check if bot has `message_content` intent enabled
- Verify bot has `Send Messages` permission
- Check if command sync completed (use `.syncstatus`)

**Slash commands not showing:**
- Wait 1 hour after bot startup (rate limit protection)
- Use `.sync` command (owner only)
- Check `.syncstatus` for rate limit information

**MongoDB connection errors:**
- Verify `MONGO_URL` in `.env` file
- Check MongoDB Atlas IP whitelist
- Ensure network connectivity
- Check logs for specific error messages

**Permission errors:**
- Bot needs `Manage Roles` for mute system
- Bot needs `Manage Channels` for permission overwrites
- Bot's role must be higher than target roles
- Check channel-specific permissions

**Leaderboard not updating:**
- Verify MongoDB connection
- Check if channels are configured
- Ensure bot can read message history
- Wait for 5-minute update cycle

### Debug Commands

```bash
# Check bot status
.ping

# View loaded cogs
.cogs

# Check command sync status
.syncstatus

# Reload specific cog
.reload <cog_name>

# View logs
tail -f logs/bot.log
```

## 📈 Scaling Considerations

### For Large Servers (10k+ members)

**Recommended Settings:**
- Enable MongoDB connection pooling (already configured)
- Use dedicated MongoDB instance or cluster
- Increase `maxPoolSize` if needed
- Monitor memory usage with cleanup tasks

**Leaderboard Optimization:**
- Limit `MAX_MEMBERS_FETCH` in config
- Increase update interval if needed
- Use pagination for large leaderboards
- Archive old data regularly

**Giveaway Optimization:**
- Use fake participant filling sparingly
- Limit concurrent giveaways
- Clean up ended giveaways periodically

### For Multiple Servers

The bot supports multiple servers simultaneously:
- Each server has isolated configurations
- Shared MongoDB connection across all servers
- Per-guild caching for performance
- Automatic cleanup when bot leaves server

## 💡 Pro Tips

### For Server Owners

1. **Start Small**: Enable features gradually. Don't configure everything at once.
2. **Test First**: Use test commands like `/test_greet` before going live.
3. **Monitor Logs**: Check `logs/bot.log` regularly for issues.
4. **Use Cooldowns**: Configure appropriate cooldowns to prevent spam.
5. **Backup Configs**: MongoDB has automatic backups, but export important configs.

### For Developers

1. **Hot Reload**: Use `.reload <cog>` instead of restarting the bot.
2. **Check Sync Status**: Use `.syncstatus` before manually syncing.
3. **Read Cog READMEs**: Each major feature has detailed documentation.
4. **Use Logging**: Add logging to your custom cogs for debugging.
5. **Test Locally**: Always test changes in a development server first.

### Performance Tips

1. **MongoDB Atlas**: Use MongoDB Atlas for better reliability.
2. **Connection Pooling**: Already optimized, but monitor if you have 100+ servers.
3. **Cache Cleanup**: Automatic, but you can adjust intervals in cog files.
4. **Rate Limits**: Respect Discord's rate limits - the bot handles this automatically.
5. **Memory Usage**: Monitor with `htop` or similar tools.

### Common Mistakes to Avoid

❌ **Don't restart the bot repeatedly** - This triggers rate limits  
✅ Use `.reload` for code changes

❌ **Don't sync commands manually too often** - Wait for auto-sync  
✅ Check `.syncstatus` first

❌ **Don't give bot Administrator permission** - Security risk  
✅ Grant only needed permissions

❌ **Don't ignore error logs** - They contain important information  
✅ Check logs regularly and fix issues

❌ **Don't use the same MongoDB for production and testing**  
✅ Use separate databases

## 🔐 Security Best Practices

### Environment Variables
- Never commit `.env` file to version control
- Use strong, unique tokens
- Rotate tokens periodically
- Limit webhook URL access

### Permissions
- Follow principle of least privilege
- Only grant necessary permissions
- Use role hierarchy properly
- Audit permission changes regularly

### Moderation
- Configure moderator roles properly
- Use case tracking for accountability
- Enable logging channels
- Review appeal system regularly

### Data Privacy
- Confession system is anonymous
- AFK mentions stored temporarily (7 days)
- Jail logs auto-delete after 7 days
- Archive data has 1-year TTL

## 📚 Additional Resources

### Cog-Specific Documentation
Each major feature has its own detailed README:
- [Counting System](cogs/counting/README.md)
- [Giveaway System](cogs/giveaways/README.md)
- [Leaderboard System](cogs/leaderboard/README.md)
- [Purge System](cogs/purge/README.md)
- [Quarantine & Appeals](cogs/quarantine/README.md)
- [Skullboard System](cogs/skullboard/README.md)
- [Sticky Button System](cogs/sticky-button/README.md)

### External Resources
- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [MongoDB Motor Documentation](https://motor.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/docs)
- [Discord.py Server](https://discord.gg/dpy)

## 🎯 Roadmap

### Planned Features
- [ ] Web dashboard for configuration
- [ ] Advanced analytics and insights
- [ ] Custom command builder
- [ ] Backup and restore system
- [ ] Multi-language support
- [ ] Webhook integration system

### In Progress
- [x] Smart command sync system
- [x] Comprehensive error handling
- [x] Performance optimizations
- [x] Documentation improvements

## 🙏 Acknowledgments

<div align="center">

### Built With Amazing Technologies 🚀

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/Discord.py-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://github.com/Rapptz/discord.py)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)

</div>

- 🐍 **Python 3.8+** - Modern async/await syntax
- 🤖 **discord.py** - Powerful Discord API wrapper
- 🗄️ **MongoDB & Motor** - Async database operations with connection pooling
- 🗄️ **aiosqlite** - Async SQLite operations
- 🌐 **aiohttp** - Async HTTP client/server framework
- 🎨 **Pillow** - Image processing capabilities
- 📝 **pyfiglet** - ASCII art for terminal output
- 🔧 **python-dotenv** - Environment variable management
- 🕐 **pytz** - Timezone support

---

<div align="center">

### ⭐ Star this repository if you find it helpful! ⭐

<br>

[![GitHub stars](https://img.shields.io/github/stars/vasud3v/poison?style=social)](https://github.com/vasud3v/poison/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/vasud3v/poison?style=social)](https://github.com/vasud3v/poison/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/vasud3v/poison?style=social)](https://github.com/vasud3v/poison/watchers)

<br>

### Made with ❤️ and ☕ by **vasud3v**

[![GitHub](https://img.shields.io/badge/GitHub-vasud3v-181717?style=for-the-badge&logo=github)](https://github.com/vasud3v)

*Crafting powerful Discord bots, one commit at a time* ✨

</div>

---

## 🎉 Why Choose Poison Bot?

<div align="center">

### The Complete Package

| Aspect | Details |
|--------|---------|
| 🚀 **Performance** | Optimized async operations, connection pooling, smart caching |
| 🛡️ **Reliability** | Error handling, automatic retries, graceful degradation |
| 📊 **Scalability** | Tested with 10k+ member servers, supports 100+ servers |
| 🔧 **Maintainability** | Modular design, hot-reload, comprehensive logging |
| 📚 **Documentation** | 8 README files, inline comments, usage examples |
| 🎨 **Customization** | Configurable colors, emojis, messages, cooldowns |
| 🔐 **Security** | Role hierarchy, permission checks, data privacy |
| 💪 **Feature-Rich** | 50+ features, 100+ commands, 30+ cogs |

### Perfect For

✅ **Community Servers** - Engagement features, leaderboards, giveaways  
✅ **Gaming Servers** - Voice management, matchmaking, stats tracking  
✅ **Moderation Teams** - Quarantine system, appeals, case tracking  
✅ **Large Servers** - Optimized for 10k+ members with connection pooling  
✅ **Developers** - Clean code, modular design, easy to extend

</div>

---

## 🌟 What Makes It Special?

### Unique Features

1. **Smart Command Sync** - Industry-leading command sync with exponential backoff and automatic recovery
2. **Dual Sticky Systems** - Both simple text and interactive button-based sticky messages
3. **Comprehensive AFK** - Global/server modes with mention tracking and pagination
4. **Advanced Quarantine** - Full appeal workflow with Discord modals and case tracking
5. **Real-time Updates** - Leaderboards update every 5 minutes, ban responses update instantly
6. **Production Ready** - Used in real servers with 10k+ members

### Technical Excellence

- **Zero Downtime Updates**: Hot-reload any cog without restarting
- **Intelligent Rate Limiting**: Multi-layer protection prevents API abuse
- **Database Optimization**: Shared connections, TTL indexes, compound queries
- **Memory Management**: Automatic cleanup prevents memory leaks
- **Error Recovery**: Graceful degradation and automatic retries
- **Monitoring**: Built-in logging and webhook error reporting

---

## 📞 Get Help

<div align="center">

### Need Assistance?

| Type | Resource |
|------|----------|
| 🐛 **Bug Report** | [Open an Issue](https://github.com/vasud3v/poison/issues/new?labels=bug) |
| 💡 **Feature Request** | [Open an Issue](https://github.com/vasud3v/poison/issues/new?labels=enhancement) |
| 📖 **Documentation** | Check README files in each cog folder |
| ❓ **Questions** | Read the [FAQ](#-frequently-asked-questions) section |
| 🔧 **Troubleshooting** | See [Troubleshooting](#-troubleshooting) guide |

</div>

---

## 📜 Version History

### Current Version: 2.0
- ✅ Complete rewrite with discord.py 2.0
- ✅ Smart command sync system
- ✅ MongoDB integration
- ✅ 50+ features implemented
- ✅ Comprehensive documentation

### Coming Soon
- 🔄 Web dashboard
- 🔄 Advanced analytics
- 🔄 Multi-language support
- 🔄 Webhook integrations

---



## ✅ Complete Feature Checklist

### 🛡️ Moderation (7/7)
- [x] Verification system with tickets
- [x] Quarantine/mute system with appeals
- [x] Ban management with custom messages
- [x] Purge with advanced filters
- [x] Case tracking system
- [x] Moderator role configuration
- [x] Auto-unmute with duration support

### 📊 Activity & Tracking (4/4)
- [x] Chat leaderboard (daily/weekly/monthly/all-time)
- [x] Voice leaderboard with time tracking
- [x] Counting game with validation
- [x] Skullboard (reaction highlighting)

### 👥 Engagement (8/8)
- [x] AFK system (global/server-specific)
- [x] Confession system with reports
- [x] Auto responder with placeholders
- [x] Greeting system with customization
- [x] Sticky messages (simple & button)
- [x] Snipe (deleted message recovery)
- [x] Giveaways with fake filling
- [x] Drops with cooldown management

### 🎤 Voice (4/4)
- [x] VC Manager (pull/push/kick/mute/lock)
- [x] VC Roles (auto-assign)
- [x] Always VC monitoring
- [x] Summon system with DM

### 🎮 Entertainment (3/3)
- [x] Match making with queue
- [x] Bulk ping system
- [x] Thread auto-creation

### 🎨 Utility (7/7)
- [x] Avatar display
- [x] Status changer
- [x] Media-only channels
- [x] Info commands (server/role/member)
- [x] Stats tracking
- [x] Emoji stealing
- [x] Role request system

### 🔧 Technical (10/10)
- [x] Smart command sync with backoff
- [x] MongoDB connection pooling
- [x] SQLite for simple features
- [x] Global cooldown system
- [x] Duplicate response prevention
- [x] Automatic error reporting
- [x] Graceful shutdown
- [x] Periodic cleanup tasks
- [x] Hot-reload support
- [x] Pretty terminal output

### 📚 Documentation (7/7)
- [x] Main README
- [x] Cog-specific READMEs
- [x] Installation guide
- [x] Configuration guide
- [x] Command reference
- [x] Troubleshooting guide
- [x] FAQ section

**Total Features: 50+ implemented and documented**

---

## 📊 Statistics

<div align="center">

| Metric | Count |
|--------|-------|
| **Total Cogs** | 30+ |
| **Slash Commands** | 50+ |
| **Prefix Commands** | 50+ |
| **Database Collections** | 20+ |
| **Lines of Code** | 15,000+ |
| **Features** | 50+ |
| **README Files** | 8 |

</div>

---

## ❓ Frequently Asked Questions

### General Questions

**Q: How do I get started with the bot?**
A: Follow the installation steps above, configure your `.env` file, and run `python main.py`. Use `/setup-mute` and other setup commands to configure features.

**Q: Can I use this bot on multiple servers?**
A: Yes! The bot supports multiple servers simultaneously with isolated configurations per server.

**Q: How do I update the bot?**
A: Pull the latest changes with `git pull`, install any new dependencies with `pip install -r requirements.txt`, and restart the bot. Use `.reload` for hot-reloading cogs without restart.

**Q: Is MongoDB required?**
A: Yes, for most features. Some simple features use SQLite, but MongoDB is required for AFK, Confessions, Counting, Giveaways, Leaderboards, Quarantine, and Skullboard.

### Command Sync Issues

**Q: Why aren't my slash commands showing up?**
A: The bot uses smart command sync with rate limit protection. Wait 1 hour after startup, or check `.syncstatus` to see if you're rate limited. Use `.sync` (owner only) to force sync.

**Q: What does "Rate Limited" mean in syncstatus?**
A: Discord limits how often you can sync commands. The bot implements exponential backoff (1h → 2h → 4h → 8h → 24h max) and will automatically retry. **Don't restart the bot repeatedly!**

**Q: How do I disable auto-sync?**
A: Set `AUTO_SYNC_COMMANDS=false` in your `.env` file. You'll need to manually sync with `.sync` command.

### Feature-Specific Questions

**Q: How do I set up the mute system?**
A: Run `/setup-mute <moderator_role>` to create the Muted role, jail channel, and punishment-logs channel. Then use `!qmute <user> <duration> [reason]` to mute users.

**Q: What duration formats are supported for mutes?**
A: Use `s` for seconds, `m` for minutes, `h` for hours, `d` for days. Examples: `30s`, `10m`, `2h`, `7d`

**Q: How do I customize ban messages?**
A: Edit `responses.txt` file (one response per line). Use `@user` for user mention and `[reason]` for ban reason. Changes are detected in real-time.

**Q: Can users appeal their mutes?**
A: Yes! Users receive a DM with an appeal button. Moderators can review appeals with `/appeal-list` and `/appeal-review`.

**Q: How do I set up the counting game?**
A: Use `/count settings` to configure the counting channel, emoji, and other options. Users count sequentially in that channel.

**Q: How do leaderboards work?**
A: The bot tracks chat messages and voice time automatically. Leaderboards update every 5 minutes and show daily, weekly, monthly, and all-time statistics.

**Q: What's the difference between the two sticky systems?**
A: Simple sticky (`.sticky_add`) is basic text. Sticky Button (`/sticky-manage`) supports interactive buttons with custom embeds using Discohook JSON.

**Q: How do I create a giveaway?**
A: Use `/giveaway-edit` for an interactive menu. You can create, fill with fake participants, force winners, extend duration, or cancel giveaways.

### Troubleshooting

**Q: Bot is not responding to messages**
A: Check if `message_content` intent is enabled in Discord Developer Portal. Verify bot has `Send Messages` permission in the channel.

**Q: "Missing permissions" error**
A: Ensure bot's role is higher than target roles. Check specific permissions like `Manage Roles`, `Manage Channels`, `Manage Messages`.

**Q: MongoDB connection timeout**
A: Check your `MONGO_URL` in `.env`. If using MongoDB Atlas, whitelist your IP address. The bot uses extended timeouts (60s) for unreliable networks.

**Q: Leaderboard not updating**
A: Wait for the 5-minute update cycle. Check if MongoDB is connected. Verify bot has `Read Message History` permission.

**Q: Commands have cooldowns**
A: Most commands have cooldowns to prevent spam (5-15 seconds). Voice commands have 5-second cooldowns. This is intentional.

### Customization

**Q: How do I change the bot's prefix?**
A: Edit `command_prefix="."` in `main.py` to your desired prefix.

**Q: Can I customize embed colors?**
A: Yes! Most cogs have color constants at the top of their files. Edit the hex values (e.g., `0x2f3136`).

**Q: How do I add custom emojis?**
A: Replace emoji IDs in the cog files. Find emojis like `<a:white_tick:1426439810733572136>` and replace with your server's emoji IDs.

**Q: Can I disable specific features?**
A: Yes! Simply don't load the cog by removing it from the `cogs/` directory or commenting out its setup in the file.

### Performance

**Q: How much RAM does the bot use?**
A: Typically 100-300MB depending on server count and active features. Memory is automatically cleaned up every 5 minutes.

**Q: Can it handle large servers?**
A: Yes! The bot is optimized for servers with 10k+ members. Features like leaderboards and giveaways have special optimizations for large servers.

**Q: How many servers can it handle?**
A: Tested with 50+ servers. MongoDB connection pooling and caching systems allow scaling to hundreds of servers.

## 💡 Usage Examples

### Setting Up a New Server

```bash
# 1. Setup verification system
/setup-verify embed_channel:#verify log_channel:#logs

# 2. Setup mute/quarantine system
/setup-mute moderator_role:@Moderator
!setmodrole @Moderator

# 3. Setup confession system
/setup-confess submission-channel:#confessions log-channel:#mod-logs embed-color:#2f3136

# 4. Enable greetings
/greet_enable channel:#welcome cooldown:60 delete_after:60

# 5. Setup counting game
/count settings counting_channel:#counting emoji:💀 threshold:2

# 6. Setup leaderboards (if using leaderboard cog)
# Configure via cog-specific commands

# 7. Setup custom ban command
/setban ban
# Now use .ban @user reason to ban with custom messages
```

### Common Moderation Workflows

```bash
# Mute a user for 1 hour
!qmute @user 1h Spamming in chat

# View all active mutes
!mutelist

# Check a specific case
!case 42

# Review pending appeals
/appeal-list

# Approve an appeal
/appeal-review appeal_id:123 approve

# Purge bot messages
.purge 50 bots

# Purge specific user's messages
.purge 20 @user

# Ban with custom message
.ban @user Breaking server rules
```

### Voice Channel Management

```bash
# Pull user to your channel
.pull @user

# Push user to another channel
.push @user #General Voice

# Kick from voice
.kick @user

# Voice mute
.vcmute @user

# Lock your channel
.lock

# Summon user (sends DM)
.summon @user
```

### Activity Tracking

```bash
# View counting stats
/count view

# View skullboard stats
/skull-stats type:authors

# Check leaderboard (if configured)
# Leaderboards auto-update every 5 minutes
```

### Role Management

```bash
# Setup role request system
.setupreqrole @Member

# Map custom role name
.setrole "VIP" @VIP "Special VIP role"

# List available roles
.rolelist

# User requests role
# Users type the custom name to get the role
```

### Auto Responder Setup

```bash
# Add autoresponse with modal
/autoresponder add
# Fill in: Trigger: "hello", Response: "Hello {user}! Welcome to {server}!"

# List all autoresponses
/autoresponder list

# Remove autoresponse
/autoresponder remove trigger:hello

# View placeholders
/autoresponder placeholders
```

### Giveaway Management

```bash
# Open giveaway menu
/giveaway-edit

# Select "Fill" to add fake participants
# Enter message ID, total reactions, duration

# Select "Force Winner" to manually choose winners
# Enter message ID and user mentions/IDs

# Select "Stats" to view giveaway statistics
```

---



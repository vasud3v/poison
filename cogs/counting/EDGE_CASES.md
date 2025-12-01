# Edge Cases Handled

## Input Validation Edge Cases

### ✅ Negative Numbers
- **Case**: User posts "-5"
- **Handling**: Rejected and deleted (non_positive_number)

### ✅ Zero
- **Case**: User posts "0"
- **Handling**: Rejected and deleted (non_positive_number)

### ✅ Leading Zeros
- **Case**: User posts "007" instead of "7"
- **Handling**: Rejected and deleted (leading_zeros)

### ✅ Extremely Large Numbers
- **Case**: User posts "999999999999"
- **Handling**: Rejected if > 1 billion (number_too_large)

### ✅ Decimal Numbers
- **Case**: User posts "3.14"
- **Handling**: Rejected (invalid_format) - only pure integers allowed

### ✅ Multiple Numbers
- **Case**: User posts "1 2 3" or "123 456"
- **Handling**: Rejected and deleted (multi_number)

### ✅ Text with Numbers
- **Case**: User posts "the number is 5"
- **Handling**: Rejected (invalid_format) - must be pure integer

### ✅ Scientific Notation
- **Case**: User posts "1e5"
- **Handling**: Rejected (invalid_format)

## Concurrency Edge Cases

### ✅ Race Condition on Count Read
- **Case**: Two users post at the exact same time
- **Handling**: Lock ensures only one processes at a time, second gets race condition error

### ✅ Lock Creation Race
- **Case**: Multiple messages arrive before lock is created
- **Handling**: `setdefault()` ensures atomic lock creation

### ✅ Database Update Race
- **Case**: Count changes between read and update
- **Handling**: Atomic update with filter on current value, fails gracefully if changed

### ✅ Same User Twice (Race)
- **Case**: User posts twice before first is processed
- **Handling**: Lock prevents this, second message is rejected

## Permission Edge Cases

### ✅ Bot Loses Permissions Mid-Count
- **Case**: Admin removes Manage Messages permission
- **Handling**: Bot checks permissions and logs warning hourly

### ✅ Bot Can't Add Reactions
- **Case**: Bot lacks Add Reactions permission
- **Handling**: Silently fails with fallback, logs warning

### ✅ Bot Can't Delete Messages
- **Case**: Bot lacks Manage Messages permission
- **Handling**: Deletion queued but fails, logged as warning

### ✅ Bot Can't Send Messages
- **Case**: Bot lacks Send Messages permission
- **Handling**: Silently fails, no error messages sent

## Channel Edge Cases

### ✅ Counting Channel Deleted
- **Case**: Admin deletes the counting channel
- **Handling**: `on_guild_channel_delete` clears setting and notifies via log channel

### ✅ Log Channel Deleted
- **Case**: Admin deletes the log channel
- **Handling**: Logs fail silently, no errors

### ✅ Channel Permissions Changed
- **Case**: Channel becomes private/bot loses access
- **Handling**: Permission check fails, logs warning

### ✅ Bot Removed from Guild
- **Case**: Bot is kicked from server
- **Handling**: `on_guild_remove` cleans up all caches and locks

## User Edge Cases

### ✅ User Leaves Server
- **Case**: User leaves but is in leaderboard
- **Handling**: User ID still shows in leaderboard (by design)

### ✅ User Banned from Counting
- **Case**: Banned user tries to count
- **Handling**: Message deleted, DM sent (with cooldown)

### ✅ User Edits Message
- **Case**: User posts "5" then edits to "6"
- **Handling**: `on_message_edit` deletes edited message (anti-cheat)

### ✅ User Deletes Own Message
- **Case**: User posts correct number then deletes it
- **Handling**: Count already updated, next user continues from there

### ✅ Bot User Posts
- **Case**: Another bot posts a number
- **Handling**: Ignored (bot check at start)

### ✅ Webhook Posts
- **Case**: Webhook posts a number
- **Handling**: Ignored (webhook_id check)

## Emoji Edge Cases

### ✅ Custom Emoji Deleted
- **Case**: Custom emoji is deleted after being set
- **Handling**: Fallback to default custom emoji, then unicode ✅

### ✅ Custom Emoji from Another Server
- **Case**: Admin tries to set emoji bot can't access
- **Handling**: Validation fails, error message shown

### ✅ Invalid Emoji Format
- **Case**: Admin enters malformed emoji string
- **Handling**: Validation fails, error message shown

### ✅ Animated Emoji
- **Case**: Admin sets animated emoji
- **Handling**: Properly parsed with `is_animated` flag

## Database Edge Cases

### ✅ MongoDB Connection Lost
- **Case**: MongoDB server goes down
- **Handling**: Operations fail with logged errors, retries enabled

### ✅ Connection Pool Exhausted
- **Case**: Too many concurrent operations
- **Handling**: Semaphore limits to 20 concurrent ops

### ✅ Document Doesn't Exist
- **Case**: First message in a new guild
- **Handling**: `_get_or_create` creates default document

### ✅ Backup Fails
- **Case**: Backup operation errors
- **Handling**: Logged but doesn't affect counting

### ✅ Index Creation Conflict
- **Case**: TTL index exists with different settings
- **Handling**: Drops and recreates index

## Reset/Settings Edge Cases

### ✅ Reset During Active Counting
- **Case**: Admin resets while users are counting
- **Handling**: Lock prevents race, next message starts from 1

### ✅ Set Number to Current
- **Case**: Admin sets number to current count
- **Handling**: Works fine, next number is current + 1

### ✅ Set Number to Negative
- **Case**: Admin tries to set negative number
- **Handling**: Validation rejects with error message

### ✅ Set Number Too Large
- **Case**: Admin tries to set > 1 billion
- **Handling**: Validation rejects with error message

### ✅ Ban User Who Just Counted
- **Case**: Admin bans user immediately after they count
- **Handling**: User's count is preserved, future messages deleted

### ✅ Multiple Settings Changes
- **Case**: Multiple admins change settings simultaneously
- **Handling**: Last one wins (known limitation)

## Milestone Edge Cases

### ✅ Milestone at 100 After Reset
- **Case**: Count reaches 100 again after reset
- **Handling**: Only announces if it's a NEW record (> old record)

### ✅ Milestone Skipped
- **Case**: Count set from 50 to 150
- **Handling**: No announcement (only on actual counting)

### ✅ Multiple Milestones
- **Case**: Count set to 200, then 300
- **Handling**: Each milestone announced only once

## Rate Limit Edge Cases

### ✅ Deletion Rate Limited
- **Case**: Too many deletions too fast
- **Handling**: Queue system with 250ms delay, requeues on 429

### ✅ Reaction Rate Limited
- **Case**: Too many reactions too fast
- **Handling**: Fails silently, doesn't block counting

### ✅ DM Rate Limited
- **Case**: Too many DMs to banned users
- **Handling**: 1 hour cooldown per user

### ✅ Log Channel Spam
- **Case**: Many errors in short time
- **Handling**: Each log is independent, no spam protection (could add)

## Shutdown Edge Cases

### ✅ Cog Unload with Pending Deletions
- **Case**: Bot reloads with 100 messages in queue
- **Handling**: Processes first 50, logs skipped count

### ✅ Bot Shutdown During Count
- **Case**: Bot shuts down while processing message
- **Handling**: Lock released, message may not be processed

### ✅ MongoDB Connection on Unload
- **Case**: Cog unloads with shared connection
- **Handling**: Only closes if it owns the connection

## Memory Leak Prevention

### ✅ DM Sent Cache Growth
- **Case**: Cache grows indefinitely
- **Handling**: Cleanup every 6 hours, removes old entries

### ✅ Lock Cache Growth
- **Case**: Locks for old guilds remain
- **Handling**: Cleanup every hour, removes guilds bot left

### ✅ Deletion Queue Growth
- **Case**: Queue grows faster than processing
- **Handling**: Logged in view command, visible to admins

## Untested/Unhandled Edge Cases

### ⚠️ Unicode Number Characters
- **Case**: User posts "①" (unicode number)
- **Status**: Likely rejected by PURE_INT_RE, but not explicitly tested

### ⚠️ Right-to-Left Numbers
- **Case**: User posts numbers in RTL script
- **Status**: Likely rejected, but not explicitly tested

### ⚠️ Invisible Characters
- **Case**: User posts "5" with invisible unicode characters
- **Status**: `.strip()` may not remove all, could cause issues

### ⚠️ Very Long Number Strings
- **Case**: User posts "1" followed by 1000 zeros
- **Status**: Python int() can handle it, but may be slow

### ⚠️ Spam Reset Attack
- **Case**: User repeatedly posts wrong numbers to reset
- **Status**: No rate limit, could be abused (add cooldown if needed)

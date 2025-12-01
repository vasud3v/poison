# Counting Cog - Bug Fixes

## Critical Bugs Fixed

### 1. Race Condition in Count Reading (CRITICAL)
**Issue**: The `current` count was read from the database BEFORE acquiring the lock, causing race conditions where two messages could read the same count value.

**Fix**: Moved the database read inside the lock to ensure each message gets the most up-to-date count.

**Impact**: This was causing the "Expected 31 but got 30" error in your screenshot.

### 2. Lock Creation Race Condition (CRITICAL)
**Issue**: The lock was checked and created in two separate steps, allowing multiple coroutines to create different lock objects for the same guild.

**Fix**: Used `setdefault()` to atomically create locks.

**Impact**: Could cause multiple messages to process simultaneously, breaking the counting logic.

### 3. Wrong Number Messages Not Deleted
**Issue**: When a user posted the wrong number, the message was not queued for deletion.

**Fix**: Added `self.queue_deletion(message, "wrong_number")` after detecting wrong numbers.

**Impact**: Wrong number messages would stay in the channel, cluttering it.

### 4. Negative/Zero Number Validation Missing
**Issue**: Users could post 0 or negative numbers, breaking the counting logic.

**Fix**: Added validation to reject numbers <= 0.

**Impact**: Could cause database corruption and logic errors.

### 5. No Maximum Number Limit
**Issue**: Users could post extremely large numbers (e.g., 999999999999), potentially causing integer overflow or performance issues.

**Fix**: Added maximum limit of 1 billion for both manual counting and `/count settings set_number`.

**Impact**: Could cause database issues and memory problems.

## Medium Priority Bugs Fixed

### 6. Milestone Announcement Logic Wrong
**Issue**: The bot announced milestones (multiples of 100) every time someone posted them, not just when it was a NEW record.

**Fix**: Changed logic to only announce when `new_record > old_record AND num % 100 == 0`.

**Impact**: Duplicate milestone announcements when counting past 100 multiple times.

### 7. Database Semaphore Not Used in _log()
**Issue**: The `_log()` method queried the database without using the semaphore, potentially exceeding connection limits.

**Fix**: Wrapped the database query in `async with self.db_semaphore`.

**Impact**: Could cause connection pool exhaustion under heavy load.

### 8. User ID Type Mismatch in Leaderboard
**Issue**: MongoDB stores user IDs as strings in the counts dictionary, but Discord mentions require integers.

**Fix**: Added type conversion `int(uid) if isinstance(uid, str) else uid` in both leaderboard displays.

**Impact**: Leaderboard mentions might not work correctly.

## Code Quality Improvements

### 9. Removed Redundant Lock Check
**Issue**: Lock existence was checked twice - once before banned user check and once before acquiring.

**Fix**: Removed the early check and only check/create when needed.

**Impact**: Cleaner code, no functional change.

### 10. Better Error Messages
**Issue**: Generic error messages didn't help users understand what went wrong.

**Fix**: Added specific deletion reasons for debugging (e.g., "non_positive_number", "number_too_large").

**Impact**: Easier debugging and monitoring.

## Additional Edge Cases Fixed (Round 2)

### 11. Database Queries Without Semaphore
**Issue**: Several database queries didn't use the semaphore, risking connection pool exhaustion.

**Fix**: Wrapped all `find_one()` calls with `async with self.db_semaphore`.

**Impact**: Prevents connection pool exhaustion under heavy load.

### 12. Leading Zeros Not Rejected
**Issue**: Users could post "007" instead of "7", which could cause confusion.

**Fix**: Added validation to reject numbers with leading zeros.

**Impact**: Ensures consistent number formatting.

### 13. Deletion Queue Order
**Issue**: Messages were queued for deletion AFTER error handling, so if error handling failed, deletion wouldn't happen.

**Fix**: Moved `queue_deletion()` calls to the beginning of error handlers.

**Impact**: Ensures messages are always deleted even if error handling fails.

### 14. No Cleanup on Guild Remove
**Issue**: When bot is removed from a guild, caches and locks weren't cleaned up.

**Fix**: Added `on_guild_remove` listener to clean up all guild-specific data.

**Impact**: Prevents memory leaks when bot is removed from servers.

### 15. No Handling for Channel Deletion
**Issue**: If the counting channel is deleted, the bot would keep trying to use it.

**Fix**: Added `on_guild_channel_delete` listener to clear the channel setting and notify admins.

**Impact**: Prevents errors and notifies admins to set a new channel.

### 16. Permission Loss Not Logged
**Issue**: If bot loses permissions, it silently fails without notifying admins.

**Fix**: Added hourly logging when permissions are missing.

**Impact**: Admins are notified when permissions need to be fixed.

### 17. Unload Timeout Risk
**Issue**: During cog unload, processing all deletions could timeout.

**Fix**: Limited to 50 deletions during unload and log skipped ones.

**Impact**: Prevents bot shutdown delays.

### 18. Multi-Number Spam Logging
**Issue**: Every multi-number message was logged, causing log spam.

**Fix**: Removed logging for multi-number messages (still deleted).

**Impact**: Cleaner logs.

## Remaining Known Limitations

1. **Settings Command Race Condition**: Multiple admins running `/count settings` simultaneously could overwrite each other's changes. (Low priority - rare occurrence)

2. **Deleted Users in Leaderboard**: Users who left the server still appear in the leaderboard. (By design - preserves history)

3. **No Backup Restore Command**: Backups are created but there's no command to restore from them. (Feature request)

4. **Emoji Validation Timing**: Emoji validation happens during settings change, but if the emoji is deleted later, reactions will fail silently. (Acceptable - has fallback)

5. **No Rate Limit on Wrong Counts**: A user could spam wrong numbers to reset the count repeatedly. (Could add cooldown if needed)

## Testing Recommendations

1. Test rapid counting (2+ users posting within milliseconds)
2. Test with numbers at boundaries (0, 1, 999999999, 1000000000, 1000000001)
3. Test same user posting twice in a row
4. Test wrong numbers (skipping, going backwards)
5. Test with deleted/invalid custom emojis
6. Test ban/unban functionality
7. Test milestone announcements at 100, 200, etc.
8. Test after bot restart (persistence)

## Performance Notes

- Lock-based concurrency control ensures correctness but may slow down under extreme load
- Deletion queue prevents rate limit hits but adds latency to message deletion
- Database semaphore limits concurrent operations to prevent connection exhaustion
- All critical operations are now atomic and race-condition-free

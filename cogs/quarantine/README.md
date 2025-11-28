# Quarantine System

A comprehensive mute/timeout system with appeal functionality and jail channel.

## Features

- **Mute System**: Timeout users with custom durations
- **Jail Channel**: Isolated channel for muted users
- **Appeal System**: Users can submit appeals with reasons
- **Auto-Unmute**: Automatic unmute when duration expires
- **Logging**: Detailed punishment logs
- **Case Tracking**: Numbered case system for moderation
- **DM Notifications**: Automatic DM to muted users
- **Permission Management**: Automatic channel permission overwrites
- **Moderator Roles**: Configurable moderator role system

## Commands

### Setup Commands (Admin)
- `/setup-mute <moderator_role>`: Initial system setup
- `/check-muteperms`: Verify configuration
- `/reset-muteconfig CONFIRM`: Reset configuration
- `/reapply-mute-perms`: Reapply permission overwrites

### Moderation Commands
- `.qmute <user> <duration> [reason]`: Mute a user
- `.qunmute <user> [reason]`: Unmute a user
- `.mutelist`: View all active mutes
- `.clearmutes`: Clear all mutes (admin only)
- `.jailhistory <user>`: View user's jail message history
- `.case <case_id>`: View specific case details
- `.setmodrole <role>`: Set moderator role (admin only)

### Appeal Commands
- `.appeal-status`: Check appeal status
- `.appeal-review <appeal_id> <approve/deny> [reason]`: Review appeals (moderator)
- `.appeal-list`: List pending appeals (moderator)

## Duration Format

- `s` - seconds (e.g., `30s`)
- `m` - minutes (e.g., `10m`)
- `h` - hours (e.g., `2h`)
- `d` - days (e.g., `7d`)

Examples: `10m`, `2h`, `1d`, `30s`

## Components

### Core Files
- `quarantine_system.py`: Main mute system logic
- `appeal_system.py`: Appeal submission and review
- `config.py`: Configuration constants

## Configuration

Requires:
- `MONGO_URL` environment variable
- Manage Guild permission for setup
- Manage Roles permission
- Manage Channels permission (for overwrites)

## Database Collections

- **guild_configs**: Server configurations
- **mutes**: Active and historical mutes
- **jail_messages**: Jail channel message history (7-day TTL)
- **guild_counters**: Case ID tracking
- **pending_dm_deletes**: Scheduled DM deletions
- **appeals**: Appeal submissions and reviews

## Technical Features

- Atomic case ID generation
- Exponential backoff for rate limits
- Per-guild locks for race condition prevention
- TTL indexes for auto-cleanup
- Persistent DM deletion scheduling
- Large server optimization
- Comprehensive error handling
- Role hierarchy validation

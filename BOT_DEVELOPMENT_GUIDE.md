# Multi-Platform Bot Development Guide

A comprehensive guide for building, deploying, and extending a multi-platform bot that works across Discord, Telegram, and Slack.

## Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Architecture](#architecture)
4. [Configuration](#configuration)
5. [Platform Setup](#platform-setup)
6. [Commands](#commands)
7. [Development](#development)
8. [Deployment](#deployment)
9. [Extending the Bot](#extending-the-bot)
10. [Troubleshooting](#troubleshooting)

## Overview

This bot framework provides a unified interface for creating bots that work across multiple chat platforms. It features:

- **Multi-platform support**: Discord, Telegram, and Slack
- **Unified command system**: Write commands once, use everywhere
- **Modular architecture**: Easy to extend and customize
- **Docker deployment**: Simple containerized deployment
- **Configuration management**: Environment-based configuration
- **Structured logging**: Comprehensive logging system

## Quick Start

### Prerequisites

- Python 3.11+
- Docker and Docker Compose (for deployment)
- Bot tokens for desired platforms

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd multi-platform-bot

# Install dependencies
pip install -r bot-app/requirements.txt
```

### 2. Configure Bot Tokens

Create a `.env` file in the bot-app directory:

```bash
# Discord
DISCORD_TOKEN=your_discord_bot_token_here
ENABLE_DISCORD=true

# Telegram
TELEGRAM_TOKEN=your_telegram_bot_token_here
ENABLE_TELEGRAM=true

# Slack
SLACK_TOKEN=your_slack_bot_token_here
SLACK_SIGNING_SECRET=your_slack_signing_secret_here
ENABLE_SLACK=true

# General Settings
COMMAND_PREFIX=!
BOT_NAME=MultiBot
ADMIN_USERS=your_user_id_here
```

### 3. Run the Bot

```bash
# Local development
cd bot-app
python -m main

# Or using Docker
./scripts/deploy.sh deploy
```

## Architecture

### Core Components

```
bot-app/
├── core/
│   └── bot_framework.py      # Core bot framework
├── adapters/
│   ├── discord_adapter.py    # Discord integration
│   ├── telegram_adapter.py   # Telegram integration
│   └── slack_adapter.py      # Slack integration
├── plugins/
│   └── basic_commands.py     # Command implementations
├── config.py                 # Configuration management
└── main.py                   # Application entry point
```

### Key Classes

- **`BotAdapter`**: Abstract base class for platform-specific implementations
- **`BotManager`**: Manages multiple bot adapters
- **`BotMessage`**: Universal message format across platforms
- **`CommandContext`**: Context passed to command handlers
- **`Command`**: Command definition with metadata

## Configuration

Configuration is managed through environment variables and `.env` files:

### Platform Tokens

```bash
# Discord
DISCORD_TOKEN=your_token_here
ENABLE_DISCORD=true

# Telegram  
TELEGRAM_TOKEN=your_token_here
ENABLE_TELEGRAM=true

# Slack
SLACK_TOKEN=your_token_here
SLACK_SIGNING_SECRET=your_secret_here
ENABLE_SLACK=true
```

### Bot Settings

```bash
COMMAND_PREFIX=!                    # Command prefix
BOT_NAME=MultiBot                   # Bot display name
BOT_DESCRIPTION=A versatile bot     # Bot description
ADMIN_USERS=user1,user2             # Admin user IDs
```

### Database & Storage

```bash
DATABASE_URL=sqlite:///bot.db       # Database connection
REDIS_URL=redis://localhost:6379    # Redis for caching
```

### Logging

```bash
LOG_LEVEL=INFO                      # Logging level
LOG_FORMAT=text                     # json or text format
```

## Platform Setup

### Discord Bot Setup

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to "Bot" section and create a bot
4. Copy the bot token
5. Enable necessary intents:
   - Server Members Intent
   - Message Content Intent
6. Generate invite URL with bot permissions

### Telegram Bot Setup

1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Use `/newbot` command
3. Follow instructions to create bot
4. Copy the bot token
5. Configure bot settings:
   - Set description: `/setdescription`
   - Set commands: `/setcommands`

### Slack Bot Setup

1. Go to [Slack API](https://api.slack.com/apps)
2. Create a new app
3. Configure OAuth & Permissions:
   - Add bot token scopes: `chat:write`, `commands`, `app_mentions:read`
4. Install app to workspace
5. Copy Bot User OAuth Token
6. For Socket Mode (recommended):
   - Enable Socket Mode
   - Create App-Level Token with `connections:write` scope

## Commands

### Built-in Commands

| Command | Description | Usage |
|---------|-------------|--------|
| `!ping` | Check bot responsiveness | `!ping` |
| `!help` | Show available commands | `!help [command]` |
| `!info` | Bot information | `!info` |
| `!echo` | Echo message | `!echo <message>` |
| `!roll` | Roll dice | `!roll [sides]` or `!roll [count]d[sides]` |
| `!choose` | Random choice | `!choose option1 option2 ...` |
| `!flip` | Coin flip | `!flip` |
| `!8ball` | Magic 8-ball | `!8ball <question>` |

### Admin Commands

| Command | Description | Usage |
|---------|-------------|--------|
| `!shutdown` | Shutdown bot | `!shutdown` |
| `!eval` | Evaluate Python code | `!eval <code>` |
| `!reload` | Reload configuration | `!reload` |

## Development

### Running Locally

```bash
cd bot-app
python -m main
```

### Creating Custom Commands

```python
from core.bot_framework import BotAdapter, CommandContext

def register_custom_commands(bot: BotAdapter):
    @bot.command(
        name="greet",
        description="Greet a user",
        usage="!greet <name>",
        aliases=["hello", "hi"]
    )
    async def greet_command(ctx: CommandContext):
        if not ctx.args:
            await ctx.reply("Hello! Please provide a name to greet.")
            return
        
        name = " ".join(ctx.args)
        await ctx.reply(f"Hello, {name}! 👋")

    @bot.command(
        name="admin_only",
        description="Admin only command",
        admin_only=True
    )
    async def admin_command(ctx: CommandContext):
        await ctx.reply("This is an admin-only command!")
```

### Adding Event Handlers

```python
@bot.on_event("message")
async def on_message(message):
    # Handle all messages
    pass

@bot.on_event("member_join") 
async def on_member_join(member):
    # Handle new members (Discord)
    pass
```

### Platform-Specific Features

```python
# Discord-specific features
if ctx.message.platform == "discord":
    # Use Discord embeds
    embed = {
        "title": "Hello!",
        "description": "This is an embed",
        "color": 0x00ff00
    }
    await ctx.reply("", embed=embed)

# Telegram-specific features  
elif ctx.message.platform == "telegram":
    # Use Telegram keyboards
    keyboard = {
        "inline_keyboard": [[
            {"text": "Button 1", "callback_data": "btn1"}
        ]]
    }
    await ctx.reply("Choose an option:", reply_markup=keyboard)
```

## Deployment

### Docker Deployment

#### Simple Deployment

```bash
# Deploy with Redis
./scripts/deploy.sh deploy
```

#### Advanced Deployments

```bash
# Deploy with PostgreSQL
./scripts/deploy.sh deploy-postgres

# Deploy with web interface
./scripts/deploy.sh deploy-web

# View logs
./scripts/deploy.sh logs

# Stop bot
./scripts/deploy.sh stop
```

#### Manual Docker Commands

```bash
# Build and run
docker-compose build
docker-compose up -d

# View logs
docker-compose logs -f bot

# Stop
docker-compose down
```

### Production Deployment

#### Environment Variables

Set production environment variables:

```bash
# Security
LOG_FORMAT=json
LOG_LEVEL=INFO

# Database
DATABASE_URL=postgresql://user:pass@db:5432/botdb
REDIS_URL=redis://redis:6379

# Remove development settings
DEBUG=false
```

#### Docker Compose Override

Create `docker-compose.prod.yml`:

```yaml
version: '3.8'
services:
  bot:
    restart: always
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
  
  redis:
    restart: always
    ports: []  # Remove exposed ports
  
  postgres:
    restart: always
    ports: []  # Remove exposed ports
```

Deploy with:

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### Cloud Deployment

#### Docker Hub

```bash
# Build and push
docker build -t your-username/multi-platform-bot .
docker push your-username/multi-platform-bot

# Deploy on server
docker run -d --env-file .env your-username/multi-platform-bot
```

#### Kubernetes

Create `k8s-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: multi-platform-bot
spec:
  replicas: 1
  selector:
    matchLabels:
      app: multi-platform-bot
  template:
    metadata:
      labels:
        app: multi-platform-bot
    spec:
      containers:
      - name: bot
        image: your-username/multi-platform-bot
        envFrom:
        - secretRef:
            name: bot-secrets
```

## Extending the Bot

### Adding New Platforms

1. Create a new adapter in `adapters/` directory:

```python
from core.bot_framework import BotAdapter, BotMessage

class MyPlatformAdapter(BotAdapter):
    def __init__(self):
        super().__init__("myplatform")
    
    async def start(self):
        # Initialize platform connection
        pass
    
    async def send_message(self, channel_id: str, content: str, **kwargs) -> str:
        # Send message implementation
        pass
    
    # Implement other required methods...
```

2. Register the adapter in `main.py`:

```python
if config.is_platform_enabled("myplatform"):
    my_adapter = MyPlatformAdapter()
    register_all_commands(my_adapter)
    self.bot_manager.add_adapter(my_adapter)
```

### Creating Plugin System

```python
# plugins/example_plugin.py
def register_plugin(bot: BotAdapter):
    @bot.command(name="plugin_command")
    async def plugin_cmd(ctx):
        await ctx.reply("Plugin command executed!")

# Load in main.py
from plugins.example_plugin import register_plugin
register_plugin(adapter)
```

### Database Integration

```python
import aiosqlite

class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
    
    async def init_db(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    platform TEXT,
                    user_id TEXT,
                    username TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            await db.commit()
```

### Middleware System

```python
async def logging_middleware(message: BotMessage):
    logger.info("Message received", 
                platform=message.platform,
                user=message.author_name)
    return True  # Continue processing

async def rate_limit_middleware(message: BotMessage):
    # Implement rate limiting
    if is_rate_limited(message.author_id):
        return False  # Block processing
    return True

# Add middleware
bot.add_middleware(logging_middleware)
bot.add_middleware(rate_limit_middleware)
```

## Troubleshooting

### Common Issues

#### Bot Not Responding

1. Check bot tokens are correct
2. Verify platform-specific permissions
3. Check logs for errors: `docker-compose logs bot`

#### Discord Issues

- Ensure Message Content Intent is enabled
- Check bot has required permissions in server
- Verify bot is invited with correct scopes

#### Telegram Issues

- Check bot token format
- Ensure bot is not muted in groups
- Verify webhook URL if using webhooks

#### Slack Issues

- Check OAuth scopes are sufficient
- Verify Socket Mode is enabled (if using)
- Ensure app is installed in workspace

### Debugging

#### Enable Debug Logging

```bash
LOG_LEVEL=DEBUG
```

#### Check Platform Connections

```python
# Add to adapter start() method
self.logger.info("Platform connected", 
                 user_id=self.bot_user_id,
                 platform=self.platform_name)
```

#### Monitor Resource Usage

```bash
# Check container resources
docker stats

# Check logs for memory issues
docker-compose logs bot | grep -i memory
```

### Performance Optimization

#### Redis Caching

```python
import redis.asyncio as redis

class CacheManager:
    def __init__(self, redis_url: str):
        self.redis = redis.from_url(redis_url)
    
    async def get(self, key: str):
        return await self.redis.get(key)
    
    async def set(self, key: str, value: str, expire: int = 3600):
        return await self.redis.setex(key, expire, value)
```

#### Database Connection Pooling

```python
import asyncpg

class PostgresManager:
    def __init__(self, database_url: str):
        self.pool = None
        self.database_url = database_url
    
    async def init_pool(self):
        self.pool = await asyncpg.create_pool(self.database_url)
```

## Security Considerations

### Token Security

- Never commit tokens to version control
- Use environment variables or secret management
- Rotate tokens regularly

### Input Validation

```python
async def safe_eval_command(ctx: CommandContext):
    if not ctx.user.is_admin:
        await ctx.reply("Admin only!")
        return
    
    # Sanitize input
    code = " ".join(ctx.args).strip()
    if any(dangerous in code for dangerous in ['import', '__', 'exec', 'eval']):
        await ctx.reply("Dangerous code detected!")
        return
```

### Rate Limiting

```python
from collections import defaultdict
import time

class RateLimiter:
    def __init__(self, max_requests: int = 10, window: int = 60):
        self.max_requests = max_requests
        self.window = window
        self.requests = defaultdict(list)
    
    def is_allowed(self, user_id: str) -> bool:
        now = time.time()
        user_requests = self.requests[user_id]
        
        # Clean old requests
        user_requests[:] = [req for req in user_requests if now - req < self.window]
        
        if len(user_requests) >= self.max_requests:
            return False
        
        user_requests.append(now)
        return True
```

## Contributing

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Add tests
5. Submit pull request

### Code Style

- Use Black for code formatting
- Follow PEP 8 guidelines
- Add type hints
- Document functions and classes

### Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=bot-app

# Type checking
mypy bot-app/
```

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Support

- Create an issue for bug reports
- Join our Discord server for community support
- Check the troubleshooting section for common issues

---

*Happy bot building! 🤖*
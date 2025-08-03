# Multi-Platform Bot Framework

A comprehensive bot framework that enables you to create bots that work seamlessly across Discord, Telegram, and Slack platforms with a unified command system.

## 🚀 Features

- **Multi-Platform Support**: Deploy to Discord, Telegram, and Slack simultaneously
- **Unified Command System**: Write commands once, use everywhere
- **Modular Architecture**: Easy to extend and customize
- **Docker Ready**: Containerized deployment with Docker Compose
- **Structured Logging**: Comprehensive logging with structured output
- **Configuration Management**: Environment-based configuration
- **Admin System**: Role-based command access
- **Rate Limiting**: Built-in protection against spam
- **Middleware Support**: Extensible message processing pipeline

## 🏗️ Architecture

```
bot-app/
├── core/                     # Core framework
│   └── bot_framework.py      # Abstract bot adapter and command system
├── adapters/                 # Platform-specific implementations
│   ├── discord_adapter.py    # Discord integration
│   ├── telegram_adapter.py   # Telegram integration
│   └── slack_adapter.py      # Slack integration
├── plugins/                  # Command plugins
│   └── basic_commands.py     # Built-in commands
├── scripts/                  # Deployment and utility scripts
│   └── deploy.sh            # Automated deployment script
├── config.py                # Configuration management
├── main.py                  # Application entry point
└── requirements.txt         # Python dependencies
```

## 📦 Quick Start

### Prerequisites

- Python 3.11+
- Docker and Docker Compose (for deployment)
- Bot tokens from your desired platforms

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd multi-platform-bot

# Install dependencies
pip install -r bot-app/requirements.txt
```

### 2. Configuration

Create a `.env` file in the `bot-app` directory:

```bash
# Platform Tokens
DISCORD_TOKEN=your_discord_bot_token
TELEGRAM_TOKEN=your_telegram_bot_token
SLACK_TOKEN=your_slack_bot_token
SLACK_SIGNING_SECRET=your_slack_signing_secret

# Platform Toggles
ENABLE_DISCORD=true
ENABLE_TELEGRAM=true
ENABLE_SLACK=true

# Bot Settings
COMMAND_PREFIX=!
BOT_NAME=MultiBot
ADMIN_USERS=your_user_id_here
```

### 3. Run the Bot

```bash
# Local development
cd bot-app
python -m main

# Docker deployment
./scripts/deploy.sh deploy
```

## 🎮 Built-in Commands

| Command | Description | Usage |
|---------|-------------|--------|
| `!ping` | Check bot responsiveness | `!ping` |
| `!help` | Show available commands | `!help [command]` |
| `!info` | Bot information and stats | `!info` |
| `!echo` | Echo a message | `!echo <message>` |
| `!roll` | Roll dice | `!roll [count]d[sides]` |
| `!choose` | Random choice | `!choose option1 option2 ...` |
| `!flip` | Coin flip | `!flip` |
| `!8ball` | Magic 8-ball responses | `!8ball <question>` |

### Admin Commands
| Command | Description | Usage |
|---------|-------------|--------|
| `!shutdown` | Shutdown the bot | `!shutdown` |
| `!eval` | Execute Python code | `!eval <code>` |
| `!reload` | Reload configuration | `!reload` |

## 🔧 Platform Setup

### Discord
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application and bot
3. Enable Message Content Intent
4. Copy the bot token

### Telegram
1. Message [@BotFather](https://t.me/botfather)
2. Create a new bot with `/newbot`
3. Copy the bot token

### Slack
1. Go to [Slack API](https://api.slack.com/apps)
2. Create a new app
3. Enable Socket Mode and Bot Token Scopes
4. Install to workspace

## 🐳 Docker Deployment

### Simple Deployment
```bash
./scripts/deploy.sh deploy
```

### Advanced Options
```bash
# Deploy with PostgreSQL
./scripts/deploy.sh deploy-postgres

# Deploy with web interface
./scripts/deploy.sh deploy-web

# View logs
./scripts/deploy.sh logs

# Stop the bot
./scripts/deploy.sh stop
```

### Manual Docker
```bash
docker-compose up -d
docker-compose logs -f bot
```

## 🛠️ Development

### Adding Custom Commands

```python
from core.bot_framework import BotAdapter, CommandContext

def register_custom_commands(bot: BotAdapter):
    @bot.command(name="greet", description="Greet someone")
    async def greet_command(ctx: CommandContext):
        name = " ".join(ctx.args) if ctx.args else "World"
        await ctx.reply(f"Hello, {name}! 👋")
```

### Event Handlers

```python
@bot.on_event("message")
async def on_message(message):
    # Handle all messages
    pass

@bot.on_event("member_join")
async def on_member_join(member):
    # Welcome new members
    pass
```

### Platform-Specific Features

```python
# Discord embeds
if ctx.message.platform == "discord":
    embed = {"title": "Hello", "color": 0x00ff00}
    await ctx.reply("", embed=embed)

# Telegram keyboards
elif ctx.message.platform == "telegram":
    keyboard = {"inline_keyboard": [[{"text": "Button", "callback_data": "btn1"}]]}
    await ctx.reply("Choose:", reply_markup=keyboard)
```

## 📚 Documentation

For comprehensive documentation, see [BOT_DEVELOPMENT_GUIDE.md](BOT_DEVELOPMENT_GUIDE.md) which includes:

- Detailed platform setup instructions
- Advanced configuration options
- Plugin development guide
- Deployment strategies
- Troubleshooting guide
- Security considerations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: Report bugs and request features via GitHub Issues
- **Documentation**: Check the comprehensive guide for detailed information
- **Community**: Join our Discord server for community support

## 🎯 Roadmap

- [ ] Web dashboard for bot management
- [ ] Database integration for persistent storage
- [ ] Plugin marketplace
- [ ] Metrics and analytics
- [ ] Auto-scaling support
- [ ] Additional platform support (Matrix, WhatsApp Business)

---

**Built with ❤️ for the multi-platform bot community**

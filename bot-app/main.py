import asyncio
import logging
import signal
import sys
import structlog
from contextlib import asynccontextmanager

from .config import config
from .core.bot_framework import BotManager
from .adapters.discord_adapter import DiscordAdapter
from .adapters.telegram_adapter import TelegramAdapter
from .adapters.slack_adapter import SlackAdapter
from .plugins.basic_commands import register_all_commands


def setup_logging():
    """Set up structured logging"""
    logging.basicConfig(level=getattr(logging, config.log_level.upper()))
    
    if config.log_format == "json":
        structlog.configure(
            processors=[
                structlog.stdlib.filter_by_level,
                structlog.stdlib.add_logger_name,
                structlog.stdlib.add_log_level,
                structlog.stdlib.PositionalArgumentsFormatter(),
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.StackInfoRenderer(),
                structlog.processors.format_exc_info,
                structlog.processors.UnicodeDecoder(),
                structlog.processors.JSONRenderer()
            ],
            context_class=dict,
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True,
        )
    else:
        structlog.configure(
            processors=[
                structlog.stdlib.filter_by_level,
                structlog.stdlib.add_logger_name,
                structlog.stdlib.add_log_level,
                structlog.stdlib.PositionalArgumentsFormatter(),
                structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
                structlog.processors.StackInfoRenderer(),
                structlog.processors.format_exc_info,
                structlog.dev.ConsoleRenderer()
            ],
            context_class=dict,
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True,
        )


class MultiPlatformBot:
    """Main bot application"""
    
    def __init__(self):
        self.bot_manager = BotManager()
        self.logger = structlog.get_logger()
        self.shutdown_event = asyncio.Event()
        
    async def setup(self):
        """Set up bot adapters and commands"""
        # Create and register adapters
        if config.is_platform_enabled("discord"):
            discord_adapter = DiscordAdapter()
            register_all_commands(discord_adapter)
            self.bot_manager.add_adapter(discord_adapter)
        
        if config.is_platform_enabled("telegram"):
            telegram_adapter = TelegramAdapter()
            register_all_commands(telegram_adapter)
            self.bot_manager.add_adapter(telegram_adapter)
        
        if config.is_platform_enabled("slack"):
            slack_adapter = SlackAdapter()
            register_all_commands(slack_adapter)
            self.bot_manager.add_adapter(slack_adapter)
        
        # Set up signal handlers for graceful shutdown
        self._setup_signal_handlers()
        
        self.logger.info("Bot setup complete", platforms=list(self.bot_manager.adapters.keys()))
    
    def _setup_signal_handlers(self):
        """Set up signal handlers for graceful shutdown"""
        def signal_handler(signum, frame):
            self.logger.info("Shutdown signal received", signal=signum)
            self.shutdown_event.set()
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    
    async def run(self):
        """Run the bot"""
        try:
            self.logger.info("Starting multi-platform bot")
            
            # Start all bot adapters
            await self.bot_manager.start_all()
            
            # Wait for shutdown signal
            await self.shutdown_event.wait()
            
        except Exception as e:
            self.logger.error("Error running bot", error=str(e), exc_info=True)
            raise
        finally:
            self.logger.info("Shutting down bot")
            await self.bot_manager.stop_all()
    
    async def start(self):
        """Start the bot with setup"""
        await self.setup()
        await self.run()


async def main():
    """Main entry point"""
    # Set up logging
    setup_logging()
    logger = structlog.get_logger()
    
    # Validate configuration
    if not any([
        config.is_platform_enabled("discord"),
        config.is_platform_enabled("telegram"),
        config.is_platform_enabled("slack")
    ]):
        logger.error("No platforms enabled or configured!")
        sys.exit(1)
    
    # Create and run bot
    bot = MultiPlatformBot()
    
    try:
        await bot.start()
    except KeyboardInterrupt:
        logger.info("Bot interrupted by user")
    except Exception as e:
        logger.error("Bot crashed", error=str(e), exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    # Create .env file if it doesn't exist
    import os
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("""# Bot Configuration
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
BOT_DESCRIPTION=A versatile multi-platform bot

# Admin Settings (comma-separated user IDs)
ADMIN_USERS=your_user_id_here

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=text
""")
        print("Created .env file. Please configure your bot tokens!")
    
    asyncio.run(main())
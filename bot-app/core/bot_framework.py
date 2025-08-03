import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass
from datetime import datetime
import structlog

from ..config import config


@dataclass
class BotMessage:
    """Universal message format across platforms"""
    id: str
    content: str
    author_id: str
    author_name: str
    channel_id: str
    platform: str
    timestamp: datetime
    is_dm: bool = False
    attachments: List[str] = None
    raw_data: Any = None
    
    def __post_init__(self):
        if self.attachments is None:
            self.attachments = []


@dataclass
class BotUser:
    """Universal user format across platforms"""
    id: str
    name: str
    display_name: str
    platform: str
    is_admin: bool = False
    raw_data: Any = None


@dataclass
class CommandContext:
    """Context passed to command handlers"""
    message: BotMessage
    user: BotUser
    args: List[str]
    bot: 'BotAdapter'
    
    async def reply(self, content: str, **kwargs):
        """Reply to the message"""
        return await self.bot.send_message(self.message.channel_id, content, **kwargs)
    
    async def send_dm(self, content: str, **kwargs):
        """Send a direct message to the user"""
        return await self.bot.send_dm(self.user.id, content, **kwargs)


class Command:
    """Command definition"""
    def __init__(
        self,
        name: str,
        handler: Callable,
        description: str = "",
        aliases: List[str] = None,
        admin_only: bool = False,
        usage: str = ""
    ):
        self.name = name
        self.handler = handler
        self.description = description
        self.aliases = aliases or []
        self.admin_only = admin_only
        self.usage = usage


class BotAdapter(ABC):
    """Abstract base class for platform-specific bot adapters"""
    
    def __init__(self, platform_name: str):
        self.platform_name = platform_name
        self.logger = structlog.get_logger(platform=platform_name)
        self.commands: Dict[str, Command] = {}
        self.event_handlers: Dict[str, List[Callable]] = {}
        self.middleware: List[Callable] = []
        
    @abstractmethod
    async def start(self):
        """Start the bot"""
        pass
    
    @abstractmethod
    async def stop(self):
        """Stop the bot"""
        pass
    
    @abstractmethod
    async def send_message(self, channel_id: str, content: str, **kwargs) -> str:
        """Send a message to a channel"""
        pass
    
    @abstractmethod
    async def send_dm(self, user_id: str, content: str, **kwargs) -> str:
        """Send a direct message to a user"""
        pass
    
    @abstractmethod
    async def edit_message(self, channel_id: str, message_id: str, content: str, **kwargs):
        """Edit a message"""
        pass
    
    @abstractmethod
    async def delete_message(self, channel_id: str, message_id: str):
        """Delete a message"""
        pass
    
    def add_command(self, command: Command):
        """Add a command to the bot"""
        self.commands[command.name] = command
        for alias in command.aliases:
            self.commands[alias] = command
        self.logger.info("Command registered", command=command.name, aliases=command.aliases)
    
    def command(
        self,
        name: str = None,
        description: str = "",
        aliases: List[str] = None,
        admin_only: bool = False,
        usage: str = ""
    ):
        """Decorator for registering commands"""
        def decorator(func):
            cmd_name = name or func.__name__
            command = Command(cmd_name, func, description, aliases, admin_only, usage)
            self.add_command(command)
            return func
        return decorator
    
    def on_event(self, event_name: str):
        """Decorator for registering event handlers"""
        def decorator(func):
            if event_name not in self.event_handlers:
                self.event_handlers[event_name] = []
            self.event_handlers[event_name].append(func)
            return func
        return decorator
    
    def add_middleware(self, middleware: Callable):
        """Add middleware function"""
        self.middleware.append(middleware)
    
    async def process_message(self, message: BotMessage):
        """Process an incoming message"""
        # Apply middleware
        for middleware in self.middleware:
            result = await middleware(message)
            if result is False:  # Middleware can block processing
                return
        
        # Check if it's a command
        if message.content.startswith(config.command_prefix):
            await self._handle_command(message)
        
        # Trigger message event handlers
        await self._trigger_event("message", message)
    
    async def _handle_command(self, message: BotMessage):
        """Handle command execution"""
        content = message.content[len(config.command_prefix):].strip()
        if not content:
            return
        
        parts = content.split()
        command_name = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        if command_name not in self.commands:
            return
        
        command = self.commands[command_name]
        
        # Create user object
        user = BotUser(
            id=message.author_id,
            name=message.author_name,
            display_name=message.author_name,
            platform=self.platform_name,
            is_admin=message.author_id in config.admin_users
        )
        
        # Check admin requirement
        if command.admin_only and not user.is_admin:
            await self.send_message(
                message.channel_id,
                "❌ This command requires administrator privileges."
            )
            return
        
        # Create context and execute command
        context = CommandContext(message, user, args, self)
        
        try:
            await command.handler(context)
            self.logger.info(
                "Command executed",
                command=command_name,
                user=user.name,
                args=args
            )
        except Exception as e:
            self.logger.error(
                "Command execution failed",
                command=command_name,
                error=str(e),
                exc_info=True
            )
            await self.send_message(
                message.channel_id,
                f"❌ Command failed: {str(e)}"
            )
    
    async def _trigger_event(self, event_name: str, *args, **kwargs):
        """Trigger event handlers"""
        if event_name in self.event_handlers:
            for handler in self.event_handlers[event_name]:
                try:
                    await handler(*args, **kwargs)
                except Exception as e:
                    self.logger.error(
                        "Event handler failed",
                        event=event_name,
                        error=str(e),
                        exc_info=True
                    )


class BotManager:
    """Manages multiple bot adapters"""
    
    def __init__(self):
        self.adapters: Dict[str, BotAdapter] = {}
        self.logger = structlog.get_logger()
    
    def add_adapter(self, adapter: BotAdapter):
        """Add a bot adapter"""
        self.adapters[adapter.platform_name] = adapter
        self.logger.info("Bot adapter added", platform=adapter.platform_name)
    
    async def start_all(self):
        """Start all bot adapters"""
        tasks = []
        for platform, adapter in self.adapters.items():
            if config.is_platform_enabled(platform):
                tasks.append(adapter.start())
                self.logger.info("Starting bot adapter", platform=platform)
            else:
                self.logger.info("Skipping disabled platform", platform=platform)
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
    
    async def stop_all(self):
        """Stop all bot adapters"""
        tasks = []
        for adapter in self.adapters.values():
            tasks.append(adapter.stop())
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
    
    def get_adapter(self, platform: str) -> Optional[BotAdapter]:
        """Get a specific adapter"""
        return self.adapters.get(platform)
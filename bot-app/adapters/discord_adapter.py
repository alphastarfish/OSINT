import discord
from discord.ext import commands
from datetime import datetime
from typing import Optional

from ..core.bot_framework import BotAdapter, BotMessage, BotUser
from ..config import config


class DiscordAdapter(BotAdapter):
    """Discord bot adapter"""
    
    def __init__(self):
        super().__init__("discord")
        
        # Set up intents
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        intents.members = True
        
        self.client = commands.Bot(
            command_prefix=config.command_prefix,
            intents=intents,
            help_command=None  # We'll implement our own help
        )
        
        # Set up event handlers
        self._setup_events()
    
    def _setup_events(self):
        """Set up Discord event handlers"""
        
        @self.client.event
        async def on_ready():
            self.logger.info("Discord bot connected", user=self.client.user.name)
            await self._trigger_event("ready")
        
        @self.client.event
        async def on_message(message):
            # Ignore bot messages
            if message.author.bot:
                return
            
            # Convert to universal message format
            bot_message = self._convert_message(message)
            await self.process_message(bot_message)
        
        @self.client.event
        async def on_guild_join(guild):
            self.logger.info("Joined guild", guild=guild.name, id=guild.id)
            await self._trigger_event("guild_join", guild)
        
        @self.client.event
        async def on_guild_remove(guild):
            self.logger.info("Left guild", guild=guild.name, id=guild.id)
            await self._trigger_event("guild_leave", guild)
        
        @self.client.event
        async def on_member_join(member):
            await self._trigger_event("member_join", member)
        
        @self.client.event
        async def on_member_remove(member):
            await self._trigger_event("member_leave", member)
    
    def _convert_message(self, message: discord.Message) -> BotMessage:
        """Convert Discord message to universal format"""
        return BotMessage(
            id=str(message.id),
            content=message.content,
            author_id=str(message.author.id),
            author_name=message.author.display_name,
            channel_id=str(message.channel.id),
            platform="discord",
            timestamp=message.created_at,
            is_dm=isinstance(message.channel, discord.DMChannel),
            attachments=[attachment.url for attachment in message.attachments],
            raw_data=message
        )
    
    async def start(self):
        """Start the Discord bot"""
        if not config.discord_token:
            self.logger.error("Discord token not provided")
            return
        
        try:
            await self.client.start(config.discord_token)
        except Exception as e:
            self.logger.error("Failed to start Discord bot", error=str(e))
            raise
    
    async def stop(self):
        """Stop the Discord bot"""
        if self.client:
            await self.client.close()
    
    async def send_message(self, channel_id: str, content: str, **kwargs) -> str:
        """Send a message to a Discord channel"""
        try:
            channel = self.client.get_channel(int(channel_id))
            if not channel:
                # Try to fetch the channel
                channel = await self.client.fetch_channel(int(channel_id))
            
            # Handle embeds
            embed = kwargs.get('embed')
            if embed and isinstance(embed, dict):
                embed = discord.Embed(**embed)
            
            message = await channel.send(
                content=content,
                embed=embed,
                file=kwargs.get('file'),
                files=kwargs.get('files')
            )
            return str(message.id)
        
        except Exception as e:
            self.logger.error("Failed to send message", error=str(e), channel_id=channel_id)
            raise
    
    async def send_dm(self, user_id: str, content: str, **kwargs) -> str:
        """Send a direct message to a Discord user"""
        try:
            user = self.client.get_user(int(user_id))
            if not user:
                user = await self.client.fetch_user(int(user_id))
            
            embed = kwargs.get('embed')
            if embed and isinstance(embed, dict):
                embed = discord.Embed(**embed)
            
            message = await user.send(
                content=content,
                embed=embed,
                file=kwargs.get('file'),
                files=kwargs.get('files')
            )
            return str(message.id)
        
        except Exception as e:
            self.logger.error("Failed to send DM", error=str(e), user_id=user_id)
            raise
    
    async def edit_message(self, channel_id: str, message_id: str, content: str, **kwargs):
        """Edit a Discord message"""
        try:
            channel = self.client.get_channel(int(channel_id))
            if not channel:
                channel = await self.client.fetch_channel(int(channel_id))
            
            message = await channel.fetch_message(int(message_id))
            
            embed = kwargs.get('embed')
            if embed and isinstance(embed, dict):
                embed = discord.Embed(**embed)
            
            await message.edit(content=content, embed=embed)
        
        except Exception as e:
            self.logger.error("Failed to edit message", error=str(e), message_id=message_id)
            raise
    
    async def delete_message(self, channel_id: str, message_id: str):
        """Delete a Discord message"""
        try:
            channel = self.client.get_channel(int(channel_id))
            if not channel:
                channel = await self.client.fetch_channel(int(channel_id))
            
            message = await channel.fetch_message(int(message_id))
            await message.delete()
        
        except Exception as e:
            self.logger.error("Failed to delete message", error=str(e), message_id=message_id)
            raise
    
    async def add_reaction(self, channel_id: str, message_id: str, emoji: str):
        """Add a reaction to a Discord message"""
        try:
            channel = self.client.get_channel(int(channel_id))
            if not channel:
                channel = await self.client.fetch_channel(int(channel_id))
            
            message = await channel.fetch_message(int(message_id))
            await message.add_reaction(emoji)
        
        except Exception as e:
            self.logger.error("Failed to add reaction", error=str(e), emoji=emoji)
    
    def get_guild(self, guild_id: str) -> Optional[discord.Guild]:
        """Get a Discord guild by ID"""
        return self.client.get_guild(int(guild_id))
    
    def get_user(self, user_id: str) -> Optional[discord.User]:
        """Get a Discord user by ID"""
        return self.client.get_user(int(user_id))
    
    def get_channel(self, channel_id: str) -> Optional[discord.abc.GuildChannel]:
        """Get a Discord channel by ID"""
        return self.client.get_channel(int(channel_id))
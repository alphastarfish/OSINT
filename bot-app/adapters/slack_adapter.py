import asyncio
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.socket_mode.async_client import AsyncSocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.socket_mode.response import SocketModeResponse
from datetime import datetime
from typing import Optional

from ..core.bot_framework import BotAdapter, BotMessage, BotUser
from ..config import config


class SlackAdapter(BotAdapter):
    """Slack bot adapter"""
    
    def __init__(self):
        super().__init__("slack")
        self.web_client = None
        self.socket_client = None
    
    async def start(self):
        """Start the Slack bot"""
        if not config.slack_token:
            self.logger.error("Slack token not provided")
            return
        
        try:
            # Initialize clients
            self.web_client = AsyncWebClient(token=config.slack_token)
            
            # Test the connection
            auth_response = await self.web_client.auth_test()
            bot_user_id = auth_response["user_id"]
            
            self.logger.info("Slack bot authenticated", user_id=bot_user_id)
            
            # Set up Socket Mode if app token is available
            if config.slack_signing_secret:
                self.socket_client = AsyncSocketModeClient(
                    app_token=config.slack_signing_secret,
                    web_client=self.web_client
                )
                
                # Set up event handlers
                self._setup_socket_handlers()
                
                # Start socket mode
                await self.socket_client.connect()
            
            await self._trigger_event("ready")
            
        except Exception as e:
            self.logger.error("Failed to start Slack bot", error=str(e))
            raise
    
    async def stop(self):
        """Stop the Slack bot"""
        if self.socket_client:
            await self.socket_client.disconnect()
    
    def _setup_socket_handlers(self):
        """Set up Slack Socket Mode event handlers"""
        
        @self.socket_client.socket_mode_request_listeners.append
        async def handle_socket_mode_request(client: AsyncSocketModeClient, req: SocketModeRequest):
            if req.type == "events_api":
                # Handle Events API
                event = req.payload.get("event", {})
                
                if event.get("type") == "message" and not event.get("subtype"):
                    # Convert to universal message format
                    bot_message = self._convert_message(event)
                    if bot_message:
                        await self.process_message(bot_message)
                
                # Acknowledge the request
                response = SocketModeResponse(envelope_id=req.envelope_id)
                await client.send_socket_mode_response(response)
            
            elif req.type == "slash_commands":
                # Handle slash commands
                command = req.payload
                
                # Convert slash command to our command format
                content = f"{config.command_prefix}{command['command'][1:]} {command.get('text', '')}"
                
                bot_message = BotMessage(
                    id=f"slash_{command['trigger_id']}",
                    content=content.strip(),
                    author_id=command['user_id'],
                    author_name=command['user_name'],
                    channel_id=command['channel_id'],
                    platform="slack",
                    timestamp=datetime.now(),
                    is_dm=command['channel_name'] == "directmessage",
                    raw_data=command
                )
                
                await self.process_message(bot_message)
                
                # Acknowledge the request
                response = SocketModeResponse(envelope_id=req.envelope_id)
                await client.send_socket_mode_response(response)
    
    def _convert_message(self, event) -> Optional[BotMessage]:
        """Convert Slack message event to universal format"""
        # Skip bot messages
        if event.get("bot_id") or event.get("subtype"):
            return None
        
        # Get message content
        content = event.get("text", "")
        
        # Handle mentions and convert them
        if content.startswith(f"<@{event.get('bot_id', '')}>"):
            # Remove bot mention and treat as command
            content = config.command_prefix + content.split(">", 1)[1].strip()
        
        return BotMessage(
            id=event.get("ts", ""),
            content=content,
            author_id=event.get("user", ""),
            author_name="Unknown",  # We'll fetch this separately if needed
            channel_id=event.get("channel", ""),
            platform="slack",
            timestamp=datetime.fromtimestamp(float(event.get("ts", 0))),
            is_dm=event.get("channel_type") == "im",
            attachments=[],  # TODO: Handle file attachments
            raw_data=event
        )
    
    async def send_message(self, channel_id: str, content: str, **kwargs) -> str:
        """Send a message to a Slack channel"""
        try:
            # Handle blocks (rich formatting)
            blocks = kwargs.get('blocks')
            attachments = kwargs.get('attachments')
            
            response = await self.web_client.chat_postMessage(
                channel=channel_id,
                text=content,
                blocks=blocks,
                attachments=attachments,
                thread_ts=kwargs.get('thread_ts'),
                reply_broadcast=kwargs.get('reply_broadcast', False)
            )
            
            return response["ts"]
        
        except Exception as e:
            self.logger.error("Failed to send message", error=str(e), channel_id=channel_id)
            raise
    
    async def send_dm(self, user_id: str, content: str, **kwargs) -> str:
        """Send a direct message to a Slack user"""
        try:
            # Open DM channel
            response = await self.web_client.conversations_open(users=[user_id])
            channel_id = response["channel"]["id"]
            
            # Send message to DM channel
            return await self.send_message(channel_id, content, **kwargs)
        
        except Exception as e:
            self.logger.error("Failed to send DM", error=str(e), user_id=user_id)
            raise
    
    async def edit_message(self, channel_id: str, message_id: str, content: str, **kwargs):
        """Edit a Slack message"""
        try:
            blocks = kwargs.get('blocks')
            attachments = kwargs.get('attachments')
            
            await self.web_client.chat_update(
                channel=channel_id,
                ts=message_id,
                text=content,
                blocks=blocks,
                attachments=attachments
            )
        
        except Exception as e:
            self.logger.error("Failed to edit message", error=str(e), message_id=message_id)
            raise
    
    async def delete_message(self, channel_id: str, message_id: str):
        """Delete a Slack message"""
        try:
            await self.web_client.chat_delete(
                channel=channel_id,
                ts=message_id
            )
        
        except Exception as e:
            self.logger.error("Failed to delete message", error=str(e), message_id=message_id)
            raise
    
    async def add_reaction(self, channel_id: str, message_id: str, emoji: str):
        """Add a reaction to a Slack message"""
        try:
            # Remove colons from emoji if present
            emoji = emoji.strip(':')
            
            await self.web_client.reactions_add(
                channel=channel_id,
                timestamp=message_id,
                name=emoji
            )
        
        except Exception as e:
            self.logger.error("Failed to add reaction", error=str(e), emoji=emoji)
    
    async def upload_file(self, channel_id: str, file_path: str, title: str = "", comment: str = ""):
        """Upload a file to Slack"""
        try:
            response = await self.web_client.files_upload(
                channels=channel_id,
                file=file_path,
                title=title,
                initial_comment=comment
            )
            return response["file"]["id"]
        
        except Exception as e:
            self.logger.error("Failed to upload file", error=str(e))
            raise
    
    async def get_user_info(self, user_id: str):
        """Get user information"""
        try:
            response = await self.web_client.users_info(user=user_id)
            return response["user"]
        except Exception as e:
            self.logger.error("Failed to get user info", error=str(e), user_id=user_id)
            return None
    
    async def get_channel_info(self, channel_id: str):
        """Get channel information"""
        try:
            response = await self.web_client.conversations_info(channel=channel_id)
            return response["channel"]
        except Exception as e:
            self.logger.error("Failed to get channel info", error=str(e), channel_id=channel_id)
            return None
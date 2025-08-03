from telegram import Update, Bot
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from datetime import datetime
from typing import Optional

from ..core.bot_framework import BotAdapter, BotMessage, BotUser
from ..config import config


class TelegramAdapter(BotAdapter):
    """Telegram bot adapter"""
    
    def __init__(self):
        super().__init__("telegram")
        self.application = None
        self.bot = None
    
    async def start(self):
        """Start the Telegram bot"""
        if not config.telegram_token:
            self.logger.error("Telegram token not provided")
            return
        
        try:
            # Create application
            self.application = Application.builder().token(config.telegram_token).build()
            self.bot = self.application.bot
            
            # Set up handlers
            self._setup_handlers()
            
            # Start the bot
            await self.application.initialize()
            await self.application.start()
            await self.application.updater.start_polling()
            
            self.logger.info("Telegram bot started")
            await self._trigger_event("ready")
            
        except Exception as e:
            self.logger.error("Failed to start Telegram bot", error=str(e))
            raise
    
    async def stop(self):
        """Stop the Telegram bot"""
        if self.application:
            await self.application.updater.stop()
            await self.application.stop()
            await self.application.shutdown()
    
    def _setup_handlers(self):
        """Set up Telegram message handlers"""
        
        async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
            if update.message:
                # Convert to universal message format
                bot_message = self._convert_message(update.message)
                await self.process_message(bot_message)
        
        # Add message handler
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
        )
        
        # Add command handler (for messages starting with /)
        self.application.add_handler(
            MessageHandler(filters.COMMAND, handle_message)
        )
    
    def _convert_message(self, message) -> BotMessage:
        """Convert Telegram message to universal format"""
        # Handle different message types
        content = ""
        attachments = []
        
        if message.text:
            content = message.text
        elif message.caption:
            content = message.caption
        
        if message.photo:
            # Get the largest photo
            largest_photo = max(message.photo, key=lambda x: x.file_size or 0)
            attachments.append(f"photo:{largest_photo.file_id}")
        
        if message.document:
            attachments.append(f"document:{message.document.file_id}")
        
        if message.video:
            attachments.append(f"video:{message.video.file_id}")
        
        if message.audio:
            attachments.append(f"audio:{message.audio.file_id}")
        
        # Convert Telegram command format to our format
        if content.startswith('/'):
            content = config.command_prefix + content[1:]
        
        return BotMessage(
            id=str(message.message_id),
            content=content,
            author_id=str(message.from_user.id),
            author_name=message.from_user.first_name or "Unknown",
            channel_id=str(message.chat.id),
            platform="telegram",
            timestamp=message.date,
            is_dm=message.chat.type == "private",
            attachments=attachments,
            raw_data=message
        )
    
    async def send_message(self, channel_id: str, content: str, **kwargs) -> str:
        """Send a message to a Telegram chat"""
        try:
            # Handle markdown formatting
            parse_mode = kwargs.get('parse_mode', 'Markdown')
            
            message = await self.bot.send_message(
                chat_id=int(channel_id),
                text=content,
                parse_mode=parse_mode,
                reply_markup=kwargs.get('reply_markup')
            )
            return str(message.message_id)
        
        except Exception as e:
            self.logger.error("Failed to send message", error=str(e), channel_id=channel_id)
            raise
    
    async def send_dm(self, user_id: str, content: str, **kwargs) -> str:
        """Send a direct message to a Telegram user"""
        # In Telegram, DM is just sending to the user's chat
        return await self.send_message(user_id, content, **kwargs)
    
    async def edit_message(self, channel_id: str, message_id: str, content: str, **kwargs):
        """Edit a Telegram message"""
        try:
            parse_mode = kwargs.get('parse_mode', 'Markdown')
            
            await self.bot.edit_message_text(
                chat_id=int(channel_id),
                message_id=int(message_id),
                text=content,
                parse_mode=parse_mode,
                reply_markup=kwargs.get('reply_markup')
            )
        
        except Exception as e:
            self.logger.error("Failed to edit message", error=str(e), message_id=message_id)
            raise
    
    async def delete_message(self, channel_id: str, message_id: str):
        """Delete a Telegram message"""
        try:
            await self.bot.delete_message(
                chat_id=int(channel_id),
                message_id=int(message_id)
            )
        
        except Exception as e:
            self.logger.error("Failed to delete message", error=str(e), message_id=message_id)
            raise
    
    async def send_photo(self, channel_id: str, photo, caption: str = "", **kwargs) -> str:
        """Send a photo to a Telegram chat"""
        try:
            message = await self.bot.send_photo(
                chat_id=int(channel_id),
                photo=photo,
                caption=caption,
                parse_mode=kwargs.get('parse_mode', 'Markdown')
            )
            return str(message.message_id)
        
        except Exception as e:
            self.logger.error("Failed to send photo", error=str(e))
            raise
    
    async def send_document(self, channel_id: str, document, caption: str = "", **kwargs) -> str:
        """Send a document to a Telegram chat"""
        try:
            message = await self.bot.send_document(
                chat_id=int(channel_id),
                document=document,
                caption=caption,
                parse_mode=kwargs.get('parse_mode', 'Markdown')
            )
            return str(message.message_id)
        
        except Exception as e:
            self.logger.error("Failed to send document", error=str(e))
            raise
    
    async def get_chat(self, chat_id: str):
        """Get chat information"""
        try:
            return await self.bot.get_chat(int(chat_id))
        except Exception as e:
            self.logger.error("Failed to get chat", error=str(e), chat_id=chat_id)
            return None
    
    async def get_chat_member(self, chat_id: str, user_id: str):
        """Get chat member information"""
        try:
            return await self.bot.get_chat_member(int(chat_id), int(user_id))
        except Exception as e:
            self.logger.error("Failed to get chat member", error=str(e))
            return None
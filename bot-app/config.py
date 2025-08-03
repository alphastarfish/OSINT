import os
from typing import Optional, List
from pydantic import BaseSettings, Field
from pydantic_settings import SettingsConfigDict


class BotConfig(BaseSettings):
    """Bot configuration using environment variables and .env file"""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )
    
    # Bot platform tokens
    discord_token: Optional[str] = Field(None, description="Discord bot token")
    telegram_token: Optional[str] = Field(None, description="Telegram bot token")
    slack_token: Optional[str] = Field(None, description="Slack bot token")
    slack_signing_secret: Optional[str] = Field(None, description="Slack signing secret")
    
    # Database configuration
    database_url: str = Field("sqlite:///bot.db", description="Database connection URL")
    redis_url: Optional[str] = Field("redis://localhost:6379", description="Redis URL for caching")
    
    # Bot settings
    command_prefix: str = Field("!", description="Command prefix for bots")
    bot_name: str = Field("MultiBot", description="Bot display name")
    bot_description: str = Field("A versatile multi-platform bot", description="Bot description")
    
    # API settings
    api_host: str = Field("0.0.0.0", description="API server host")
    api_port: int = Field(8000, description="API server port")
    webhook_url: Optional[str] = Field(None, description="Webhook URL for platforms")
    
    # Feature flags
    enable_discord: bool = Field(True, description="Enable Discord integration")
    enable_telegram: bool = Field(True, description="Enable Telegram integration")
    enable_slack: bool = Field(True, description="Enable Slack integration")
    enable_web_interface: bool = Field(True, description="Enable web interface")
    
    # Admin settings
    admin_users: List[str] = Field(default_factory=list, description="List of admin user IDs")
    allowed_guilds: List[str] = Field(default_factory=list, description="List of allowed Discord guild IDs")
    
    # Logging
    log_level: str = Field("INFO", description="Logging level")
    log_format: str = Field("json", description="Logging format (json or text)")
    
    # Rate limiting
    rate_limit_requests: int = Field(60, description="Rate limit requests per minute")
    rate_limit_window: int = Field(60, description="Rate limit window in seconds")
    
    def is_platform_enabled(self, platform: str) -> bool:
        """Check if a specific platform is enabled and configured"""
        platform_map = {
            "discord": (self.enable_discord, self.discord_token),
            "telegram": (self.enable_telegram, self.telegram_token),
            "slack": (self.enable_slack, self.slack_token)
        }
        
        if platform not in platform_map:
            return False
            
        enabled, token = platform_map[platform]
        return enabled and token is not None


# Global config instance
config = BotConfig()
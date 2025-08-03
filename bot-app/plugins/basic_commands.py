import asyncio
import time
import random
from datetime import datetime
from typing import List

from ..core.bot_framework import BotAdapter, CommandContext


def register_basic_commands(bot: BotAdapter):
    """Register basic commands for the bot"""
    
    @bot.command(
        name="ping",
        description="Check if the bot is responding",
        aliases=["p"]
    )
    async def ping_command(ctx: CommandContext):
        """Simple ping command"""
        start_time = time.time()
        message_id = await ctx.reply("🏓 Pong!")
        end_time = time.time()
        
        # Calculate latency
        latency = (end_time - start_time) * 1000
        
        # Edit the message with latency info
        await ctx.bot.edit_message(
            ctx.message.channel_id,
            message_id,
            f"🏓 Pong! Latency: {latency:.2f}ms"
        )
    
    @bot.command(
        name="echo",
        description="Echo back the provided message",
        usage="!echo <message>"
    )
    async def echo_command(ctx: CommandContext):
        """Echo command"""
        if not ctx.args:
            await ctx.reply("❌ Please provide a message to echo!")
            return
        
        message = " ".join(ctx.args)
        await ctx.reply(f"📢 {message}")
    
    @bot.command(
        name="help",
        description="Show available commands",
        aliases=["h", "commands"]
    )
    async def help_command(ctx: CommandContext):
        """Help command"""
        if ctx.args:
            # Show help for specific command
            command_name = ctx.args[0].lower()
            if command_name in ctx.bot.commands:
                command = ctx.bot.commands[command_name]
                help_text = f"**{command.name}**\n"
                help_text += f"Description: {command.description or 'No description'}\n"
                if command.usage:
                    help_text += f"Usage: {command.usage}\n"
                if command.aliases:
                    help_text += f"Aliases: {', '.join(command.aliases)}\n"
                if command.admin_only:
                    help_text += "⚠️ Admin only command\n"
                
                await ctx.reply(help_text)
            else:
                await ctx.reply(f"❌ Command '{command_name}' not found!")
        else:
            # Show all commands
            commands = {}
            for cmd in ctx.bot.commands.values():
                if cmd.name not in commands:  # Avoid duplicates from aliases
                    commands[cmd.name] = cmd
            
            help_text = f"**Available Commands** (Prefix: `{ctx.bot.commands['help'].name[0] if ctx.bot.commands else '!'}`)\n\n"
            
            for cmd in sorted(commands.values(), key=lambda x: x.name):
                help_text += f"• **{cmd.name}** - {cmd.description or 'No description'}\n"
            
            help_text += f"\nUse `!help <command>` for detailed information about a specific command."
            
            await ctx.reply(help_text)
    
    @bot.command(
        name="info",
        description="Show bot information and stats",
        aliases=["about", "status"]
    )
    async def info_command(ctx: CommandContext):
        """Bot info command"""
        info_text = f"🤖 **Bot Information**\n\n"
        info_text += f"Platform: {ctx.message.platform.title()}\n"
        info_text += f"Commands loaded: {len(set(cmd.name for cmd in ctx.bot.commands.values()))}\n"
        info_text += f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n"
        
        await ctx.reply(info_text)
    
    @bot.command(
        name="roll",
        description="Roll dice",
        usage="!roll [sides] or !roll [count]d[sides]",
        aliases=["dice", "d"]
    )
    async def roll_command(ctx: CommandContext):
        """Dice rolling command"""
        if not ctx.args:
            # Default: roll 1d6
            result = random.randint(1, 6)
            await ctx.reply(f"🎲 You rolled: **{result}**")
            return
        
        dice_str = ctx.args[0]
        
        try:
            if 'd' in dice_str.lower():
                # Format: XdY (e.g., 2d20)
                count, sides = dice_str.lower().split('d')
                count = int(count) if count else 1
                sides = int(sides)
                
                if count > 20:
                    await ctx.reply("❌ Maximum 20 dice allowed!")
                    return
                
                if sides > 1000:
                    await ctx.reply("❌ Maximum 1000 sides allowed!")
                    return
                
                results = [random.randint(1, sides) for _ in range(count)]
                total = sum(results)
                
                if count == 1:
                    await ctx.reply(f"🎲 You rolled 1d{sides}: **{results[0]}**")
                else:
                    result_str = " + ".join(map(str, results))
                    await ctx.reply(f"🎲 You rolled {count}d{sides}: {result_str} = **{total}**")
            
            else:
                # Single number: sides of die
                sides = int(dice_str)
                if sides > 1000:
                    await ctx.reply("❌ Maximum 1000 sides allowed!")
                    return
                
                result = random.randint(1, sides)
                await ctx.reply(f"🎲 You rolled 1d{sides}: **{result}**")
        
        except ValueError:
            await ctx.reply("❌ Invalid dice format! Use `!roll 6` or `!roll 2d20`")
    
    @bot.command(
        name="choose",
        description="Choose randomly from a list of options",
        usage="!choose option1 option2 option3...",
        aliases=["pick", "select"]
    )
    async def choose_command(ctx: CommandContext):
        """Random choice command"""
        if len(ctx.args) < 2:
            await ctx.reply("❌ Please provide at least 2 options to choose from!")
            return
        
        choice = random.choice(ctx.args)
        await ctx.reply(f"🤔 I choose: **{choice}**")
    
    @bot.command(
        name="flip",
        description="Flip a coin",
        aliases=["coin", "coinflip"]
    )
    async def flip_command(ctx: CommandContext):
        """Coin flip command"""
        result = random.choice(["Heads", "Tails"])
        emoji = "🪙" if result == "Heads" else "🔄"
        await ctx.reply(f"{emoji} **{result}**!")
    
    @bot.command(
        name="8ball",
        description="Ask the magic 8-ball a question",
        usage="!8ball <question>",
        aliases=["eightball", "ball"]
    )
    async def eightball_command(ctx: CommandContext):
        """Magic 8-ball command"""
        if not ctx.args:
            await ctx.reply("❌ Please ask a question!")
            return
        
        responses = [
            "It is certain", "It is decidedly so", "Without a doubt",
            "Yes definitely", "You may rely on it", "As I see it, yes",
            "Most likely", "Outlook good", "Yes", "Signs point to yes",
            "Reply hazy, try again", "Ask again later", "Better not tell you now",
            "Cannot predict now", "Concentrate and ask again",
            "Don't count on it", "My reply is no", "My sources say no",
            "Outlook not so good", "Very doubtful"
        ]
        
        response = random.choice(responses)
        await ctx.reply(f"🎱 {response}")
    
    @bot.command(
        name="uptime",
        description="Show how long the bot has been running"
    )
    async def uptime_command(ctx: CommandContext):
        """Uptime command"""
        # This is a simple implementation - in a real bot you'd track start time
        await ctx.reply("🕐 Bot uptime tracking is not implemented yet!")
    
    @bot.command(
        name="version",
        description="Show bot version"
    )
    async def version_command(ctx: CommandContext):
        """Version command"""
        await ctx.reply("🔖 Bot Framework v1.0.0")


# Admin commands
def register_admin_commands(bot: BotAdapter):
    """Register admin-only commands"""
    
    @bot.command(
        name="shutdown",
        description="Shutdown the bot (admin only)",
        admin_only=True
    )
    async def shutdown_command(ctx: CommandContext):
        """Shutdown command"""
        await ctx.reply("🔌 Shutting down bot...")
        # In a real implementation, you'd properly shutdown the bot
        # await ctx.bot.stop()
    
    @bot.command(
        name="eval",
        description="Evaluate Python code (admin only)",
        admin_only=True,
        usage="!eval <code>"
    )
    async def eval_command(ctx: CommandContext):
        """Eval command - dangerous, admin only"""
        if not ctx.args:
            await ctx.reply("❌ Please provide code to evaluate!")
            return
        
        code = " ".join(ctx.args)
        
        try:
            # This is dangerous and should be used carefully
            result = eval(code)
            await ctx.reply(f"```python\n{result}\n```")
        except Exception as e:
            await ctx.reply(f"❌ Error: {str(e)}")
    
    @bot.command(
        name="reload",
        description="Reload bot configuration (admin only)",
        admin_only=True
    )
    async def reload_command(ctx: CommandContext):
        """Reload command"""
        await ctx.reply("🔄 Configuration reload is not implemented yet!")


def register_all_commands(bot: BotAdapter):
    """Register all commands for the bot"""
    register_basic_commands(bot)
    register_admin_commands(bot)
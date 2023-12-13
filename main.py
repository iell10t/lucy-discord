from config import discordConfig
from bot import discordBotManager
import asyncio

# Load token for Discord bot 
TOKEN = discordConfig.DISCORD_BOT_TOKEN
CHANNEL_ID = discordConfig.DISCORD_CHANNEL_ID

# Run Discord Bot (discord.Client.start)
def main():
    bot = discordBotManager.BotClient(TOKEN, CHANNEL_ID)
    asyncio.run(bot.start_bot())

if __name__ == "__main__":
    main()

import discord

class BotClient(discord.Client):
    def __init__(self, token, channel_id):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.token = token
        self.channel_id = channel_id

    # This function is a coroutine. A shorthand coroutine for login() + connect().
    async def start_bot(self):
        await self.start(self.token)

    # Called when the client is done preparing the data received from Discord. Usually after login is successful and the Client.guilds and co. are filled up.
    async def on_ready(self):
        channel = self.get_channel(int(self.channel_id))
        await channel.send('Hello Friend')
    
    # Called when a Message is created and sent.
    async def on_message(self, message):
        if message.author == self.user:
            return
 
        if message.content == 'ping':
            await message.channel.send('pong {0.author.mention}'.format(message))
        else:
            await message.channel.send('running...')

import discord
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
# print(token)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    async def on_message(self,message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

client = MyClient()
client.run(token)

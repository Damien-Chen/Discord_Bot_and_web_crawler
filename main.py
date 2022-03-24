from http import client
import discord
import Network_Spider
from discord.ext import commands
Token = "OTUzOTI5MDk0MDI0ODIyNzk0.YjLtsw.3Sm0XISbSXCQuih3yguxww8YU48"
client = discord.Client()

@client.event
async def on_message(message):
    data = Network_Spider.PData(message.content)
    if message.author == client.user:
        return
    if message.content == 'hello':
        await message.channel.send('hi')
        await message.channel.send(data)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(Token)
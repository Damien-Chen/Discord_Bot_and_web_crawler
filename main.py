from http import client
import discord
import Network_Spider
from discord.ext import commands
Token = Your bot token
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

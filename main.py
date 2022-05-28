from http import client
import discord
import Network_Spider
import Global
import time
import re
from discord.ext import commands
Token = Your Token 
client = discord.Client()

Global.i = 0
character = "'"
character2 = ","
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hi':
        #while Global.num != 0 :
        for i in range(len(Global.list)):
            #data = Network_Spider.PData(message.content)
            #await message.channel.send(data)
            embedVar = discord.Embed(title=Global.list[Global.i], color=0x00ff00)
            link_value = 'ptt.cc',Global.link[Global.i]
            link_value = str(link_value)
            link_value = re.sub("',()", "",link_value)
            embedVar.add_field(name="網址", value=link_value, inline=False)
            await message.channel.send(embed=embedVar)
            Global.i = Global.i + 1
            Global.num = Global.num - 1 
            time.sleep(1)
            

        await message.channel.send("資料已傳送完畢")
        #reset Global.i 
        Global.i = 0
            


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
client.run(Token)





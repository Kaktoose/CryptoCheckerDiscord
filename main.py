import discord
import cryptocompare
import os
from dotenv import load_dotenv
client = discord.Client()
token = os.environ["DISCORD_TOKEN"]
load_dotenv()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
# test message
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    



 #price of Bitcoin
    if message.content.startswith('$price') and message.content.endswith("btc"):
        finalPrice= cryptocompare.get_price("btc", 'usd') 
        await message.channel.send(finalPrice)
    else:
       message.channel.send('Sorry, currently only Nano and Vite are supported :( If you have any suggested currencies...')


#price of nano
    if message.content.startswith('$price') and message.content.endswith("nano"):
        finalPrice= cryptocompare.get_price("nano", 'usd') 
        await message.channel.send(finalPrice)
    else:
       message.channel.send('Sorry, currently only Nano and Vite are supported :( If you have any suggested currencies...')

#price of Ether
    if message.content.startswith('$price') and message.content.endswith("Eth"):
        finalPrice= cryptocompare.get_price("Eth", 'usd') 
        await message.channel.send(finalPrice)
    else:
       message.channel.send('Sorry, currently only Nano and Vite are supported :( If you have any suggested currencies...')


client.run(token)

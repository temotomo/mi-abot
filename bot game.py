import os
import discord

# .envからTOKENを取ってくる
TOKEN = os.getenv("TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print("起動!")
    await client.change_presence(activity=discord.Game(name="幻塔"))


client.run(
    "MTAwOTA5MzQ1NTc2NDUyMTA4MA.GAfrxp.QVRiYLi5_PCltPaRLiv2gy6znAAWDYTWJTwkGU")

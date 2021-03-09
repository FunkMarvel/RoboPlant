import discord
import os
# import requests
# import json
# import random
from replit import db
from keep_alive import keep_alive

#test code (too be replaced once i figure out what to do with this bot):
client = discord.Client()

@client.event
async def on_ready():
  print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  else:
    return

keep_alive()
client.run(os.getenv("TOKEN"))
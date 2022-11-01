import os
import discord
import discord.ext.commands as commands
from dotenv import load_dotenv
from loader import load
load_dotenv()

bot = commands.Bot('p.', intents = discord.Intents(
  guilds = True,
  guild_messages = True,
  message_content = True,
))

for event in load('events'):
  event.setup(bot)

for command in load('commands'):
  command.setup(bot)

for extension in load('extensions'):
  extension.setup(bot)

bot.run(os.getenv('TOKEN'))
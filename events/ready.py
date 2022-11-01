from discord.ext.commands import Bot

def setup(bot: Bot):
  @bot.listen('on_ready')
  async def handler():
    print('ready!')
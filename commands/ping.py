from discord.ext.commands import Bot, Context

def setup(bot: Bot):
  @bot.command('ping')
  async def handler(ctx: Context):
    await ctx.reply('pong!', mention_author = False)
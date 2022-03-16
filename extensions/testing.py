import includes
from discord.ext import commands

class testing(commands.Cog, name='Test commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def test(self, ctx):
        await includes.log(ctx)

def setup(bot):
    bot.add_cog(testing(bot))

import includes
from discord.ext import commands

class testing(commands.Cog, name='Test commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def test(self, ctx):
        await includes.log(ctx)
    
    @commands.command(hidden=True)
    async def testget(self, ctx, arg):
        # Check if a user was mentioned #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None
        
def setup(bot):
    bot.add_cog(testing(bot))

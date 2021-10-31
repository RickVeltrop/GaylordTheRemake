import discord
import includes
from discord.ext import commands


class errorhandler(commands.Cog, name='errorhandler'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f'Error {error} in message \'{ctx.message.content}\' by {ctx.author}')
        await ctx.reply(embed=discord.Embed(title='An error occurred!', description=f'Error: \'{error}\'.\nIf this is a reoccurring issue, please ask for assistance.', color=includes.randomcolor()))

def setup(bot):
    bot.add_cog(errorhandler(bot))

import discord
import includes
from discord.ext import commands


class errorhandler(commands.Cog, name='errorhandler'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error: commands.CommandError):

        message = None
        if isinstance(error, commands.MissingRequiredArgument):
            message = f'You missed a required argument "{error.param}"'
        elif isinstance(error, commands.MissingPermissions):
            message = f'You\'re missing permissions to do that.'
        elif isinstance(error, commands.BotMissingPermissions):
            message = f'I don\'t have permissions to run this command.'
        else:
            message = f'Error: \'{error}\'.\nIf this is a reoccurring issue, please ask for assistance.'

        print(f'Error {error} in message \'{ctx.message.content}\' by {ctx.author}')
        await ctx.reply(embed=discord.Embed(title='An error occurred!', description=message, color=includes.randomcolor()))

def setup(bot):
    bot.add_cog(errorhandler(bot))

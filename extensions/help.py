import discord
from discord.ext import commands
from attributes import helpatt as a


class HelpComm(commands.Cog, name='Help commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=a.help['aliases'], brief=a.help['brief'], description=a.help['description'], enabled=a.help['enabled'], hidden=a.help['hidden'], usage=a.help['usage'])
    async def help(self, ctx, comm=None):
        if comm is not None:
            for command in self.bot.commands:
                if command.name == comm or comm in command.aliases:
                    # Define help text #
                    HelpText = f'``` Help for command {command.name}({comm}): \n'
                    HelpText += f'(Params with a * are optional)\n\n'
                    HelpText += f'{command.description}\n'
                    HelpText += f'Aliases: {[al for al in command.aliases]}\n'
                    HelpText += f'Usage: {command.name} {command.usage}'
                    HelpText += '```'

                    # Send help text and end function #
                    await ctx.reply(HelpText)
                    return
            await ctx.reply(embed=discord.Embed(title='Request failed!', description=f'Could not find command \'{comm}\'.'))
        else:
            # Define start of help text #
            HelpText = '``` Help for all commands: \n'

            # Loop through cogs #
            Cogs = self.bot.cogs
            for cog in Cogs.values():
                # If cog has no commands #
                if len(cog.get_commands()) <= 1: continue

                # Add cog name and commands to the list #
                HelpText += f'\n  --  {cog.qualified_name}:  --  \n'
                for command in cog.get_commands():
                    if command.brief is None or command.hidden is True: continue
                    HelpText += f'{command.name}:   {command.brief}\n'

            # End help text and send text #
            HelpText += '```'
            await ctx.reply(HelpText)

    @commands.command(aliases=a.commhelp['aliases'], brief=a.commhelp['brief'], description=a.commhelp['description'], enabled=a.commhelp['enabled'], hidden=a.commhelp['hidden'], usage=a.commhelp['usage'])
    async def commhelp(self, ctx, comm):
        for command in self.bot.commands:
            if command.name == comm or comm in command.aliases:
                # Define help text #
                HelpText = f'``` Help for command {command.name}({comm}): \n'
                HelpText += f'(Params with a * are optional)\n\n'
                HelpText += f'{command.description}\n'
                HelpText += f'Aliases: {[al for al in command.aliases]}\n'
                HelpText += f'Usage: {command.name} {command.usage}'
                HelpText += '```'

                # Send help text and end function #
                await ctx.reply(HelpText)
                return

        await ctx.reply(embed=discord.Embed(title='Request failed!', description=f'Could not find command \'{comm}\'.'))


def setup(bot):
    bot.add_cog(HelpComm(bot))

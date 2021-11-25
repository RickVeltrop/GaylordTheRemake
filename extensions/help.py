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
                    HelpText += f'(Params with a * are optional, note that you cannot skip params though.)\n\n'
                    HelpText += f'{command.description}\n'
                    HelpText += f'Aliases: {[al for al in command.aliases]}\n'
                    HelpText += f'Usage: {self.bot.command_prefix}{command.name} {command.usage}'
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
                # Start counting commands and backup text #
                ShownAmount = 0
                TextBackup = HelpText

                # Add cog info to command #
                HelpText += f'\n  --  {cog.qualified_name}:  --  \n'
                for command in cog.get_commands():
                    # Check if command should be shown #
                    if command.brief is None or command.hidden is True: continue

                    # Add command to text #
                    ShownAmount += 1
                    HelpText += f'{command.name}:   {command.brief}\n'

                # Check whether enough commands are shown #
                if ShownAmount < 1:
                    HelpText = TextBackup
                    continue

            # End help text and send text #
            HelpText += '```'
            await ctx.reply(HelpText)


def setup(bot):
    bot.add_cog(HelpComm(bot))

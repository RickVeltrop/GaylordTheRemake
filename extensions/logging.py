import datetime
import discord
import json
from discord.ext import commands

Format = f'%H:%M:%S (-2) %a %d/%m/%y'
JsonFile = 'json/logs.json'

class logging(commands.Cog, name='Logging commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions()
    async def log(self, ctx):

        # Prepare log data attributes #
        CommName = 'command:' + ctx.command.name
        AdminName = 'adminname:' + ctx.author.name + '#' + ctx.author.discriminator
        AdminId = 'adminid' + str(ctx.author.id)

        # Log data #
        LogList = [
            CommName,
            AdminName,
            AdminId,
        ]

        # Read data in json file #
        data = {}
        with open(JsonFile, 'r') as file:
            data = json.load(file)
            file.close()

        # Get currently saved logs #
        Logs = {}
        try:
            Logs = data[str(ctx.author.id)]
        except KeyError:
            Logs = {}
            data[str(ctx.author.id)] = {}
        Logs = data[str(ctx.author.id)]

        # Generate key and add log data #
        LogKey = f'Log{len(Logs)}{ctx.command.name}'
        data[str(ctx.author.id)][LogKey] = LogList

        # Write updated data to file and clear data #
        with open(JsonFile, 'w') as file:
            json.dump(data, file)
            file.close()
            data.clear()

    @commands.command()
    @commands.has_permissions()
    async def showlogs(self, ctx):
        print('Test command for showing logs')

def setup(bot):
    bot.add_cog(logging(bot))

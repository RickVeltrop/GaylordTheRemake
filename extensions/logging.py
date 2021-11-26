import datetime
import discord
import json
from discord.ext import commands

Format = f'%H:%M:%S (-2) %a %d/%m/%y'
JsonFile = 'json/logs.json'

class log():
    def __init__(self, command, admin):
        CurrTime = datetime.datetime.today().strftime(Format)

        self.command = command
        self.admin = admin
        self.time = CurrTime

class logging(commands.Cog, name='Logging commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions()
    async def log(self, ctx):
        print('Test command for creating logs')

        data = {}
        data[ctx.command.name+str(ctx.author.id)] = {'Command': ctx.command.name, 'AdminName': f'{ctx.author.name}#{ctx.author.discriminator}', 'AdminId': ctx.author.id}

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

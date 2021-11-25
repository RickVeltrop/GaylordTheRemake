import datetime
import discord
from discord.ext import commands

Format = f'%H:%M:%S (-2) %a %d/%m/%y'

class log():
    def __init__(self, command, admin):
        CurrTime = datetime.datetime.today().strftime(Format)

        self.command = command
        self.admin = admin
        self.time = CurrTime

class admin(commands.Cog, name='Logging commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions()
    async def createlog(self, ctx):
        await ctx.reply('Test command for creating logs')

    @commands.command()
    @commands.has_permissions()
    async def showlogs(self, ctx):
        await ctx.reply('Test command for showing logs')

def setup(bot):
    bot.add_cog(admin(bot))

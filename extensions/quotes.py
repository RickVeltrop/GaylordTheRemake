import discord
import includes
from discord.ext import commands

class quotecmds(commands.Cog, name='Quote commands'):
    @commands.command()
    @commands.has_permissions()
    async def quote(self, ctx):
        print(ctx)

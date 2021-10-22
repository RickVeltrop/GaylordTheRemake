import discord
from discord.ext import commands

class admin(commands.Cog, name='Admin commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getperms(self, ctx):
        # Check if a user was mentioned or default to author #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else ctx.author

        # Get users perms and create embed #
        UserPerms = dict(user.guild_permissions)
        EmbedText = f',\n'.join(f'{key}: {val}' for key, val in UserPerms.items())
        Embed = discord.Embed(title=f'Permissions for {user.mention}', description=EmbedText)
        await ctx.send(embed=Embed)

def setup(bot):
    bot.add_cog(admin(bot))

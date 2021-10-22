import json
import discord
from discord.ext import commands

JsonFile = 'json/data.json'

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

    @commands.command()
    async def warn(self, ctx, reason):
        # Check if a user was mentioned #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None
        if user is None: await ctx.send(embed=discord.Embed(title="Request failed!", description="You need to mention a user to warn."))

        # Read current data from file #
        data = None
        with open(JsonFile, 'r') as file:
            data = dict(json.load(file))
            file.close()

        # Check if there is data or not #
        if str(user.id) in data:
            data[str(user.id)]['warns'].append([reason, str(ctx.author.id)])
        else:
            data[user.id] = {"warns": [[reason, ctx.author.id]]}

        # Write updated data to file and clear data #
        with open(JsonFile, 'w') as file:
            json.dump(data, file)
            file.close()
            data.clear()


def setup(bot):
    bot.add_cog(admin(bot))

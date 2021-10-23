import json
import discord
from discord.ext import commands

JsonFile = 'json/warns.json'

class admin(commands.Cog, name='Admin commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['g', 'perms'])
    async def getperms(self, ctx):
        # Check if a user was mentioned or default to author #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else ctx.author

        # Get users perms and create embed #
        UserPerms = dict(user.guild_permissions)
        EmbedText = f',\n'.join(f'{key}: {val}' for key, val in UserPerms.items())
        Embed = discord.Embed(title=f'Permissions for {user.mention}', description=EmbedText)
        await ctx.send(embed=Embed)

    @commands.command(aliases=['w'])
    async def warn(self, ctx, reason):
        # Check if a user was mentioned #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None
        if user is None:
            await ctx.send(embed=discord.Embed(title="Request failed!", description="You need to mention a user to warn."))
            return

        # Read current data from file #
        with open(JsonFile, 'r') as file:
            data = dict(json.load(file))
            file.close()

        # Check whether there is data or not #
        if str(user.id) in data:
            data[str(user.id)]['warns'].append([reason, str(ctx.author.id)])
        else:
            data[user.id] = {"warns": [[reason, ctx.author.id]]}

        # Write updated data to file and clear data #
        with open(JsonFile, 'w') as file:
            json.dump(data, file)
            file.close()
            data.clear()

    @commands.command(aliases=['s', 'warns'])
    async def showwarns(self, ctx):
        # Check if a user was mentioned #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None
        if user is None:
            await ctx.send(embed=discord.Embed(title="Request failed!", description="You need to mention a user to show."))
            return

        # Read current data from file #
        with open(JsonFile, 'r') as file:
            data = dict(json.load(file))
            file.close()

        # Prepare discord embed #
        Embed = discord.Embed(title='Warns', description='Warns for <user>, first item is for format')
        Embed.add_field(name='Admin ID', value='Reason', inline=False)

        # Bool to determine whether there is data #
        HasData = False
        for userid, val in data.items():
            # Check if this item is the user we're looking for #
            if str(user.id) in userid:
                for item in data[userid]['warns']:
                    # If data has been found #
                    HasData = True
                    Embed.add_field(name=item[0], value=item[1], inline=False)

        # Report back to user #
        if HasData:
            await ctx.send(embed=Embed)
        elif not HasData:
            await ctx.send(embed=discord.Embed(title='No data!', description='No data was found for this user.'))


def setup(bot):
    bot.add_cog(admin(bot))

import json
import datetime
import discord
from discord.ext import commands

TimeFormat = '%H:%M:%S (gmt-1) on %a %d/%m/%y'
JsonFile = 'json/warns.json'

class admin(commands.Cog, name='Admin commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['mention', 'get', 'user'])
    async def getuser(self, ctx, userid):
        await ctx.send(f"<@!{userid}>")

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

        # Check whether reason is within allowed length #
        if len(reason) > 50:
            await ctx.send(embed=discord.Embed(title="Request failed!", description="Your reason has to be shorter."))
            return

        # Read current data from file #
        with open(JsonFile, 'r') as file:
            data = dict(json.load(file))
            file.close()

        # Include time in warn #
        CurrentTime = datetime.datetime.today()
        CurrentTime = CurrentTime.strftime(TimeFormat)
        TimeText = f" (at {CurrentTime})."

        # Check whether there is data or not #
        if str(user.id) in data:
            data[str(user.id)]['warns'].append([reason, str(ctx.author.id), TimeText])
        else:
            data[user.id] = {"warns": [[reason, str(ctx.author.id), TimeText]]}

        # Write updated data to file and clear data #
        with open(JsonFile, 'w') as file:
            json.dump(data, file)
            file.close()
            data.clear()

        # Report back to the user #
        await ctx.send(embed=discord.Embed(title='Success!', description=f'Warned {user.name} for {reason}'))

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
        Embed = discord.Embed(title=f'Warns for {user.name}:')

        # Bool to determine whether there is data #
        HasData = False
        for userid, val in data.items():
            # Check if this item is the user we're looking for #
            if str(user.id) == userid:
                for item in data[userid]['warns']:
                    # If data has been found #
                    HasData = True

                    # Prepare text and add field to embed #
                    Text = f'Admin ID: {item[1]}\nTime: {item[2]}'
                    Embed.add_field(name=item[0], value=Text, inline=False)

        # Report back to user #
        if HasData:
            await ctx.send(embed=Embed)
        elif not HasData:
            await ctx.send(embed=discord.Embed(title='No data!', description='No data was found for this user.'))


def setup(bot):
    bot.add_cog(admin(bot))

import json
import discord
import datetime
from attributes import adminatt as a
from discord.ext import commands
import includes

TimeFormat = '%H:%M:%S (gmt-1) on %a %d/%m/%y'
JsonFile = 'json/warns.json'

class admin(commands.Cog, name='General admin commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=a.getuser['aliases'], brief=a.getuser['brief'], description=a.getuser['description'], enabled=a.getuser['enabled'], hidden=a.getuser['hidden'], usage=a.getuser['usage'])
    @commands.has_permissions(mention_everyone=True)
    async def getuser(self, ctx, userid):
        await ctx.reply(f"<@!{userid}>")

    @commands.command(aliases=a.getperms['aliases'], brief=a.getperms['brief'], description=a.getperms['description'], enabled=a.getperms['enabled'], hidden=a.getperms['hidden'], usage=a.getperms['usage'])
    @commands.has_permissions(manage_roles=True)
    async def getperms(self, ctx, mention=None):
        # Check if a user was mentioned or default to author #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else ctx.author

        # Get users perms and create embed #
        UserPerms = dict(user.guild_permissions)
        EmbedText = f',\n'.join(f'{key}: {val}' for key, val in UserPerms.items())
        Embed = discord.Embed(title=f'Permissions for {user.name}', description=EmbedText, color=includes.randomcolor())
        await ctx.reply(embed=Embed)

    @commands.command(aliases=a.kick['aliases'], brief=a.kick['brief'], description=a.kick['description'], enabled=a.kick['enabled'], hidden=a.kick['hidden'], usage=a.kick['usage'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, mention, kickreason):
        # Check if a user was mentioned #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None
        if user is None:
            await ctx.reply(embed=discord.Embed(title="Request failed!", description="You need to mention a user to kick.", color=includes.randomcolor()))
            return

        # Check whether reason is within allowed length #
        if len(kickreason) > 50:
            await ctx.reply(embed=discord.Embed(title="Request failed!", description="Your reason has to be shorter.", color=includes.randomcolor()))
            return

        # Kick member and report back to the user #
        await ctx.guild.kick(user=user, reason=kickreason)
        await ctx.reply(embed=discord.Embed(title="Success!", description=f"{user.name} was kicked from the server"))

    @commands.command(aliases=a.ban['aliases'], brief=a.ban['brief'], description=a.ban['description'], enabled=a.ban['enabled'], hidden=a.ban['hidden'], usage=a.ban['usage'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, mention, banreason):
        # Check if a user was mentioned #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None
        if user is None:
            await ctx.reply(embed=discord.Embed(title="Request failed!", description="You need to mention a user to ban.", color=includes.randomcolor()))
            return

        # Check whether reason is within allowed length #
        if len(banreason) > 50:
            await ctx.reply(embed=discord.Embed(title="Request failed!", description="Your reason has to be shorter.", color=includes.randomcolor()))
            return

        # Ban member and report back to the user #
        await ctx.guild.ban(user=user, reason=banreason, delete_message_days=0)
        await ctx.reply(embed=discord.Embed(title="Success!", description=f"{user.name} was banned from the server", color=includes.randomcolor()))

    @commands.command(aliases=a.warn['aliases'], brief=a.warn['brief'], description=a.warn['description'], enabled=a.warn['enabled'], hidden=a.warn['hidden'], usage=a.warn['usage'])
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, mention, reason):
        # Check if a user was mentioned #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None
        if user is None:
            await ctx.reply(embed=discord.Embed(title="Request failed!", description="You need to mention a user to warn.", color=includes.randomcolor()))
            return

        # Check whether reason is within allowed length #
        if len(reason) > 50:
            await ctx.reply(embed=discord.Embed(title="Request failed!", description="Your reason has to be shorter.", color=includes.randomcolor()))
            return

        # Read current data from file #
        with open(JsonFile, 'r') as file:
            data = dict(json.load(file))
            file.close()

        # Include time in warn #
        CurrentTime = datetime.datetime.today()
        CurrentTime = CurrentTime.strftime(TimeFormat)
        CurrentTime = f" (at {CurrentTime})."

        # Check whether there is data or not #
        if str(user.id) in data:
            data[str(user.id)]['warns'].append([reason, str(ctx.author.id), CurrentTime])
        else:
            data[user.id] = {"warns": [[reason, str(ctx.author.id), CurrentTime]]}

        # Write updated data to file and clear data #
        with open(JsonFile, 'w') as file:
            json.dump(data, file)
            file.close()
            data.clear()

        # Report back to the user #
        await ctx.reply(embed=discord.Embed(title='Success!', description=f'Warned {user.name} for {reason}', color=includes.randomcolor()))

    @commands.command(aliases=a.showwarns['aliases'], brief=a.showwarns['brief'], description=a.showwarns['description'], enabled=a.showwarns['enabled'], hidden=a.showwarns['hidden'], usage=a.showwarns['usage'])
    @commands.has_permissions(kick_members=True)
    async def showwarns(self, ctx, mention):
        # Check if a user was mentioned #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None
        if user is None:
            await ctx.reply(embed=discord.Embed(title="Request failed!", description="You need to mention a user to show.", color=includes.randomcolor()))
            return

        # Read current data from file #
        with open(JsonFile, 'r') as file:
            data = dict(json.load(file))
            file.close()

        # Prepare discord embed #
        Embed = discord.Embed(title=f'Warns for {user.name}:', color=includes.randomcolor())

        # Bool to determine whether there is data #
        HasData = False
        for userid, val in data.items():
            # Check if this item is the user we're looking for #
            if str(user.id) == userid:
                for item in data[userid]['warns']:
                    # If data has been found #
                    HasData = True

                    # Define list contents #
                    WarnReason = item[0]
                    AdminName = self.bot.get_user(int(item[1])).name
                    AdminID = item[1]
                    WarnTime = item[2]

                    # Prepare text and add field to embed #
                    Text = f'Admin name: \'{AdminName}\'.\nAdmin ID: {AdminID}\nTime: {WarnTime}'
                    Embed.add_field(name=WarnReason, value=Text, inline=False)

        # Report back to user #
        if HasData:
            await ctx.reply(embed=Embed)
        elif not HasData:
            await ctx.reply(embed=discord.Embed(title='No data!', description='No data was found for this user.', color=includes.randomcolor()))


def setup(bot):
    bot.add_cog(admin(bot))

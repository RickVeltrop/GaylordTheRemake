import discord
import includes
from discord.ext import commands
from attributes import channeladmin as a

LockedChannels = []

class channeladmin(commands.Cog, name='Channel admin commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=a.lockchannel['aliases'], brief=a.lockchannel['brief'], description=a.lockchannel['description'], enabled=a.lockchannel['enabled'], hidden=a.lockchannel['hidden'], usage=a.lockchannel['usage'])
    @commands.has_permissions(manage_channels=True)
    async def lockchannel(self, ctx, channel=None):
        # Check if a channel was mentioned #
        channel = ctx.message.channel_mentions[0] if len(ctx.message.channel_mentions) > 0 else ctx.channel

        # Add locked channel to list #
        LockedChannels.append(channel)

        # Edit channel perms and report to user #
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.reply(embed=discord.Embed(title='Success!', description=f'Locked {channel.name}.', color=includes.randomcolor()))

    @commands.command(aliases=a.unlock['aliases'], brief=a.unlock['brief'], description=a.unlock['description'], enabled=a.unlock['enabled'], hidden=a.unlock['hidden'], usage=a.unlock['usage'])
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel=None):
        # Check if a channel was mentioned #
        channel = ctx.message.channel_mentions[0] if len(ctx.message.channel_mentions) > 0 else ctx.channel

        # Check if given channel is locked #
        if channel not in LockedChannels:
            await ctx.reply(embed=discord.Embed(title='Request failed!', description='This channel is not locked', color=includes.randomcolor()))
            return

        # Edit channel perms and report to user #
        await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.reply(embed=discord.Embed(title='Success!', description=f'Unlocked {channel.name}.', color=includes.randomcolor()))

    @commands.command(aliases=a.purge['aliases'], brief=a.purge['brief'], description=a.purge['description'], enabled=a.purge['enabled'], hidden=a.purge['hidden'], usage=a.purge['usage'])
    @commands.has_permissions(manage_channels=True)
    async def purge(self, ctx, amount=None, user=None, channel=None):
        # Get channel and user if available #
        channel = ctx.message.channel_mentions[0] if len(ctx.message.channel_mentions) > 0 else ctx.channel
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None

        # Default amount to none if user entered inf #
        amount = None if amount == 'inf' else amount

        # If no user specified, delete any messages #
        purged = []
        if user is None:
            purged = await channel.purge(limit=amount)

        # If a user if specified, loop through message history #
        elif user is not None:
            # Get channel history #
            history = await channel.history(limit=amount).flatten()

            # Loop through messages #
            for msg in history:
                # Check if this message should be deleted #
                if msg.author.id is user.id:
                    await msg.delete()
                    purged.append(msg)

        try:
            await ctx.reply(embed=discord.Embed(title=f'Purged {channel.name}', description=f'Purged {len(purged)} messages.', color=includes.randomcolor()))
        except:
            await ctx.send(embed=discord.Embed(title=f'Purged {channel.name}', description=f'Purged {len(purged)} messages.', color=includes.randomcolor()))

    @commands.command(aliases=a.spam['aliases'], brief=a.spam['brief'], description=a.spam['description'], enabled=a.spam['enabled'], hidden=a.spam['hidden'], usage=a.spam['usage'])
    @commands.has_permissions(manage_channels=True)
    async def spam(self, ctx, amount, msg, channel=None):
        # Get channel if one is mentioned #
        channel = ctx.message.channel_mentions[0] if len(ctx.message.channel_mentions) > 0 else ctx.channel

        # Send specified amount of messages #
        for num in range(1, int(amount)):
            await channel.send(msg)

        # Report back to the user #
        await ctx.reply(embed=discord.Embed(title=f'Spammed {channel.name}', description=f'Sent {msg} {amount} times in {channel.name}.', color=includes.randomcolor()))


def setup(bot):
    bot.add_cog(channeladmin(bot))

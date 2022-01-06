import datetime
import discord
import json
import includes
from discord.ext import commands

Format = f'%H:%M:%S (-2) %a %d/%m/%y'
JsonFile = 'json/logs.json'

class logging(commands.Cog, name='Logging commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions()
    async def log(self, ctx, testarg1, testarg2):

        # Prepare log data attributes #
        CommName = ctx.command.name
        AdminName = ctx.author.name + '#' + ctx.author.discriminator
        AdminId = str(ctx.author.id)
        ArgsList = [testarg1, testarg2]
        InvTime = datetime.datetime.today().strftime(Format)

        # Log data #
        LogList = [
            CommName,
            AdminName,
            AdminId,
            ArgsList,
            InvTime,
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
    async def showlogs(self, ctx, userid=None):
        # Check if a user was mentioned #
        user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None
        if user is None:
            if userid is None:
                await ctx.reply(embed=discord.Embed(title="Request failed!", description="You need to mention a user to warn.", color=includes.randomcolor()))
                return
            elif userid is not None:
                user = self.bot.get_user(int(userid))

        # Read data in json file #
        data = {}
        with open(JsonFile, 'r') as file:
            data = dict(json.load(file))
            file.close()

        userlogs = dict(data[str(user.id)])
        data.clear()

        embed = discord.Embed(title=f'Logs for {user.name}#{user.discriminator}')
        for key, log in userlogs.items():
            CommName = log[0]
            AdminName = log[1]
            AdminId = log[2]
            ArgsList = log[3]
            InvTime = log[4]

            admin = self.bot.get_user(int(AdminId))

            FieldText = f'Admin:{admin.id}#{admin.discriminator}\nArguments: {ArgsList}\nTime: {InvTime}'
            embed.add_field(name=f'{CommName}', value=FieldText, inline=False)

        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(logging(bot))

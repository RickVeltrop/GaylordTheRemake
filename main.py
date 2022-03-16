import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

Intents = discord.Intents.default()
Intents.members = True

Client = commands.Bot(
    command_prefix='-',
    case_insensitive=True,
    intents=Intents,
    help_command=None,
)

@Client.event
async def on_ready():
    Activity = discord.Game(f'{Client.command_prefix}help')
    await Client.change_presence(status=discord.Status.online, activity=Activity)
    print(f'Logged in as {Client.user}')

ext = [
    'extensions.testing',
    'extensions.admin',
    'extensions.channeladmin',
    'extensions.help',
    'extensions.errors',
]

if __name__ == "__main__":
    for extension in ext:
        Client.load_extension(extension)
    Client.run(os.getenv('TOKEN'))

'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  To do:  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

-- Admin logging
-- Fun commands
-- Quote command and managing

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''

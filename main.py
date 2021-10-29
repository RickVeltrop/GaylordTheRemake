import discord
from discord.ext import commands

Client = commands.Bot(
    command_prefix='-',
    case_insensitive=True,
)

@Client.event
async def on_ready():
    Activity = discord.Game(f'{Client.command_prefix}help')
    await Client.change_presence(status=discord.Status.online, activity=Activity)
    print(f'Logged in as {Client.user}')

ext = [
    'extensions.testing',
    'extensions.admin',
    'extensions.errors',
]

if __name__ == "__main__":
    for extension in ext:
        Client.load_extension(extension)
    Client.run('OTAwNzc5NjE5MjI4MjE3Mzg1.YXGSZA.gZLNFnEObiDg1jHjYxRKcXNYrTE')

'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  To do:  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

-- Admin logging
-- Mutes
-- Fun commands

-- Admin username in showwarns

-- Help command
-- Error handling

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''

import asyncio
from os import *
import discord
from discord.ext import commands
import colorama as cr
from dotenv import load_dotenv

load_dotenv()
cr.init()

Intents = discord.Intents.default()
Intents.message_content = True

# Gaylord is the bot's name
Gaylord = commands.Bot(
 	command_prefix='>',
 	case_insensitive=True,
 	intents=Intents,
 	owner_id=getenv('OWNER'),
)


@Gaylord.event
async def on_ready():
	print(f'{cr.Fore.BLUE}Logged in as {Gaylord.user}{cr.Fore.RESET}')

	Activity = discord.Game('with ur mom`s clit')
	await Gaylord.change_presence(status=discord.Status.online, activity=Activity)


async def main():
	for file in listdir('./cogs'):
		if not file.endswith('.py'): continue
		await Gaylord.load_extension(f'cogs.{file[:-3]}')

	token = getenv('TOKEN')
	async with Gaylord:
		await Gaylord.start(token)


if __name__ == '__main__':
	asyncio.run(main())

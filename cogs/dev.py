from logger import Logging,LogInfo,LogType
import discord
from discord.ext import commands
import os
import sys

class dev(commands.Cog, name='Development commands'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(hidden=False)
	async def kill(self, ctx):
		LogInfo(f'{ctx.author.name}({ctx.author.id}) killed discord.', LogType.LOG, True)

		await ctx.reply('Protocol 2. Uphold the Mission.')
		sys.exit()

	@commands.command(hidden=False)
	async def restart(self, ctx):
		LogInfo(f'{ctx.author.name}({ctx.author.id}) restarted Gaylord.', LogType.LOG, True)

		await ctx.reply('Restarting myself! This should only take a second.')
		os.system('python ./main.py')
		sys.exit()

	@commands.command(hidden=False)
	async def getlogs(self, ctx):
		data = Logging.GetAllLogs()
		embed = discord.Embed(title='Logs')
		for i,v in reversed(data.items()):
			embed.add_field(name=i,value=v['msg'], inline=False)
		
		await ctx.reply(embed=embed)
	
	@commands.command(hidden=False)
	async def getlastlog(self, ctx):
		data = Logging.GetAllLogs()
		(id, log) = next(iter(reversed(data.items())))
		embed = discord.Embed(title='Logs')
		embed.add_field(name=id,value=log['msg'], inline=False)

		await ctx.reply(embed=embed)

async def setup(bot):
	await bot.add_cog(dev(bot))

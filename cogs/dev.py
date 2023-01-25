import discord
from discord.ext import commands
import os
import sys

class test(commands.Cog, name='Test commands'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(hidden=False)
	async def kill(self, ctx):
		await ctx.reply('Protocol 2. Uphold the Mission.')
		sys.exit()

	@commands.command(hidden=False)
	async def restart(self, ctx):
		await ctx.reply('Restarting myself! This should only take a second.')
		os.system('python ./main.py')
		sys.exit()

async def setup(bot):
	await bot.add_cog(test(bot))

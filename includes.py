import json
import discord
from random import choice
from discord import Color as c

JsonFile = 'json/logs.json'

colors = [
	c.from_rgb(255, 255, 255),		# White
	c.from_rgb(100, 100, 100),		# Grey
	c.from_rgb(0, 0, 0),			# Black
	c.from_rgb(255, 100, 100),		# Light red
	c.from_rgb(255, 0, 0),			# Red
	c.from_rgb(155, 0, 0),			# Dark red
	c.from_rgb(255, 100, 0),		# Orange
	c.from_rgb(255, 255, 0),		# Yellow
	c.from_rgb(125, 150, 100),		# Light green
	c.from_rgb(0, 255, 0),			# Green
	c.from_rgb(40, 70, 45),			# Dark green
	c.from_rgb(0, 175, 255),		# Light blue
	c.from_rgb(0, 0, 255),			# Blue
	c.from_rgb(0, 35, 100),			# Dark blue
	c.from_rgb(255, 150, 220),		# Light pink
	c.from_rgb(255, 0, 255),		# Pink
	c.from_rgb(170, 0, 170),		# Magenta
	c.from_rgb(125, 0, 125)			# Purple
]

# Function to return a random embed color #
def randomcolor():
	# Return a random color #
	return choice(colors)

async def log(ctx, args=[]):
	# Check if a user was mentioned #
	user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None
	
	MsgId = ctx.message.id
	Admin = ctx.author
	CmdName = ctx.command.name
	Target = user if user is not None else 'None'
	
	LogData = {
		'Admin': f'{Admin.name}#{Admin.discriminator}',
		'AdminId': Admin.id,
		'CommandName': CmdName,
		'Target': f'{Target.name}#{Target.discriminator}' if user is not None else None,
		'TargetId': Target.id if user else None,
		'Args': args,
	}
	
	with open(JsonFile, 'r') as file:
		JsonCont = dict(json.load(file))
	
	JsonCont[MsgId] = LogData
	
	with open(JsonFile, 'w') as file:
		json.dump(JsonCont, file)
	
	await ctx.reply(f'Admin: {Admin} : {Admin.id}\nCmd: {CmdName}\nTarget: {Target} : {Target.id if user else "None"}')

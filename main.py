import discord, asyncio, requests
from discord.ext import tasks, commands
from discord.ui import View
from bs4 import BeautifulSoup
import get42mail
import atexit
import json

param = json.load(open('token/param.json', 'r'))
token = open('token/bottoken', 'r').read()
adminid = param.get('adminid')

async def send_embed(mails, mails_contents):
	user = await client.fetch_user(adminid)
	embed = discord.Embed(
		title='42 Mails',
		url='https://profile.intra.42.fr/',
		color=discord.Color.blue())
	i = 0
	for mail in mails:
		embed.add_field(name=mails[i], value=mails_contents[i], inline=False)
		i += 1
	await user.send(embed=embed)

class bot(discord.Client):
	async def on_ready(bot):
		bot.check_mails.start()

	@tasks.loop(seconds=param.get('refreshtime'))
	async def check_mails(bot):
		mails, mails_contents = await get42mail.get_mails()
		if mails and mails_contents:
			await send_embed(mails, mails_contents)
	
intents = discord.Intents.default()
intents = discord.Intents()
client = bot(intents=intents)
client.run(token)
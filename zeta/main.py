import discord
from random import choice, randint
import requests
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('edward'):
            await message.channel.send('of course he is gay {0.author.mention}'.format(message))
        if message.content.startswith('but'):
            await message.channel.send('edward is gay.xD {0.author.mention}'.format(message))
        if message.content.startswith('really?'):
            await message.channel.send('YES! INDEED. {0.author.mention}'.format(message))
        if message.content.startswith('really?...'):
            await message.channel.send('Of course not. {0.author.mention}'.format(message))
        if message.content.startswith('/'):
            await message.channel.send('not really {0.author.mention}'.format(message))
        if message.content.startswith('fuck'):
            await message.channel.send('no u {0.author.mention}'.format(message))
        if message.content.startswith('really?'):
            await message.channel.send('yes! indeed. {0.author.mention}'.format(message))
        if message.content.startswith('lol'):
            await message.channel.send('LOL. {0.author.mention}'.format(message))
        if message.content.startswith('?'):
            await message.channel.send('What? {0.author.mention}'.format(message))
        if message.content == '%cf':
          choices = ('heads', 'tails')
          await message.channel.send(choice(choices))
        if message.content == '%dice':
          choices = randint (1,6)
          await message.channel.send(choices)
        if message.content.startswith('cat'):
          await message.channel.send(requests.get('http://thecatapi.com/api/images/get?format=src&type=gif').url + ' :cat:')
        if message.content.lower().startswith('!game '):
          if str(message.author) == 'ConfectrixAlpha#9538':await client.change_presence(status=discord.Status.idle,activity=discord.Game(name=message.content[6:]))
        if message.content == "any":
          emoji = discord.utils.get(message.author.guild.emojis, name='yeenaw')
          await message.add_reaction(emoji)
        elif message.content.startswith('cat!'):
            # output a cat picture
            await message.channel.send(requests.get('http://thecatapi.com/api/images/get?format=src&type=jpg').url + ' :cat:')
client = MyClient()
client.run("NzQxMTA4OTQxMzQ5NzE1OTY4.XyyxfA.3Iw0Z7C2ao43_qTd3SQJiIXBCJo")
import discord
import os
import json
import requests
from textblob.translate import Translator
from server import keep_alive
from discord.ext import commands
from discord import *

trans = Translator()
bot = commands.Bot(command_prefix='>>')


#this is for the !!sad thing
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


#this thing im still doing but its about roles


class Myclient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 918176347925389353

    async def on_raw_reaction_add(self, payload):
        '''adns'''

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        print(payload.emoji.name)

        if payload.emoji.name == baka:
            return

        elif payload.emoji.name == smart:
            return

        elif payload.emoji.name == wutwut:
            return

    async def botbutton(ctx):
        bot = Button(label='Accept', style=discord.buttonstyle.green)
        view = View()
        view.add_item(button)
        await ctx.send('Hello', view=view)
#this thing im still doing but its about roles

    async def on_ready(self):
        print('Im online')

#these are for the rest of the commands

    async def on_message(self, message):
        if message.author == client.user:
            return

    #the  one above  says that dont respond to bot message
        if message.content.startswith('!!hello'):
            await message.channel.send('hello!')

    async def button(ctx, message):
        if message.content.startswith('!!nitro'):
            await ctx.send(
                'This is a button',
                components=[Button(style='Buttonstyle.blue', label='Accept')])
            interaction = await client.wait_for(
                'Button Click',
                lambda i: i.component.label.startswith('Accept'))
            await interaction.respond(content='Button clicked!')

        if message.content.startswith('!!gt'):
            quote = get_quote()
            await message.channel.send(r'''!!ok imma hack frag :computer:''')
        if message.content.startswith('!!sad'):
            quote = get_quote()
            await message.channel.send(quote)

        if message.content.startswith('!!hax'):
            emoji = "<a:Hacking:924723090829766666>"
            quote = get_quote()
            await message.channel.send(r'''!!ok imma hack Nasa %s''' % emoji)
        if message.content.startswith('!!help'):
            await message.channel.send('''!!bye - sends bye 
      !!helo - sends hello''')

        if message.content.startswith('!!bye'):
            await message.channel.send('bye')
        

            if message.content.startswith('!!delete'):
                await message.channel.delete()

        msg_content = message.content.lower()

        sad_word = ['sad', 'very sad', 'unhappy', 'im feeling depressed']
        bag = ['working', 'ded', 'bot', 'coding', 'code', 'python']
        curseWord = ['Fuck', 'F@ck', 'fuck']

        stram = ['streaming', 'stream', 'when', 'join']

        dic1 = ['good night', 'sleep']

        dic2 = ['is talking', 'is speaking', 'can talk']
        dic3 = ['ded', 'died', 'dead']
        usera = [754466652472737832, 629960365127761950, 843455784192573440]

        #this one says if any word from dict 1 ( a little up) is being used in dsicord , respond with you should sleep
        if any(word in msg_content for word in dic1):
            await message.channel.send('Yep,you should sleep')

        if any(word in msg_content for word in dic3):
            await message.channel.send('Wut u saying, im alive')

        if any(word in msg_content for word in dic2):
            await message.channel.send('Ofc i can talk. shh')

        if any(word in msg_content for word in curseWord):
            await message.delete()

        if any(word in msg_content for word in stram):
            if user == 754466652472737832:
                await message.channel.send(
                    'streaming huh?!,would i be able to join? :evil_laugh:')

        if any(word in msg_content for word in bag):
            #bacon = client.get_user(754466652472737832)
            #fragvh = client.get_user(765932582177079306)
            #zero = client.get_user(629960365127761950)
            fragvh = client.get_user(765932582177079306)
            oldest = client.get_user(843455784192573440)

            #await zero.send('Hey oldest me is your own creation i have been bothering zero and frag for so long that they now hate living hmmm ur time has come now hahahaha evil laugh')
            await oldest.send(
                'Hey oldest me is your own creation i have been bothering zero and frag for so long that they now hate living hmmm ur time has come now hahahaha evil laugh'
            )

    async def on_message_edit(self, before, after):
        if message.author.bot:
            return
        else:
            await before.channel.send(f'@{before.author}  edit message.\n'
                                      f'Before: {before.content}\n'
                                      f'After: {after.content}')


#its myclient by oldest
#its 3am now failed but still good goin
#me very dumb damn cry
#but how. I think we need oldest

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send(
            f'{user} reacted with {reaction.emoji}')

    async def on_message(self, message):

        if message.author.bot:
            return  # ignore bots
        if message.content.startswith("kr "):
            mess = message.content[3:]
            for i in range (100):
              await message.channel.send('> ' +
                                       trans.translate(mess, to_lang='ko'))
        if message.content.startswith("en "):
            content = message.content[3:]
            await message.channel.send('> ' +
                                       trans.translate(content, to_lang='en'))
        #if message:
        #await message.add_reaction('👍')

intents = discord.Intents.default()
intents.members = True
keep_alive()

client = Myclient(intents=intents)
client.run(os.getenv('TOKEN'))

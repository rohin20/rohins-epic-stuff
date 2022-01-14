import discord
import time

thing = 'token i wont share'

client = discord.Client()


@client.event
async def on_ready():
    print('HELLO BOZOS')





@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    usr_msg = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {usr_msg} ({channel}')




    if message.author == client.user:
        return

    if message.channel.name == 'chat' or message.channel.name == 'general':
        if username == 'rohin':
            if usr_msg.lower() == 'ratio':
                await message.channel.send(
                    f'u fell off + ratio + ur white + ur british + who asked + no u + deez nutz + radio + dont care + didnt ask  caught in 4k + cope + seethe + gg + ur moms white + the hood watches Markiplier now + grow the fuck up + L + L pt. 2 + retweet + ligma + taco bell dorito crunch + think outside the bun bitch + ur benched + ur a wrench + i own u  + ur dad fell off + my dad could beat your dad up + ur aim hacking + silver elite + tryhard + boomer + sksksksk 💅 + ur beta + im sigma + youre submissive + L ')
                return
            if usr_msg.lower() == 'hello':
                await message.channel.send(f'hi {username}! i missed you!!!')
                return
            if usr_msg.lower() == 'not funny':
                await message.channel.send(f'i agree')
                return
        if username != 'rohin':
            if usr_msg.lower() == 'ratio':
                await message.channel.send(f'L')
                return
            if usr_msg.lower() == 'hello':
                await message.channel.send(f'shut up {username}')
                return
        if usr_msg.lower() == '5v5':
            await message.channel.send(f'virgin game')
            return
        if 'rohin' in usr_msg.lower():
            await message.channel.send(f'rohin is my lord and saviour')
            return
        if 'romoney' in usr_msg.lower():
            await message.channel.send(f'ROMONEY IN THE STREETS, ROHONEY IN THE SHEETS.')
            return
        if 'big boss' in usr_msg.lower():
            await message.channel.send(f'the sn1per????')
            return
        if 'no' in usr_msg.lower():
            await message.channel.send(f'too bad')
            return
        if 'thanks' in usr_msg.lower():
            await message.channel.send(f':)')
            return
        if 'some bitches' in usr_msg.lower():
            await message.channel.send(f'not funny')
            return
        if username == 'oattisoatmeal':
            if usr_msg.lower() == 'muhbunkey':
                await message.channel.send(f'ITS THE MAN WITH A MILLION NAMES')
                return




client.run(thing)

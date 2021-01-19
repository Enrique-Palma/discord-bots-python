#Pizza Bot Discord 1/18/2021
#Enrique Palma
import discord
import os

from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$napolitan'):
        await message.channel.send(
            "https://www.youtube.com/watch?v=G-jPoROGHGE&t=501s")

    if message.content.startswith('$detroit'):
        await message.channel.send(
            "https://www.kingarthurbaking.com/recipes/king-arthurs-detroit-style-pizza-recipe"
        )

    if message.content.startswith('$chicago-deep-dish'):
        await message.channel.send(
            "https://www.realdeepdish.com/deepdishholygrail/")

    if message.content.startswith('$chicago-tavern'):
        await message.channel.send(
            "https://www.realdeepdish.com/2020/11-12-chicago-thin-crust-pizza-yes-its-a-thing/"
        )

    if message.content.startswith('$new-york'):
        await message.channel.send(
            'The Best New York Style Pizza Dough and 14 Tips for Success!!')

    if message.content.startswith('$new-york'):
        await message.channel.send(
            "https://feelingfoodish.com/the-best-new-york-style-pizza-dough/#wprm-recipe-container-4979"
        )


keep_alive()
client.run(os.getenv('TOKEN'))

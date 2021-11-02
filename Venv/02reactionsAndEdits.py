import discord

# Using this client object to talk to discord api or socket
client = discord.Client()
TOKEN = ''
# Any event in discord can be listened

# called whenever the bot is online or logged in
@client.event
async def on_ready():
    print('online and ready to roll')


# On message event : to listen to messages typed by any user
@client.event
async def on_message(message):
    # to prevent the bot responding to its own text
    if message.author == client.user:
        return

    # React with am emoji if user types cool
    if message.content == 'sup':
        await message.add_reaction('\U0001F60E')

# To listen to edited messages
@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edited a message. \n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )

# To listen to deleted messages
@client.event
async def on_message_delete(message):
    await message.channel.send(
        f'{message.author} deleted a message.'
    )


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


# Run the client by passing the token
client.run(TOKEN)

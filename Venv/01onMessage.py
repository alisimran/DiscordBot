import discord
import random


#Using this client object to talk to discord api or socket
client = discord.Client()

# Any event in discord can be listened

# called whenever the bot is online or logged in
@client.event
async def on_ready():
    print('Bot is now online and ready to roll')
    print(f'{client.user.name} has rolled into this Server!!')

@client.event
async def on_member_join(ctx, member):
    await ctx.send(f'{member} has entered the arena. Watch out.')

# On message event : to listen to messages typed by any user
@client.event
async def on_message(message):
    # to prevent the bot responding to its own text
    if message.author == client.user:
        return
    
    if message.content == 'hello':
        # bot responding in the same channel the msg is coming from
        await message.channel.send('Welcome to the DB!')

    office = [
        'Make friends first, make sales second, make love third. In no particular order.',
        'I… Declare…. Bankruptcy!',
        'It’s Britney, bitch.',
        'I love inside jokes. I hope to be a part of one someday.',
        'You know what they say. Fool me once, strike one, but fool me twice...strike three.',
        'Im not superstitious, but I am a little stitious.',
        "Sometimes I'll start a sentence and I don't even know where its going. I just hope I find it along the way.",
        "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.",
        "That’s what she said.",
        "And I knew exactly what to do. But in a much more real sense, I had no idea what to do.",
        "Pizza: the great equalizer.",
        "It’s never too early for ice cream."
    ]
    if message.content == "michael":
        reply = random.choice(office)
        await message.channel.send(reply)

    


# Run the client by passing the token
client.run('ODk5NjMwMTYyNTk1OTcxMTAy.YW1j4Q.5oRQSJv4kD8HiYPa46OQm7bdtMs')


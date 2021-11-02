import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

extensions = ['01onMessage']

@client.event
async def on_ready():
    print('Bot is now online and ready to roll')
    print(f'{client.user.name} has rolled into this Server!!')

# Adding the clog to the main file

@client.command()
async def load(extension):
    if __name__ == '__main__':
        for extension in extensions:
            try:
                client.load_extension(extension)
            except Exception as error:
                print('{} cannot be loaded. [{}]'.format(extension, error))




# Run the client by passing the token
client.run('ODk5NjMwMTYyNTk1OTcxMTAy.YW1j4Q.5oRQSJv4kD8HiYPa46OQm7bdtMs')

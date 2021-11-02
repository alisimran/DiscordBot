import discord




"""
client = discord.Client()
# To listen to deleted messages
@client.event
async def on_message_delete(message):
    await message.channel.send(
        f'{message.author} deleted a message.'
    )
"""

# Alternative: to create custom class
class myclient(discord.Client):
    def __init__(self, *args, **kwargs):
        # super means referenced to the parent class
        super().__init__( *args, **kwargs)
        self.target_message_id = 900343833525620736 

    async def on_ready(self):
        print('On and ready to roll..')
    
    async def on_raw_reaction_add(self, payload):
        # if user adds an emoji, give them a role. If it deletes, remove the role
        if payload.message_id != self.target_message_id:
            return
        # Guild means the discord server
        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == '👍':
            role = discord.utils.get(guild.roles, name='dorky person')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='choco person')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🍴':
            role = discord.utils.get(guild.roles, name='food person')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        # if user remove an emoji, remove their role a role. 
        if payload.message_id != self.target_message_id:
            return
        # Guild means the discord server
        guild = client.get_guild(payload.guild_id)
        # to get a reference to the member removing the emoji
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '👍':
            role = discord.utils.get(guild.roles, name='dorky person')
            await member.remove_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='choco person')
            await member.remove_roles(role)
        elif payload.emoji.name == '🍴':
            role = discord.utils.get(guild.roles, name='food person')
            await member.remove_roles(role)
        


# Intents are group of events(member events)

intents = discord.Intents.default()
intents.members = True



# passing intents so that the original intents are our custom intents
client = myclient(intents=intents)

# Run the client by passing the token
client.run('ODk5NjMwMTYyNTk1OTcxMTAy.YW1j4Q.5oRQSJv4kD8HiYPa46OQm7bdtMs')


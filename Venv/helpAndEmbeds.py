# help commands
import discord
from discord.ext import commands

# this is a subclass of discord.Client
# anything that we did before can be done with this too
# command prefix : what message content should contain intitially


bot = commands.Bot(command_prefix='|')
# To remove a default command and rewrite it
bot.remove_command('help')

@bot.command()
async def help(ctx):
    # Embeds are fancy color output we see 
    embed = discord.Embed(
        title='Bot Commands',
        description='Welcome to the help section. Here are all the commands for the game!',
        color=discord.Colour.dark_magenta()
    )

    # to imbed an image: thumbnail
    embed.set_thumbnail(url='https://pinkpanther.fandom.com/wiki/Pink_Panther_(character)')
    embed.add_field(
        name='|help',
        value='List of all of the commands',
        inline=False
    )
    embed.add_field(
        name='|punch',
        value='This man punches another player',
        inline=False
    )
    embed.add_field(
        name='|round_kick',
        value='Kicks multiple persons',
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command()
async def round_kick(ctx, *args):
    names = ', '.join(args)
    await ctx.send(f'{ctx.author} Punched {names}')




@bot.command()
async def punch(ctx, arg):
    """
    This man punches another player
    """
    await ctx.send(f'{ctx.author} Punched {arg}')




bot.run('ODk5NjMwMTYyNTk1OTcxMTAy.YW1j4Q.5oRQSJv4kD8HiYPa46OQm7bdtMs')
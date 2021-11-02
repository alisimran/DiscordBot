from discord.ext import commands

# this is a subclass of discord.Client
# anything that we did before can be done with this too
# command prefix : what message content should contain intitially

TOKEN = ''

bot = commands.Bot(command_prefix='|')

@bot.command()
async def round_kick(ctx, *args):
    """
    |round_punch Justin mike kayla mikasg dga: print the user punched justin
    """
    names = ', '.join(args)
    await ctx.send(f'{ctx.author} Punched {names}')


@bot.command()
async def double_punch(ctx, arg1, arg2):
    """
    |double_punch Justin mike: print the user punched justin
    """
    await ctx.send(f'{ctx.author} Punched {arg1} and {arg2}')


@bot.command()
async def punch(ctx, arg):
    """
    |punch Justin: print the user punched justin
    """
    await ctx.send(f'{ctx.author} Punched {arg}')


# name of the func -> name of the command
@bot.command()
async def info(ctx):
    """
    ctx: context (info about how the command was executed)
    To invoke the command
    |info
    """
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

bot.run(TOKEN)

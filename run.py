import discord
from discord.ext import commands
import asyncio
from discord.utils import get

bot = commands.Bot()

@bot.event
async def on_ready():
    print('Logged in as', bot.user.name)
    print('------')

@bot.slash_command(name="create")
async def create(ctx):

    global channel2

    try:

        channelName = ctx.author.id
        user = await bot.fetch_user(channelName)

        category = discord.utils.get(ctx.guild.categories, name="━━━ VOCAL━━━")
        guild = bot.get_guild(918188038557954049)
        channel2 = await guild.create_voice_channel(f"Salon de {user}", category=category)
        channel1 = discord.utils.get(ctx.guild.channels, name=f"Salon de {user}")
        idChannel = channel1.id

        embed=discord.Embed(title=":white_check_mark:  | Successful channel creation!", description = "Your channel has been **successfully created.** Thank you for using our services ;)\n\n -><#{}>".format(idChannel), color=0x008000)

        await ctx.respond(embed = embed, ephemeral=True)

        await asyncio.sleep(30)

        if len(channel2.members) == 0:

            await channel2.delete()
            embedred=discord.Embed(title=":x:  | Channel Deleted!", description = "Your channel **has been deleted.** You did not join the channel within the time limit, so we have deleted it.", color=0xFF0000)

            await ctx.respond(embed = embedred, ephemeral=True)

    except Exception as e:

        print(e)
        await ctx.respond("T'es une merde, y'a une erreur par ta faute!", ephemeral=True)

@bot.event
async def on_voice_state_update(member, before, after):

    if len(channel2.members) == 0:

        await channel2.delete()



# RUN
bot.run("token")
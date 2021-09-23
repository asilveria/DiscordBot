#Bot main.py
import SQLdbconn
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#def main():
    #SQLdbconn.insertHelper(dbconn, "tyler","09/22/2021", "I'll take my goop on the side")
    #SQLdbconn.removeQuote(dbconn,3)

dbconn = SQLdbconn.fireUp()
print("successful connection...")
load_dotenv('ElmerInfo.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = discord.Client()
print("client initialized...")

# quote = SQLdbconn.returnQuoteBody(dbconn)
# print(quote)

#       0          1      2     3  
#([Primary Key][author][date][body])
bot = commands.Bot(command_prefix='!')

@bot.command()
async def quote(ctx):
    quote = SQLdbconn.returnQuoteBody(dbconn)
    await ctx.channel.send(quote[3])

# Next commands should be allowing the bot to add a new quote to the DB
    # It should snapshot the date added and have the author attached to the end of the command.
    #  Ex) !addquote I'm tired of all this whataboutism - Brian
    
bot.run(TOKEN)


#main()
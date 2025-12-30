import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import fetch_data as f

def main():
    load_dotenv()
    token = os.getenv('DISCORD_ENV')

    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    intents = discord.Intents.default()

    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f"We are ready to go in, {bot.user.name}!")

    #!dt
    @bot.command()
    async def dt(ctx, *, pokemon):

        pokemon = pokemon.strip()
        pokemon = pokemon.replace(" ", "-")

        if pokemon.split("-")[0] == "mega":
            pokemon = pokemon.split("-")[1] + "-" + pokemon.split("-")[0]
        
        await ctx.send(f.FetchData().dt(pokemon))

    bot.run(token, log_handler=handler, log_level=logging.DEBUG)

if __name__ == '__main__':
    main()
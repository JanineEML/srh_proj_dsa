import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import funktionen
import charakterdaten

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

charaktere = charakterdaten.lade_charakterwerte()

@bot.event
async def on_ready():
    print(f'{bot.user} ist online!')

@bot.command()
async def probe(ctx, name: str, talent: str):
    name = name.lower()
    talent = talent.capitalize()

    if name not in charaktere:
        await ctx.send(f"Charakter '{name}' nicht gefunden.")
        return

    if talent not in charaktere[name]:
        await ctx.send(f"Talent '{talent}' nicht gefunden.")
        return

    wert = charaktere[name][talent]
    ergebnis = funktionen.wuerfelprobe(talent, wert)
    await ctx.send(f"{name.capitalize()} würfelt: {ergebnis}")

bot.run(TOKEN)

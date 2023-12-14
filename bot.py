import discord
from discord import Embed, Colour
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot_id = 'token'
bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)


@bot.event
async def on_ready():
    print(f'Olá, eu sou {str(bot.user)[:-5]}!\nEstou pronto para começar.')

@bot.event
async def on_member_join(member):
    canal = bot.get_channel(12345678) #id canal
    embed = discord.Embed(title=f'{member.user} acaba de entrar no servidor!', color=0xff7729, description='Seja bem-vindo(a)')
    await canal.send(embed=embed)

forbidden_words = ['teste']

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    text = message.content
    text = text.lower()
    words = text.split()
    text = ''.join(words)
    if message.author == bot.user:
        return
    else:
        if 'eibot' in text:
            await message.channel.send(f'''Olá, {str(message.author)[:-5]}!\nComo posso ajudar?\n \ncomando: >>ajuda''')
        else:
            for i in forbidden_words:
                for p in words:
                    if i == p:
                        await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários!')
                        await message.delete()

@bot.command(name= 'info')
async def send_help(ctx):
    title = ':bell: Meus Comandos'
    cor = 'eb6e34'
    colour = Colour(value=int(cor, 16))
    description = '''
    **!info**
    Lista todos os comandos.
    
    **!aviso**
    Cria uma embed com os parametros;
    <"cor hexadecimal"><"título"><"descrição">
    '''
    embed = Embed(title=title, description=description, colour=colour)
    await ctx.send(embed=embed)

@bot.command(name= 'aviso')
async def send_notice(ctx, cor, title, description):
    colour = Colour(value=int(cor, 16))
    embed = Embed(title=title, description=description, colour=colour)
    embed.set_footer(text=f"\nEnviado por: {str(ctx.author)[:-5]}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

bot.run(bot_id)

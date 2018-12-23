import discord,settings,random

client = discord.Client()

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    if message.content.startswith('!z'):
        msg = 'La Cazeria de Ganzitos ha comenzado, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg, tts=True)
@client.command
async def hola():
    p_return = [
        'hola {o.author.mention}',
        'Tiempo sin verte {o.author.mention}',
    ]
    await client.say(random.choice(p_return))
@client.event
async def on_ready():
    print("Soul v{} is On".format(settings.version))


client.run(settings.bot_token)

import discord
import asyncio
import os
from discord.ext import commands
bot = commands.Bot(command_prefix = '!!')
bot.remove_command('help')
#=====================================================================================Commands=====================================================================================
@bot.command(aliases=['si', 'серверинфо'])
async def serverinfo(ctx):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    region = guild.region
    author = ctx.message.author
    avatar = author.avatar_url
    name = guild.name
    owner = guild.owner
    icon = guild.icon_url
    gicon = guild.icon
    texchannel = guild.text_channels
    voichannel = guild.voice_channels
    channels = len(texchannel) + len(voichannel)
    users = guild.member_count
    role = guild.roles
    roles = len(role)
    if gicon == None:
        vicon = 'Отсутствует'
    else:
        vicon = '⠀'
    if vicon == '⠀':
        embed = discord.Embed(title='Инфо о сервере',colour=discord.Colour.gold())
        embed.add_field(name = 'Название сервера:', value = name)
        embed.add_field(name = 'Владелец сервера:', value = owner)
        embed.add_field(name = 'Иконка сервера:', value  = vicon)
        embed.add_field(name = 'Регион:', value  = region)
        embed.add_field(name = 'Каналов:', value = channels)
        embed.add_field(name = 'Участников:', value = users)
        embed.add_field(name = 'Ролей:', value = roles)
        embed.set_thumbnail(url = icon)
        embed.set_footer(text = author, icon_url = avatar)
    else:
        embed = discord.Embed(title='Инфо о сервере',colour=discord.Colour.gold())
        embed.add_field(name = 'Название сервера:', value = name)
        embed.add_field(name = 'Владелец сервера:', value = owner)
        embed.add_field(name = 'Иконка сервера:', value  = vicon)
        embed.add_field(name = 'Регион:', value  = region)
        embed.add_field(name = 'Каналов:', value = channels)
        embed.add_field(name = 'Участников:', value = users)
        embed.add_field(name = 'Ролей:', value = roles)
        embed.set_footer(text = author, icon_url = avatar)
    await ctx.send(embed = embed)
    print(f'{guild} -> Участник {author} использовал команду serverinfo')
    await lc.send(f'{guild} -> Участник {author} использовал команду serverinfo')
@bot.command(aliases=['юсеринфо', 'ui'])
async def userinfo(ctx, member: discord.Member = None):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    author = ctx.message.author
    author_url = ctx.message.author.avatar_url
    if not member:
        name = ctx.message.author.name
        avatar = ctx.message.author.avatar
        id = ctx.message.author.id
        time = ctx.message.author.created_at
        if avatar == None:
            vicon = 'Отсутствует'
        else:
            vicon = '⠀'
        if vicon == '⠀':
            embed = discord.Embed(title='Инфо о пользователе',colour=discord.Colour.gold())
            embed.add_field(name = 'Никнейм:', value = name)
            embed.add_field(name = 'Аватар:', value = vicon)
            embed.add_field(name = 'Id:', value  = id, inline = False)
            embed.add_field(name = 'Время создания аккаунта:', value = time)
            embed.set_thumbnail(url = avatar_url)
            embed.set_footer(text = author, icon_url = author_url)
        else:
            embed = discord.Embed(title='Инфо о пользователе',colour=discord.Colour.gold())
            embed.add_field(name = 'Никнейм:', value = name)
            embed.add_field(name = 'Аватар:', value = vicon)
            embed.add_field(name = 'Id:', value  = id, inline = False)
            embed.add_field(name = 'Время создания аккаунта:', value = time)
            embed.set_footer(text = author, icon_url = author_url)
        await ctx.send(embed = embed)
        print(f'{guild} -> Участник {author} использовал команду userinfo')
        await lc.send(f'{guild} -> Участник {author} использовал команду userinfo')
    else:
        name = member.name
        avatar = member.avatar
        avatar_url = member.avatar_url
        id = member.id
        time = member.created_at
        if avatar == None:
            vicon = 'Отсутствует'
        else:
            vicon = '⠀'
        if vicon == '⠀':
            embed = discord.Embed(title='Инфо о пользователе',colour=discord.Colour.gold())
            embed.add_field(name = 'Никнейм:', value = name)
            embed.add_field(name = 'Аватар:', value = vicon)
            embed.add_field(name = 'Id:', value  = id, inline = False)
            embed.add_field(name = 'Время создания аккаунта:', value = time)
            embed.set_thumbnail(url = avatar_url)
            embed.set_footer(text = author, icon_url = author_url)
        else:
            embed = discord.Embed(title='Инфо о пользователе',colour=discord.Colour.gold())
            embed.add_field(name = 'Никнейм:', value = name)
            embed.add_field(name = 'Аватар:', value = vicon)
            embed.add_field(name = 'Id:', value  = id, inline = False)
            embed.add_field(name = 'Время создания аккаунта:', value = time)
            embed.set_footer(text = author, icon_url = author_url)
        await ctx.send(embed = embed)
        print(f'{guild} -> Участник {author} использовал команду userinfo')
        await lc.send(f'{guild} -> Участник {author} использовал команду userinfo')
@bot.command(aliases=['m', 'м', 'мьют'])
@commands.has_permissions(administrator = True)
async def mute(ctx, member:discord.Member = None, time: int = None, *, reason = None):
    url = 'https://s7.gifyu.com/images/mute-2.gif'
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    role = guild.get_role(737056764050145360)
    author = ctx.message.author
    moder = ctx.message.author.mention
    channel = guild.get_channel(738127371642732744)
    if not member:
        await ctx.send('Вы не указали пользователя')
    else:
        if not time:
            await ctx.send('Вы не указали срок действия мута')
        else:
            if not reason:
                reason = 'Не указана'
                muted = member.mention
                embed = discord.Embed(title = 'Мут', colour = discord.Colour.red())
                embed.add_field(name = 'Модератор:', value = moder, inline = False)
                embed.add_field(name = 'Нарушитель:', value = muted, inline = False)
                embed.add_field(name = 'Время:', value = f'{time} минут', inline = False)
                embed.add_field(name = 'Причина:', value = reason, inline = False)
                embed.set_thumbnail(url = url)
                await member.add_roles(role)
                await channel.send(embed = embed)
                print(f'{guild} -> Модератор {author} выдал мут {member} на {time} минут по причине: {reason}')
                await lc.send(f'{guild} -> Модератор {author} выдал мут {member} на {time} минут по причине: {reason}')
                await asyncio.sleep(time * 60)
                await member.remove_roles(role)
            else:
                muted = member.mention
                embed = discord.Embed(title = 'Мут', colour = discord.Colour.red())
                embed.add_field(name = 'Модератор:', value = moder, inline = False)
                embed.add_field(name = 'Нарушитель:', value = muted, inline = False)
                embed.add_field(name = 'Время:', value = f'{time} минут', inline = False)
                embed.add_field(name = 'Причина:', value = reason, inline = False)
                embed.set_thumbnail(url = url)
                await member.add_roles(role)
                await channel.send(embed = embed)
                print(f'{guild} -> Модератор {author} выдал мут {member} на {time} минут по причине: {reason}')
                await lc.send(f'{guild} -> Модератор {author} выдал мут {member} на {time} минут по причине: {reason}')
                await asyncio.sleep(time * 60)
                await member.remove_roles(role)
@bot.command(aliases=['um', 'р', 'размут'])
@commands.has_permissions(administrator = True)
async def unmute(ctx, member:discord.Member = None):
    url = 'https://s7.gifyu.com/images/unmute.gif'
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    role = guild.get_role(737056764050145360)
    moder = ctx.message.author.mention
    muted = member.mention
    author = ctx.message.author
    channel = guild.get_channel(738127371642732744)
    if not member:
        await ctx.send('Вы не указали пользователя')
    else:
        embed = discord.Embed(title = 'Размут', colour = discord.Colour.green())
        embed.add_field(name = 'Модератор:', value = moder, inline = False)
        embed.add_field(name = 'Нарушитель:', value = muted, inline = False)
        embed.set_thumbnail(url = url)
        await member.remove_roles(role)
        print(f'{guild} -> Модератор {author} снял мут {member}')
        await lc.send(f'{guild} -> Модератор {author} снял мут {member}')
        await channel.send(embed = embed)
@bot.command(aliases=['k', 'кик', 'к'])
@commands.has_permissions(administrator = True)
async def kick(ctx, member:discord.Member = None, *, reason = None):
    url = 'https://s7.gifyu.com/images/kick93a68b4b8d883629.gif'
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    moder = ctx.message.author.mention
    author = ctx.message.author
    channel = guild.get_channel(738127371642732744)
    if not member:
        await ctx.send('Вы не указали пользователя')
    else:
        if not reason:
            reason = 'Не указана'
            kicked = member.mention
            embed = discord.Embed(title = 'Кик', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = kicked, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Кик', colour = discord.Colour.red())
            embed1.description = f'Вас кикнули с сервера {guild}'
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.kick()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print(f'{guild} -> Модератор {author} кикнул {member} по причине: {reason}')
            await lc.send(f'{guild} -> Модератор {author} кикнул {member} по причине: {reason}')
        else:
            kicked = member.mention
            embed = discord.Embed(title = 'Кик', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = kicked, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Кик', colour = discord.Colour.red())
            embed1.description = f'Вас кикнули с сервера {guild}'
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.kick()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print(f'{guild} -> Модератор {author} кикнул {member} по причине: {reason}')
            await lc.send(f'{guild} -> Модератор {author} кикнул {member} по причине: {reason}')
@bot.command(aliases=['b', 'бан', 'б'])
@commands.has_permissions(administrator = True)
async def ban(ctx, member:discord.Member = None, *, reason = None):
    url = 'https://s7.gifyu.com/images/ban.gif'
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    moder = ctx.message.author.mention
    author = ctx.message.author
    channel = guild.get_channel(738127371642732744)
    if not member:
        await ctx.send('Вы не указали пользователя')
    else:
        if not reason:
            reason = 'Не указана'
            banned = member.mention
            embed = discord.Embed(title = 'Бан', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = banned, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Бан', colour = discord.Colour.red())
            embed1.description = f'Вас забанили на сервере {guild}'
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.ban()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print(f'{guild} -> Модератор {author} забанил {member} по причине: {reason}')
            await lc.send(f'{guild} -> Модератор {author} забанил {member} по причине: {reason}')
        else:
            banned = member.mention
            embed = discord.Embed(title = 'Бан', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = banned, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Бан', colour = discord.Colour.red())
            embed1.description = f'Вас забанили на сервере {guild}'
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.ban()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print(f'{guild} -> Модератор {author} забанил {member} по причине: {reason}')
            await lc.send(f'{guild} -> Модератор {author} забанил {member} по причине: {reason}')
@bot.command(aliases=['c', 'очистить'])
@commands.has_permissions(administrator = True)
async  def clear(ctx, count = 10):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    deleted = await ctx.message.channel.purge(limit = count + 1)
    author = ctx.message.author
    channel = ctx.message.channel
    guild = ctx.message.guild
    print(f'{guild} -> Модератор {author} удалил {count} сообщений в канале {channel}')
    await lc.send(f'{guild} -> Модератор {author} удалил {count} сообщений в канале {channel}')
@bot.command(aliases=['i', 'инвайт', 'пригласить'])
async def invite(ctx):
        lg = bot.get_guild(739951510892314654)
        lc = lg.get_channel(739952498797838366)
        guild = ctx.message.guild
        author = ctx.message.author
        avatar = author.avatar_url
        embed = discord.Embed(title = '**Denisska008**', colour = discord.Colour.gold())
        embed.description = '[Группа в Discord](https://discord.gg/gFwZF2H)\n[Пригласить Бота](https://discord.com/oauth2/authorize?client_id=681951903130976382&permissions=8&scope=bot)'
        embed.add_field(name = '👥 | Пользователей', value = f'``{len(bot.users)}``')
        embed.add_field(name = '🌐 | Серверов', value = f'``{len(bot.guilds)}``')
        embed.set_footer(text = author, icon_url = avatar)
        await ctx.send(embed = embed)
        print(f'{guild} -> Участник {author} использовал команду invite')
        await lc.send(f'{guild}  -> Участник {author} использовал команду invite')
@bot.command(aliases=['h', 'хелп', 'помощь'])
async def help(ctx):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    author = ctx.message.author
    avatar = author.avatar_url
    embed = discord.Embed(title = 'Помощь с командами', colour = discord.Colour.gold())
    embed.add_field(name = 'Пользовательские команды:', value = '___help | userinfo | invite___', inline = False)
    embed.add_field(name = 'Команды для администраторов', value = '___mute | unmute | kick | ban | clear___', inline = False)
    embed.set_footer(text = author, icon_url = avatar)
    await ctx.send(embed = embed)
    print(f'{guild} -> Участник {author} использовал команду help')
    await lc.send(f'{guild}  -> Участник {author} использовал команду help')
#=====================================================================================Events=====================================================================================
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует.**', colour = discord.Colour.red()))
@bot.event
async def on_ready():
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    name = bot.user
    activity = discord.Activity(name="🔥24/7🔥", type = discord.ActivityType.watching)
    await lc.send(f'Бот авторизовался как {name}')
    print(f'Бот авторизовался как {name}')
    await bot.change_presence(status=discord.Status.dnd, activity = activity)
@bot.event
async def on_member_join(member):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = member.guild
    name = guild.name
    user = member.name
    role = guild.get_role(745333239853482104)
    channel = guild.get_channel(738127371642732744)
    embed = discord.Embed(title=name,colour=discord.Colour.green())
    embed.description = f'```yaml\n{user}  присоединился к нам```'
    embed1 = discord.Embed(title="Welcome",colour=discord.Colour.green())
    embed1.description = '```yaml\nПривет!\nДобро пожаловать на наш сервер!\nНадеюсь тебе тут понравится.\nЕсли заблудишься пиши !!help, кстати у нас все команды пишутся с !!\nДля получения роли зайди в канал получения роли\nУдачи тебе🙂```'
    await channel.send(embed = embed)
    await member.send(embed = embed1)
    await member.add_roles(role)
    print(f'{name} -> {user} вступил на сервер')
    print(f'{name} -> Участнику {user} успешно выдана роль {role}')
    await lc.send(f'{name} -> {user} вступил на сервер')
    await lc.send(f'{name} -> Участнику {user} успешно выдана роль {role}')
@bot.event
async def on_member_remove(member):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    user = member.name
    guild = member.guild
    name = guild.name
    channel = guild.get_channel(738127371642732744)
    embed = discord.Embed(title=name,colour=discord.Colour.red())
    embed.description = f'```yaml\n{user} покинул нас```'
    await channel.send(embed = embed)
    print(f'{name} -> {user} покинул сервер')
    await lc.send(f'{name} -> {user} покинул сервер')
@bot.event
async def on_raw_reaction_add(reaction: discord.RawReactionActionEvent):
    if not reaction.message_id == 746320495615410189:  # ID сообщения на которое нужно ставить реакции
        return
    if not reaction.emoji.name == "✅":  # или payload.emoji.name == "✔" для unicode-эмодзей
        return
    if member := reaction.member:
        await member.add_roles(member.guild.get_role(746051787152425083))
        await member.remove_roles(member.guild.get_role(745333239853482104))

token = os.environ.get('BOT_TOKEN') 
bot.run(str(token))

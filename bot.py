import discord
import asyncio
import os
from discord.ext import commands
bot = commands.Bot(command_prefix = '!!')
bot.remove_command('help')
#=====================================================================================Commands=====================================================================================
@bot.command()
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
    print('%(guild)s -> Участник %(author)s использовал команду serverinfo' %{'guild': guild,'author': author})
    await lc.send('%(guild)s -> Участник %(author)s использовал команду serverinfo' %{'guild': guild,'author': author})
@bot.command(aliases=['u', 'ui'])
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
        print('%(guild)s -> Участник %(author)s использовал команду userinfo' %{'guild': guild,'author': author})
        await lc.send('%(guild)s -> Участник %(author)s использовал команду userinfo' %{'guild': guild,'author': author})
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
        print('%(guild)s -> Участник %(author)s использовал команду userinfo' %{'guild': guild,'author': author})
        await lc.send('%(guild)s -> Участник %(author)s использовал команду userinfo' %{'guild': guild,'author': author})
@bot.command()
@commands.has_permissions(administrator = True)
async def mute(ctx: commands.Context, member:discord.Member = None, time: int = None, *, reason = None):
    url = 'https://s7.gifyu.com/images/mute-2.gif'
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    role = guild.get_role(737056764050145360)
    author = ctx.message.author
    moder = ctx.message.author.mention
    muted = member.mention
    channel = guild.get_channel(738127371642732744)
    if not member:
        await ctx.send('Вы не указали пользователя')
    else:
        if not time:
            await ctx.send('Вы не указали срок действия мута')
        else:
            if not reason:
                reason = 'Не указана'
                embed = discord.Embed(title = 'Мут', colour = discord.Colour.red())
                embed.add_field(name = 'Модератор:', value = moder, inline = False)
                embed.add_field(name = 'Нарушитель:', value = muted, inline = False)
                embed.add_field(name = 'Время:', value = '%(time)s минут' %{'time': time}, inline = False)
                embed.add_field(name = 'Причина:', value = reason, inline = False)
                embed.set_thumbnail(url = url)
                await member.add_roles(role)
                await channel.send(embed = embed)
                print('%(guild)s -> Модератор %(author)s выдал мут %(muted)s на %(time)s минут по причине: %(reason)s' %{'guild': guild,'author': author, 'muted': member, 'time': time, 'reason': reason})
                await lc.send('%(guild)s -> Модератор %(author)s выдал мут %(muted)s на %(time)s минут по причине: %(reason)s' %{'guild': guild,'author': author, 'muted': member, 'time': time, 'reason': reason})
                await asyncio.sleep(time * 60)
                await member.remove_roles(role)
            else:
                embed = discord.Embed(title = 'Мут', colour = discord.Colour.red())
                embed.add_field(name = 'Модератор:', value = moder, inline = False)
                embed.add_field(name = 'Нарушитель:', value = muted, inline = False)
                embed.add_field(name = 'Время:', value = '%(time)s минут' %{'time': time}, inline = False)
                embed.add_field(name = 'Причина:', value = reason, inline = False)
                embed.set_thumbnail(url = url)
                await member.add_roles(role)
                await channel.send(embed = embed)
                print('%(guild)s -> Модератор %(author)s выдал мут %(muted)s на %(time)s минут по причине: %(reason)s' %{'guild': guild,'author': author, 'muted': member, 'time': time, 'reason': reason})
                await lc.send('%(guild)s -> Модератор %(author)s выдал мут %(muted)s на %(time)s минут по причине: %(reason)s' %{'guild': guild,'author': author, 'muted': member, 'time': time, 'reason': reason})
                await asyncio.sleep(time * 60)
                await member.remove_roles(role)
@bot.command()
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
        print('%(guild)s -> Модератор %(author)s снял мут %(muted)s' %{'guild': guild,'author': author, 'muted': member})
        await lc.send('%(guild)s -> Модератор %(author)s снял мут %(muted)s' %{'guild': guild,'author': author, 'muted': member})
        await channel.send(embed = embed)
@bot.command()
@commands.has_permissions(administrator = True)
async def kick(ctx, member:discord.Member = None, *, reason = None):
    url = 'https://s7.gifyu.com/images/kick93a68b4b8d883629.gif'
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    moder = ctx.message.author.mention
    kicked = member.mention
    author = ctx.message.author
    channel = guild.get_channel(738127371642732744)
    if not member:
        await ctx.send('Вы не указали пользователя')
    else:
        if not reason:
            reason = 'Не указана'
            embed = discord.Embed(title = 'Кик', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = kicked, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Кик', colour = discord.Colour.red())
            embed1.description = 'Вас кикнули с сервера %(guild)s' %{'guild': guild}
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.kick()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print('%(guild)s -> Модератор %(author)s кикнул %(kick)s по причине: %(reason)s' %{'guild': guild,'author': author, 'kick': member, 'reason': reason})
            await lc.send('%(guild)s -> Модератор %(author)s кикнул %(kick)s по причине: %(reason)s' %{'guild': guild,'author': author, 'kick': member, 'reason': reason})
        else:
            embed = discord.Embed(title = 'Кик', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = kicked, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Кик', colour = discord.Colour.red())
            embed1.description = 'Вас кикнули с сервера %(guild)s' %{'guild': guild}
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.kick()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print('%(guild)s -> Модератор %(author)s кикнул %(kick)s по причине: %(reason)s' %{'guild': guild,'author': author, 'kick': member, 'reason': reason})
            await lc.send('%(guild)s -> Модератор %(author)s кикнул %(kick)s по причине: %(reason)s' %{'guild': guild,'author': author, 'kick': member, 'reason': reason})
@bot.command()
@commands.has_permissions(administrator = True)
async def ban(ctx, member:discord.Member = None, *, reason = None):
    url = 'https://s7.gifyu.com/images/ban.gif'
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    moder = ctx.message.author.mention
    banned = member.mention
    author = ctx.message.author
    channel = guild.get_channel(738127371642732744)
    if not member:
        await ctx.send('Вы не указали пользователя')
    else:
        if not reason:
            reason = 'Не указана'
            embed = discord.Embed(title = 'Бан', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = banned, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Бан', colour = discord.Colour.red())
            embed1.description = 'Вас забанили на сервере %(guild)s' %{'guild': guild}
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.ban()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print('%(guild)s -> Модератор %(author)s забанил %(ban)s по причине: %(reason)s' %{'guild': guild,'author': author, 'ban': member, 'reason': reason})
            await lc.send('%(guild)s -> Модератор %(author)s забанил %(ban)s по причине: %(reason)s' %{'guild': guild,'author': author, 'ban': member, 'reason': reason})
        else:
            embed = discord.Embed(title = 'Бан', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = banned, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Бан', colour = discord.Colour.red())
            embed1.description = 'Вас забанили на сервере %(guild)s' %{'guild': guild}
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.ban()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print('%(guild)s -> Модератор %(author)s забанил %(ban)s по причине: %(reason)s' %{'guild': guild,'author': author, 'ban': member, 'reason': reason})
            await lc.send('%(guild)s -> Модератор %(author)s забанил %(ban)s по причине: %(reason)s' %{'guild': guild,'author': author, 'ban': member, 'reason': reason})
@bot.command()
@commands.has_permissions(administrator = True)
async  def clear(ctx, count = 10):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    deleted = await ctx.message.channel.purge(limit = count + 1)
    author = ctx.message.author
    channel = ctx.message.channel
    guild = ctx.message.guild
    print('%(guild)s -> Модератор %(author)s удалил %(count)s сообщений в канале %(channel)s' %{'guild': guild,'author': author, 'count': count, 'channel': channel})
    await lc.send('%(guild)s -> Модератор %(author)s удалил %(count)s сообщений в канале %(channel)s' %{'guild': guild,'author': author, 'count': count, 'channel': channel})
@bot.command()
async def invite(ctx):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    author = ctx.message.author
    embed = discord.Embed(title = 'Invite', colour = discord.Colour.gold())
    embed.description = '[Группа в Discord](https://discord.gg/gFwZF2H)'
    await ctx.send(embed = embed)
    print('%(guild)s -> Участник %(author)s использовал команду invite' %{'guild': guild,'author': author})
    await lc.send('%(guild)s -> Участник %(author)s использовал команду invite' %{'guild': guild,'author': author})
@bot.command()
async def help(ctx):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    author = ctx.message.author
    avatar = ctx.message.author.avatar_url
    embed = discord.Embed(title = 'Помощь с командами', colour = discord.Colour.gold())
    embed.add_field(name = 'Пользовательские команды:', value = '___help | userinfo | info | invite___', inline = False)
    embed.add_field(name = 'Команды Администратора', value = '___mute | unmute | kick | ban | clear___', inline = False)
    embed.set_footer(text = author, icon_url = avatar)
    await ctx.send(embed = embed)
    print('%(guild)s -> Участник %(author)s использовал команду help' %{'guild': guild,'author': author})
    await lc.send('%(guild)s -> Участник %(author)s использовал команду help' %{'guild': guild,'author': author})
@bot.command()
async def b(ctx):
    url = 'https://s7.gifyu.com/images/ban.gif'
    embed = discord.Embed(title = 'Бан', colour = discord.Colour.red())
    embed.add_field(name = 'Модератор:', value = 'Denisska008', inline = False)
    embed.add_field(name = 'Нарушитель:', value = 'Denisska008', inline = False)
    embed.add_field(name = 'Причина:', value = 'Тест', inline = False)
    embed.set_thumbnail(url = url)
    await ctx.send(embed = embed)
@bot.command()
async def m(ctx):
    url = 'https://s7.gifyu.com/images/mute-2.gif'
    embed = discord.Embed(title = 'Мут', colour = discord.Colour.red())
    embed.add_field(name = 'Модератор:', value = 'Denisska008', inline = False)
    embed.add_field(name = 'Нарушитель:', value = 'Denisska008', inline = False)
    embed.add_field(name = 'Время:', value = 'Навечно бл')
    embed.add_field(name = 'Причина:', value = 'Тест', inline = False)
    embed.set_thumbnail(url = url)
    await ctx.send(embed = embed)
@bot.command()
async def k(ctx):
    url = 'https://s7.gifyu.com/images/kick93a68b4b8d883629.gif'
    embed = discord.Embed(title = 'Кик', colour = discord.Colour.red())
    embed.add_field(name = 'Модератор:', value = 'Denisska008', inline = False)
    embed.add_field(name = 'Нарушитель:', value = 'Denisska008', inline = False)
    embed.add_field(name = 'Причина:', value = 'Тест', inline = False)
    embed.set_thumbnail(url = url)
    await ctx.send(embed = embed)
#=====================================================================================Events=====================================================================================
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует.**', colour = discord.Colour.red()))
@bot.event
async def on_ready():
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    owner = 'Denisska008'
    name = bot.user
    activity = discord.Activity(name="🔥24/7🔥", type = discord.ActivityType.watching)
    await lc.send('Бот авторизовался как %(name)s ' %{'name': name})
    print('Бот авторизовался как %(name)s ' %{'name': name})
    #await bot.change_presence(activity = discord.Game('Developer %(d)s' %{'d': owner}), status = discord.Status.dnd)
    #await bot.change_presence(activity = discord.Game('🔥24/7🔥'), status = discord.Status.dnd)
    await bot.change_presence(status=discord.Status.dnd, activity = activity)
@bot.event
async def on_member_join(member):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = member.guild
    name = guild.name
    user = member.name
    role = guild.get_role(729643408846749736)
    channel = guild.get_channel(738127371642732744)
    embed = discord.Embed(title=name,colour=discord.Colour.green())
    embed.description = '```yaml\n%(user)s присоединился к нам```' %{'user': user}
    embed1 = discord.Embed(title="Welcome",colour=discord.Colour.green())
    embed1.description = '```yaml\nПривет!\nДобро пожаловать на наш сервер!\nНадеюсь тебе тут понравится.\nЕсли заблудишься пиши !!help, кстати у нас все команды пишутся с !!\nДля получения роли зайди в канал получения роли\nУдачи тебе🙂```'
    await channel.send(embed = embed)
    await member.send(embed = embed1)
    await member.add_roles(role)
    print('%(name)s -> %(user)s вступил на сервер' %{'user': user, 'name': name})
    print('%(name)s -> Участнику %(user)s успешно выдана роль %(role)s' %{'user': user, 'role': role, 'name': name})
    await lc.send('%(name)s -> %(user)s вступил на сервер' %{'user': user, 'name': name})
    await lc.send('%(name)s -> Участнику %(user)s успешно выдана роль %(role)s' %{'user': user, 'role': role, 'name': name})
@bot.event
async def on_member_remove(member):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    user = member.name
    guild = member.guild
    name = guild.name
    channel = guild.get_channel(738127371642732744)
    embed = discord.Embed(title=name,colour=discord.Colour.red())
    embed.description = '```yaml\n%(user)s покинул нас```' %{'user': user}
    await channel.send(embed = embed)
    print('%(name)s -> %(user)s покинул сервер' %{'user': user, 'name': name})
    await lc.send('%(name)s -> %(user)s покинул сервер' %{'user': user, 'name': name})

token = os.environ.get('BOT_TOKEN') 
bot.run(str(token))

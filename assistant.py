# Work with Python 3.6
import discord
from os import system
import os

system("title "+"JammyBot Assistant")

TOKEN = os.environ["BOT_TOKEN"]

client = discord.Client()


@client.event
async def on_message(message):
    member = message.author
    # 봇이 본인의 메시지에는 대답을 하지 않음
    if (message.author == client.user):
        return


    if (message.content == '!인원수 업데이트'):
        usr = 0
        activeServers = client.servers
        for s in activeServers:
            usr += len(s.members)


        ppl = str(usr)
        gam = ppl + "명의 사용자들과 함께!ㅤㅤㅤㅤㅤㅤㅤ"
        await client.change_presence(game=discord.Game(name=gam))
        mtl = ":white_check_mark: 인원수가 업데이트 되었습니다."
        msg = "현재 인원은 **" + ppl + "** 명 입니다."
        await client.send_message(message.channel, embed=discord.Embed(title = mtl, description = msg, colour = 0x2EFEF7))


    if (message.content == '!인원수'):
        usr = 0
        activeServers = client.servers
        for s in activeServers:
            usr += len(s.members)


        ppl = str(usr)
        gam = ppl + "명의 사용자들과 함께!ㅤㅤㅤㅤㅤㅤㅤ"
        await client.change_presence(game=discord.Game(name=gam))
        mtl = "현재 인원은 **" + ppl + "** 명 입니다."
        await client.send_message(message.channel, embed=discord.Embed(title = mtl, colour = 0x2EFEF7))


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=""))
    print('다음 계정으로 로그인됨:')
    print(client.user.name)
    print(client.user.id)
    print('--- 동작 중 ---')
    usr = 0
    activeServers = client.servers
    for s in activeServers:
        usr += len(s.members)


    ppl = str(usr)
    gam = ppl + "명의 사용자들과 함께!ㅤㅤㅤㅤㅤㅤㅤ"
    await client.change_presence(game=discord.Game(name=gam))



client.run(TOKEN)

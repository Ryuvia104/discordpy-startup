import discord
import random
import os
import re
from datetime import datetime
from discord.ext import tasks
import time

from discord.ext import commands


# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NTUzMDgwNTA0NTQzMzQ2NzA2.XICmXA.IOVWOeToG3i4t3P-fffyIX3Dyqk'

# 接続に必要なオブジェクトを生成
client = discord.Client()


# テキストチャンネルの先頭につける文字
CHANNEL_PREFIX = "private_"
# botたちのロール名 (botはテキストチャンネルに参加していてほしい)
BOT_ROLE_NAME = "bot"




async def reply(message):
    coin = random.random()
    print(coin)
    if message.author.mention == '<@383478490907017216>':
        print('主人を感知しました。')
        if coin < 0.5:
            reply = f'{message.author.name}うるせぇﾁﾝｺｫｫｫｫｫｫｵｵｵｵｵ!!!!!!!!' # 返信メッセージの作成
            await message.channel.send(reply) # 返信メッセージを送信

        else:
            reply = f'{message.author.name}しばくぞｫｫｫｫｫｫｵｵｵｵｵ!!!!!!!!' # 返信メッセージの作成
            await message.channel.send(reply) # 返信メッセージを送信
    
    else:
        print(f'{message.author.name}に話しかけられました。')
        if coin > 0.8:
            reply = f'{message.author.name}の乳のサイズを教えてくれてもいいわん？' # 返信メッセージの作成
            await message.channel.send(reply) # 返信メッセージを送信
        
        elif coin < 0.2:
            reply = f'え、だっる…' # 返信メッセージの作成
            await message.channel.send(reply) # 返信メッセージを送信

        else:
            reply = f'{message.author.name}わんわん！' # 返信メッセージの作成
            await message.channel.send(reply) # 返信メッセージを送

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.content.startswith('今いるVCに誰がいるの？'):
        try:
            print('VCのコマンドを感知しました')
            name = f'(member.name for member in message.author.voice.channel.members)'
            VC_channel_name = (message.author.voice.channel)
            print(name)
            print(VC_channel_name)
            print(message.author.voice.channel.members)
            await message.channel.send(f'{VC_channel_name}には{name}がいるわん！')

        except AttributeError:
            print('発言者のVCチャンネルが確認できません！')
            await message.channel.send('お前どこにおんの？')
        
    # 「/neko」と発言したら「にゃーん」が返る処理
    elif message.content == '乳のサイズ教えてくれませんか？':
        coin = random.random()
        print(coin)
        print(f'{message.author.name}がセクハラしています')
        if coin < 0.8:
            await message.channel.send('すーぐ乳のサイズ知ろうとするんだから…')

        else:
            print('ドン引きし始めました')
            await message.channel.send('え？')
            time.sleep(2)
            await message.channel.send('きっしょ…')
            time.sleep(5)
            await message.channel.send(f'{message.author.name}がなんか段々気持ち悪く感じてきたわん…')
            time.sleep(6)
            await message.channel.send('それリアルでやってたらもっときしょいけど大丈夫？人狼でやってるだけだよね？')
    

    elif message.content == "DMを送ってくれませんか？":
        # ダイレクトメッセージ送信
        print('DMを送ります。')
        dm = await message.author.create_dm()
        await dm.send('きんたますごいよおおお！！！')

    elif message.content == 'やりたい':
        print('やりたいらしいです')
        await message.channel.send('https://tinder.com/?lang=ja')

    elif message.content == 'ナス':
        print('ナスを感知しました')
        await message.channel.send('は？')

    elif message.content == 'は？':
        print('きれます')
        await message.channel.send('何？')  

    elif message.content == 'してない':
        print('反抗します')
        time.sleep(2)
        await message.channel.send('してたやろお前ふざけんな')  

    elif message.content == '去勢してもらってもいい？':
        coin = random.random()
        print(coin)
        print(f'{message.author.name}がネスのちんこを取ろうとしてます')
        if coin < 0.7:
            await message.channel.send('ネスの金玉は取れませんでしたわん')

        else:
            print('金玉とれました')
            await message.channel.send('やったあ！')
            time.sleep(2)
            await message.channel.send('ネスの金玉がとれたわん！')
            time.sleep(5)
            await message.channel.send('これでネスはメスになったのだわん！')
            time.sleep(6)
            await message.channel.send('しらんけど')

    elif message.content == '金玉':
        print('金玉に反応しました')
        time.sleep(30)
        await message.channel.send('しばきころすぞ') 

    elif message.content == '勝率50％':
        print('勝率に反応しました')
        await message.channel.send('||勝率50以上で囲いも居るしdiscordで誰かからのアプローチは"される方"だし僕グループ招待されてるしは"待つ方"だし君に依存するなんてないし絵も上手いしフォロワー224人いるし74/76は相互なんで。強いんで。正論なんで。破綻ないんで。最強BMI16なんで。おつンゴ||') 
            
    
    elif message.content == '!p マツケンサンバ':
        print('マツケンサンバに反応しました')
        await message.channel.send('またやってる') 

    elif message.content == 'あーあ':
        print('あーあとか言われました')
        await message.channel.send('なんですか？？？？？？') 

    else:
        if client.user in message.mentions: # 話しかけられたかの判定
            await reply(message) # 返信する非同期関数を実行


@client.event
async def on_voice_state_update(member, before, after):
    # チャンネルを移動していない場合処理をしない
    if before.channel == after.channel:
        return

    # チャンネルから退出してきた場合
    if before.channel is not None:
        # ボイスチャンネルに誰もいなくなった場合
        if len(before.channel.members) == 0:
            # テキストチャンネルを削除する
            await _channel_delete(member, before.channel)
        else:
            # テキストチャンネルから退出させる
            await _channel_exit(member, before.channel)

    # ボイスチャンネルに参加してきた場合
    if after.channel is not None:
        # 参加したチャンネルの1人目だった場合
        if len(after.channel.members) == 1:
            # テキストチャンネルを作成する
            await _channel_create(member, after.channel)
        else:
            # テキストチャンネルに参加させる
            await _channel_join(member, after.channel)

        # 入室時にメンションでチャンネルに案内
        await _channel_send_join(member, after.channel)

    print("fin voice state update event")


# テキストチャンネルを検索する関数
def _channel_find(voiceChannel):
    text_channels = voiceChannel.guild.text_channels
    channel_name = CHANNEL_PREFIX + str(voiceChannel.id)
    # 名前からチャンネルオブジェクトを取得する
    return discord.utils.get(text_channels, name=channel_name)


# チャンネル作成時の権限リストを返す
def _init_overwrites(guild, member):
    overwrites = {
        # デフォルトのユーザーはメッセージを見れないように
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        # 参加したメンバーは見ることができるように
        member: discord.PermissionOverwrite(read_messages=True)
    }

    bots_role = discord.utils.get(guild.roles, name=BOT_ROLE_NAME)
    if bots_role is not None:
        # Botもメッセージを見れるように
        bot_overwrite = {
            bots_role: discord.PermissionOverwrite(read_messages=True)
        }
        overwrites.update(bot_overwrite)

    return overwrites


# テキストチャンネルを作成する関数
async def _channel_create(member, voiceChannel):
    guild = voiceChannel.guild

    channel_name = CHANNEL_PREFIX + str(voiceChannel.id)
    overwrites = _init_overwrites(guild, member)
    category = voiceChannel.category

    # テキストチャンネルを作成
    await guild.create_text_channel(
        channel_name, overwrites=overwrites, category=category)


# テキストチャンネルを削除する関数
async def _channel_delete(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        await target.delete()


# テキストチャンネルに参加させる関数
async def _channel_join(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        overwrites = discord.PermissionOverwrite(read_messages=True)
        # 該当メンバーに読み取り権限を付与
        await target.set_permissions(member, overwrite=overwrites)


# テキストチャンネルから退出させる関数
async def _channel_exit(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        # 該当メンバーの読取権限を取り消し
        await target.set_permissions(member, overwrite=None)


# 入室時にメンションを飛ばして案内したい
async def _channel_send_join(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        await target.send(member.mention + "聞き専用のチャットを作っておいたわん！")



# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

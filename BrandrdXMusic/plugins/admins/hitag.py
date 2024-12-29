from BrandrdXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ "🤩 𝗦𝗮𝗯𝗮𝗵ı𝗻ı𝘇 𝘅𝗲𝘆𝗶𝗿 𝗬𝗲𝗻𝗶 𝗴ü𝗻 𝘀𝗶𝘇ə 𝘀𝗲𝘃𝗶𝗻𝗰 𝘃ə 𝘂ğ𝘂𝗿 𝗴ə𝘁𝗶𝗿𝘀𝗶𝗻! 𝗛ə𝗿 𝗮𝗻ı𝗻ı𝘇 𝗴ö𝘇ə𝗹 𝗸𝗲ç𝘀𝗶𝗻! 🌸✨",
"☀️ 𝗦𝗮𝗯𝗮𝗵ı𝗻ı𝘇 𝘅𝗲𝘆𝗶𝗿.𝗛ə𝗿 𝗴ü𝗻 𝘆𝗲𝗻𝗶 𝗯𝗶𝗿 ü𝗺𝗶𝗱𝗱𝗶𝗿. 𝗕𝘂 𝗴ü𝗻 𝗱ə 𝗮𝗿𝘇𝘂𝗹𝗮𝗿ı𝗻ı𝘇𝗮 ç𝗮𝘁𝗺𝗮𝗾 üçü𝗻 𝗺ö𝗵𝘁əşə𝗺 𝗯𝗶𝗿 𝗳ü𝗿𝘀ə𝘁𝗱𝗶𝗿! 🌟😊",
"🌸 𝗦𝗮𝗯𝗮𝗵ı𝗻ı𝘇 𝘅𝗲𝘆𝗶𝗿.𝗚ü𝗹ü𝗺𝘀ə𝘆𝗶𝗻 𝘃ə 𝗴ö𝘇ə𝗹 𝗯𝗶𝗿 𝗴ü𝗻ə 𝗵𝗮𝘇ı𝗿 𝗼𝗹𝘂𝗻. 𝗕𝘂 𝗴ü𝗻 𝗱ə 𝗵ə𝗿 ş𝗲𝘆 ü𝗿ə𝘆𝗶𝗻𝗶𝘇𝗰ə 𝗼𝗹𝘀𝘂𝗻! 💕💪",
"☕ 𝗦𝗮𝗯𝗮𝗵ı𝗻ı𝘇 𝘅𝗲𝘆𝗶𝗿.Ç𝗮𝘆ı𝗻ı𝘇ı/𝗤ə𝗵𝘃ə𝗻𝗶𝘇𝗶 𝗮𝗹ı𝗻 𝘃ə 𝗲𝗻𝗲𝗿𝗷𝗶𝗻𝗶𝘇𝗶 𝘆ü𝗸𝘀ə𝗹𝗱𝗶𝗻! 𝗕𝘂𝗴ü𝗻 𝘀𝗶𝘇𝗶𝗻 üçü𝗻 ç𝗼𝘅 𝘂ğ𝘂𝗿𝗹𝘂 𝗼𝗹𝗮𝗰𝗮𝗾! 🌺🔥",
"🦋 𝗦𝗮𝗯𝗮𝗵ı𝗻ı𝘇 𝘅𝗲𝘆𝗶𝗿. 𝗬𝗲𝗻𝗶 𝗯𝗮ş𝗹𝗮𝗻ğı𝗰𝗹𝗮𝗿, 𝘆𝗲𝗻𝗶 ş𝗮𝗻𝘀𝗹𝗮𝗿 𝘀𝗶𝘇𝗶 𝗴ö𝘇𝗹ə𝘆𝗶𝗿. 𝗣𝗼𝘇𝗶𝘁𝗶𝘃 𝗼𝗹𝘂𝗻 𝘃ə 𝗵ə𝗿 𝗮𝗻ı 𝗱ə𝘆ə𝗿𝗹ə𝗻𝗱𝗶𝗿𝗶𝗻! 🌈✨",
          ]

@app.on_message(filters.command(["srtag" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ Bu komanda ancaq qruplar üçündür ")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ Siz admin deyilsiniz,ancaq adminlər tag edə bilər  ")

    if message.reply_to_message and message.text:
        return await message.reply("/srtag Sᴀʙᴀʜıɴıᴢ xᴇʏɪʀ Bᴇʟə ʏᴀᴢıɴ /Nöᴠʙəᴛɪ ᴅəғə ɪsᴛəɴɪʟəɴ ᴍᴇsᴀJᴀ ᴄᴀᴠᴀʙ ᴠᴇʀɪɴ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/srtag Sᴀʙᴀʜıɴıᴢ xᴇʏɪʀ Bᴇʟə ʏᴀᴢıɴ /Nöᴠʙəᴛɪ ᴅəғə ɪsᴛəɴɪʟəɴ ᴍᴇsᴀJᴀ ᴄᴀᴠᴀʙ ᴠᴇʀɪɴ...")
    else:
        return await message.reply("/srtag Sᴀʙᴀʜıɴıᴢ xᴇʏɪʀ Bᴇʟə ʏᴀᴢıɴ /Nöᴠʙəᴛɪ ᴅəғə ɪsᴛəɴɪʟəɴ ᴍᴇsᴀJᴀ ᴄᴀᴠᴀʙ ᴠᴇʀɪɴ...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["cancel", "lifetagg"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ Bu komanda ancaq qruplar üçündür ")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ Siz admin deyilsiniz,ancaq adminlər tag edə bilər  ")
    if chat_id in spam_chats:
        return await message.reply("๏ Ilk olaraq tag etme prosesini başlatın...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["srstop", "cancel", "lifestop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ Indi Tag etme prosesi başlamayıb ")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("Siz admin deyilsiniz,ancaq adminlər tag edə bilər ")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ 𝗧𝗔𝗚 𝗘𝗧𝗠𝗘 𝗣𝗥𝗢𝗦𝗘𝗦𝗜 𝗗𝗔𝗬𝗔𝗡𝗗𝗜𝗥𝗜𝗟𝗗𝗜 ๏")

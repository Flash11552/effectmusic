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

TAGMES = [ "𝐍ə 𝐯𝐚𝐫, 𝐧ə 𝐲𝐨𝐱, 𝐦ə𝐧𝐠ə𝐥𝐝𝐢𝐦! 🤪😎",
"𝐇ə𝐲𝐚𝐭ı𝐦𝐝𝐚 ə𝐧 𝐛ö𝐲ü𝐤 𝐩𝐫𝐨𝐛𝐥𝐞𝐦: 𝐖𝐢-𝐅𝐢-𝐲ə 𝐪𝐨ş𝐮𝐥𝐚 𝐛𝐢𝐥𝐦ə𝐦ə𝐤 😤📶",
"𝐘𝐨𝐱𝐬𝐚 𝐬ə𝐧 𝐝ə 𝐞𝐥ə 𝐦ə𝐧𝐢𝐦 𝐤𝐢𝐦𝐢 𝐠𝐞𝐜ə-𝐠ü𝐧𝐝ü𝐳 𝐭𝐞𝐥𝐞𝐟𝐨𝐧𝐮 ə𝐥𝐢𝐧𝐝ə𝐧 𝐝üşü𝐫𝐦ü𝐫𝐬ə𝐧? 🤳📱",
"𝐁𝐢𝐥𝐢𝐫𝐬ə𝐧, 𝐦ə𝐧𝐢𝐦 ə𝐧 𝐲𝐚𝐱şı 𝐝𝐨𝐬𝐭𝐮𝐦: 𝐘𝐮𝐱𝐮. 😴✨",
"𝐃𝐨𝐬𝐭𝐥𝐚𝐫ı𝐦ı𝐧 𝐦ə𝐧𝐢 ç𝐨𝐱 𝐬𝐞𝐯𝐝𝐢𝐲𝐢𝐧𝐢 𝐝𝐞𝐲𝐢𝐫𝐥ə𝐫, 𝐚𝐦𝐦𝐚 𝐡𝐞ç 𝐯𝐚𝐱𝐭 ə𝐥𝐢𝐦𝐝ə𝐧 𝐭𝐮𝐭𝐚𝐧 𝐭𝐚𝐩ı𝐥𝐦𝐚𝐝ı. 😅🤚",
"𝐁𝐮𝐠ü𝐧 𝐡𝐞ç 𝐧ə 𝐞𝐭𝐦ə𝐤 𝐢𝐬𝐭ə𝐦𝐢𝐫ə𝐦, 𝐛ə𝐥𝐤ə 𝐛𝐮, 𝐛ö𝐲ü𝐤 𝐩𝐥𝐚𝐧ı𝐧 𝐢𝐥𝐤 𝐚𝐝𝐝ı𝐦ı𝐝ı𝐫? 🛋️🛏️",
"𝐌ə𝐧ə 𝐛𝐢𝐫 𝐚𝐳 𝐩𝐮𝐥 𝐯𝐞𝐫𝐢𝐧, 𝐲𝐨𝐱𝐬𝐚 𝐠ə𝐥ə𝐜ə𝐲𝐢𝐦 ç𝐨𝐱 𝐪𝐚𝐫ışı𝐪 𝐨𝐥𝐚𝐜𝐚𝐪! 💸😜",
"Ç𝐨𝐱 𝐝𝐚𝐧ışı𝐫ı𝐪, 𝐚𝐦𝐦𝐚 𝐡ə𝐥ə 𝐡𝐞ç 𝐧ə 𝐝𝐚𝐧ış𝐦𝐚𝐝ı𝐪. 🤔💬",
"𝐊üçə𝐝ə 𝐲𝐚𝐯𝐚ş 𝐚𝐝𝐝ı𝐦𝐥𝐚𝐲𝐚𝐧 𝐛𝐢𝐫𝐢 𝐯𝐚𝐫𝐬𝐚, 𝐨 𝐦ə𝐧ə𝐦. 𝐍ə 𝐞𝐝𝐢𝐦, 𝐡ə𝐲𝐚𝐭ı𝐦𝐝𝐚 𝐡𝐞ç 𝐯𝐚𝐱𝐭 𝐪𝐚ç𝐦𝐚ğı 𝐛𝐚𝐜𝐚𝐫𝐦𝐚𝐝ı𝐦! 🏃‍♂️🚶‍♀️",
"𝐇ə𝐲𝐚𝐭ı𝐧 ə𝐧 𝐛ö𝐲ü𝐤 𝐬𝐢𝐫𝐥ə𝐫𝐢𝐧𝐝ə𝐧 𝐛𝐢𝐫𝐢: 𝐧𝐞𝐜ə 𝐲𝐚𝐭𝐦𝐚𝐪 𝐥𝐚𝐳ı𝐦. 😴🔮",
"𝐇ə𝐦𝐢şə 𝐱𝐞𝐲𝐢𝐫𝐱𝐚𝐡 𝐨𝐥𝐦𝐚ğ𝐚 ç𝐚𝐥ışı𝐫𝐚𝐦, 𝐚𝐦𝐦𝐚 𝐦ə𝐧ə 𝐪ə𝐡𝐯ə 𝐯𝐞𝐫𝐢𝐧, 𝐨𝐧𝐝𝐚 𝐧ə 𝐨𝐥𝐮𝐫, 𝐛𝐢𝐥𝐦𝐢𝐫ə𝐦. ☕👀",
"𝐕ə𝐡𝐡, 𝐛𝐮 𝐠ü𝐧 𝐧ə 𝐞𝐝ə𝐜ə𝐲𝐢𝐦𝐢 𝐡ə𝐥ə 𝐛𝐢𝐥𝐦ə𝐝𝐢𝐦. 𝐘ə𝐪𝐢𝐧 𝐤𝐢, 𝐦əşğ𝐮𝐥 𝐨𝐥𝐦𝐚𝐪𝐝𝐚𝐧 𝐛𝐚ş𝐪𝐚 𝐡𝐞ç 𝐧ə 𝐝üşü𝐧𝐦ə𝐫ə𝐦. 🤷‍♂️",
"𝐘𝐞𝐦ə𝐤 𝐢𝐬𝐭ə𝐲𝐢𝐫ə𝐦, 𝐚𝐦𝐦𝐚 𝐝𝐢𝐲𝐞𝐭ə 𝐛𝐚ş𝐥𝐚𝐝ı𝐦. 𝐀𝐚𝐚, 𝐲𝐞𝐦ə𝐤! 🍕🍔😋",
"𝐁𝐮 𝐠ü𝐧 𝐧ə𝐲𝐢 𝐲𝐚𝐱şı 𝐞𝐭𝐝𝐢𝐦? 𝐘ə𝐪𝐢𝐧 𝐤𝐢, 𝐡𝐞ç 𝐧ə, 𝐚𝐦𝐦𝐚 𝐡ə𝐥ə ç𝐨𝐱 𝐠ü𝐜𝐥ü 𝐠ö𝐫ü𝐧ü𝐫ə𝐦. 💪😜",
"𝐁ü𝐭ü𝐧 𝐝ü𝐧𝐲𝐚𝐧ı 𝐪𝐮𝐫𝐭𝐚𝐫𝐦𝐚𝐪 𝐢𝐬𝐭ə𝐲𝐢𝐫ə𝐦, 𝐚𝐦𝐦𝐚 𝐛𝐢𝐫 𝐚𝐳 𝐲𝐮𝐱𝐮𝐲𝐚 𝐞𝐡𝐭𝐢𝐲𝐚𝐜ı𝐦 𝐯𝐚𝐫. 😴🌍",
"İş𝐢𝐦 ç𝐨𝐱 𝐯𝐚𝐜𝐢𝐛𝐝𝐢𝐫, 𝐚𝐦𝐦𝐚 ə𝐧 𝐯𝐚𝐜𝐢𝐛 𝐢ş𝐢𝐦: 𝐬𝐞𝐯𝐝𝐢𝐤𝐥ə𝐫𝐢𝐦𝐥ə ə𝐲𝐥ə𝐧𝐦ə𝐤! 🕺💃🎉",
"𝐘𝐮𝐱𝐮𝐝𝐚 𝐡ə𝐦ə𝐧 𝐝𝐞𝐲𝐢𝐦 𝐤𝐢, 𝐬𝐚𝐛𝐚𝐡 𝐝𝐚 𝐞𝐲𝐧𝐢 ş𝐞𝐲𝐢 𝐞𝐭𝐦ə𝐲𝐢𝐦. 𝐇ə𝐲𝐚𝐭 𝐬𝐚𝐝ə 𝐨𝐥𝐦𝐚𝐥ı𝐝ı𝐫! 😆😴",
"𝐘𝐚𝐱şı 𝐝𝐨𝐬𝐭𝐮𝐦𝐮𝐧 𝐝𝐞𝐝𝐢𝐲𝐢 𝐤𝐢𝐦𝐢: 𝐇𝐞ç 𝐛𝐢𝐫 𝐩𝐫𝐨𝐛𝐥𝐞𝐦 𝐲𝐨𝐱𝐝𝐮𝐫, 𝐬𝐚𝐝ə𝐜ə 𝐡ə𝐥ə 𝐭𝐚𝐩𝐚 𝐛𝐢𝐥𝐦ə𝐦𝐢şə𝐦. 🤭",
"𝐙𝐚𝐦𝐚𝐧 𝐧ə 𝐪ə𝐝ə𝐫 𝐬ü𝐫ə𝐭𝐥𝐢 𝐤𝐞ç𝐢𝐫! 𝐇ə𝐦𝐢şə 𝐠ə𝐥ə𝐜ə𝐤𝐝ə 𝐨𝐥𝐦𝐚𝐪 𝐢𝐬𝐭ə𝐲𝐢𝐫ə𝐦. ⏳🕰️",
 "𝐇ə𝐦𝐢şə ə𝐧 𝐲𝐚𝐱şı𝐬ı üçü𝐧 𝐝𝐮𝐚 𝐞𝐭, 𝐚𝐦𝐦𝐚 𝐪ə𝐡𝐯ə𝐧𝐢 𝐮𝐧𝐮𝐭𝐦𝐚! ☕🙏",
           ]

VC_TAG = [ "**𝐎𝚈𝙴 𝐕𝙲 𝐀𝙰𝙾 𝐍𝙰 𝐏𝙻𝚂🥲**",
         "**𝐉𝙾𝙸𝙽 𝐕𝙲 𝐅𝙰𝚂𝚃 𝐈𝚃𝚂 𝐈𝙼𝙰𝙿𝙾𝚁𝚃𝙰𝙽𝚃😬**",
         "**𝐂𝙾𝙼𝙴 𝚅𝙲 𝙱𝙰𝙱𝚈 𝙵𝙰𝚂𝚃🏓**",
         "**𝐁𝙰𝙱𝚈 𝐓𝚄𝙼 𝐁𝙷𝙸 𝐓𝙷𝙾𝚁𝙰 𝐕𝙲 𝐀𝙰𝙽𝙰🥰**",
         "**𝐎𝚈𝙴 𝐂𝙷𝙰𝙼𝚃𝚄 𝐕𝙲 𝐀𝙰 𝐄𝙺 𝐄𝙰𝙼 𝐇𝙰𝙸🤨**",
         "**𝐒𝚄𝙽𝙾 𝐕𝙲 𝐉𝙾𝙸𝙽 𝐊𝚁 𝐋𝙾🤣**",
         "**𝐕𝙲 𝐀𝙰 𝐉𝙰𝙸𝚈𝙴 𝐄𝙺 𝐁𝙰𝚁😁**",
         "**𝐕𝙲 𝐓𝙰𝙿𝙺𝙾 𝐆𝙰𝙼𝙴 𝐂𝙷𝙰𝙻𝚄 𝐇𝙰𝙸⚽**",
         "**𝐕𝙲 𝐀𝙰𝙾 𝐁𝙰𝚁𝙽𝙰 𝐁𝙰𝙽 𝐇𝙾 𝐉𝙰𝙾𝙶𝙴🥺**",
         "**𝐒𝙾𝚁𝚁𝚈 𝐕𝙰𝙱𝚈 𝐏𝙻𝚂 𝐕𝙲 𝐀𝙰 𝐉𝙰𝙾 𝐍𝙰😥**",
         "**𝐕𝙲 𝐀𝙰𝙽𝙰 𝐄𝙺 𝐂𝙷𝙸𝙹 𝐃𝙸𝙺𝙷𝙰𝚃𝙸 𝐇𝚄🙄**",
         "**𝐕𝙲 𝐌𝙴 𝐂𝙷𝙴𝙲𝙺 𝐊𝚁𝙺𝙴 𝐁𝙰𝚃𝙰𝙾 𝐓𝙾 𝐒𝙾𝙽𝙶 𝐏𝙻𝙰𝚈 𝐇𝙾 𝐑𝙷𝙰 𝐇?🤔**",
         "**𝐕𝙲 𝐉𝙾𝙸𝙽 𝐊𝚁𝙽𝙴 𝐌𝙴 𝐊𝚈𝙰 𝐉𝙰𝚃𝙰 𝐇 𝐓𝙷𝙾𝚁𝙰 𝐃𝙴𝚁 𝐊𝙰𝚁 𝐋𝙾 𝐍𝙰🙂**",
        ]


@app.on_message(filters.command(["tagall"], prefixes=["/", "@", ".", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

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
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
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

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
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
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("🌷 𝐓𝐀𝐆 𝐀𝐋𝐋 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐒𝐓𝐎𝐏𝐏𝐄𝐃 🎉")

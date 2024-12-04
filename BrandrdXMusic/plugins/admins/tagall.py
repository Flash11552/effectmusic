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

TAGMES = [ "Ə𝗴ə𝗿 𝗯𝗶𝗿 ş𝗲𝘆𝗶 𝘁𝗮𝗺𝗮𝗺𝗶𝗹ə 𝘂𝗻𝘂𝗱𝗮 𝗯𝗶𝗹𝘀ə𝗻𝗶𝘇, 𝗻ə𝘆𝗶 𝘂𝗻𝘂𝗱𝗮𝗿𝗱ı𝗻ı𝘇 𝘃ə 𝗻𝗶𝘆ə? 🧠❌🔄",
"𝗕𝗶𝗿 𝗶𝗻𝘀𝗮𝗻ı𝗻 𝘅𝗮𝘀𝗶𝘆𝘆ə𝘁𝗶𝗻𝗶 𝗱ə𝘆𝗶ş𝗺ə𝗸 𝗶𝗺𝗸𝗮𝗻ı𝗻ı𝘇 𝗼𝗹𝘀𝗮, 𝗸𝗶𝗺𝗶𝗻𝗸𝗶𝗻𝗶 𝘃ə 𝗻ə𝘆𝗶 𝗱ə𝘆𝗶şə𝗿𝗱𝗶𝗻𝗶𝘇? 🤔🔄🧍‍♂️",
"𝗗ü𝗻𝘆𝗮𝗻ı𝗻 ə𝗻 𝗯ö𝘆ü𝗸 𝘀𝗶𝗿𝗿𝗶𝗻𝗶 𝗯𝗶𝗹𝗺ə𝗸 𝗶𝘀𝘁ə𝗿𝗱𝗶𝗻𝗶𝘇𝗺𝗶? 𝗛𝗮𝗻𝘀ı 𝘀𝗶𝗿𝗿 𝘀𝗶𝘇𝗶 𝗺𝗮𝗿𝗮𝗾𝗹𝗮𝗻𝗱ı𝗿𝗮𝗿? 🌌🔑❓"
"Ə𝗴ə𝗿 𝗯𝗶𝗿 𝗴ü𝗻 𝗯ü𝘁ü𝗻 𝗱ü𝗻𝘆𝗮 𝘀𝗶𝘇𝗶 𝗱𝗶𝗻𝗹ə𝘀ə𝘆𝗱𝗶, 𝗼𝗻𝗹𝗮𝗿𝗮 𝗻ə 𝗱𝗲𝘆ə𝗿𝗱𝗶𝗻𝗶𝘇? 🎤🌍👂",
"Ö𝘇ü𝗻ü𝘇𝗱ə 𝗱ə𝘆𝗶ş𝗱𝗶𝗿𝗺ə𝗸 𝗶𝘀𝘁ə𝗱𝗶𝘆𝗶𝗻𝗶𝘇 ə𝗻 𝗯ö𝘆ü𝗸 𝘅ü𝘀𝘂𝘀𝗶𝘆𝘆ə𝘁 𝗵𝗮𝗻𝘀ı𝗱ı𝗿? 🔄💭🧍‍♀️",
"𝗕ü𝘁ü𝗻 𝘅ə𝘆𝗮𝗹𝗹𝗮𝗿ı𝗻ı𝘇 𝗿𝗲𝗮𝗹𝗹𝗮ş𝘀𝗮𝘆𝗱ı, 𝗵ə𝘆𝗮𝘁ı𝗻ı𝘇 𝗻𝗲𝗰ə 𝗴ö𝗿ü𝗻ə𝗿𝗱𝗶? 🌟🏰🎉",
"𝗛𝗮𝗻𝘀ı 𝗱𝗮𝗵𝗮 𝘃𝗮𝗰𝗶𝗯𝗱𝗶𝗿: 𝘇𝗮𝗺𝗮𝗻 𝗺ı, 𝘆𝗼𝘅𝘀𝗮 𝘀𝗲𝘃𝗴𝗶? 🕰️❤️❓",
"𝗛ə𝘆𝗮𝘁ı𝗻ı𝘇ı𝗻 ə𝗻 𝗯ö𝘆ü𝗸 𝗱ə𝗿𝘀𝗶 𝗻ə 𝗼𝗹𝘂𝗯? 📚🤔✨",
"Ə𝗴ə𝗿 𝘀𝗼𝗻𝘀𝘂𝘇 𝘃𝗮𝘅𝘁ı𝗻ı𝘇 𝗼𝗹𝘀𝗮𝘆𝗱ı, 𝗻ə 𝗲𝘁𝗺ə𝘆ə 𝗯𝗮ş𝗹𝗮𝗿𝗱ı𝗻ı𝘇? ⏳♾️💡",
"İ𝗻𝘀𝗮𝗻𝗹𝗮𝗿ı𝗻 𝘀𝗶𝘇𝗶 𝗻𝗲𝗰ə 𝘅𝗮𝘁ı𝗿𝗹𝗮𝗺𝗮𝘀ı𝗻ı 𝗶𝘀𝘁ə𝘆𝗶𝗿𝘀𝗶𝗻𝗶𝘇? 🕊️📝💭",
"𝗛ə𝘆𝗮𝘁ı𝗻ı𝘇ı 𝗱ə𝘆𝗶şə𝗻 𝗯𝗶𝗿 𝗾ə𝗿𝗮𝗿ı 𝘁ə𝘀𝘃𝗶𝗿 𝗲𝗱𝗶𝗻: 🚦🔄🎯",
"𝗗ü𝗻𝘆𝗮𝗱𝗮 𝗵ə𝗿 𝗸ə𝘀𝗶𝗻 𝘀𝗶𝘇𝗱ə𝗻 ö𝘆𝗿ə𝗻ə 𝗯𝗶𝗹ə𝗰ə𝘆𝗶 𝗯𝗶𝗿 ş𝗲𝘆 𝗻ə𝗱𝗶𝗿? 🌍📖🤝",
"𝗛ə𝘆𝗮𝘁𝗱𝗮 𝘀𝗮𝗵𝗶𝗯 𝗼𝗹𝗺𝗮𝗾 𝗶𝘀𝘁ə𝗱𝗶𝘆𝗶𝗻𝗶𝘇 ə𝗻 𝗯ö𝘆ü𝗸 𝘀ə𝗿𝘃ə𝘁 𝗻ə𝗱𝗶𝗿? 💎🧠🕊️",
"Ə𝗴ə𝗿 ö𝗺𝗿ü𝗻ü𝘇 𝗯𝗼𝘆𝘂 𝘆𝗮𝗹𝗻ı𝘇 𝗯𝗶𝗿 𝘀𝘂𝗮𝗹𝗮 𝗰𝗮𝘃𝗮𝗯 𝗮𝗹𝗮 𝗯𝗶𝗹𝘀ə𝗻𝗶𝘇, 𝗵𝗮𝗻𝘀ı 𝘀𝘂𝗮𝗹ı 𝘃𝗲𝗿ə𝗿𝗱𝗶𝗻𝗶𝘇? ❓🔮",
"Ə𝗴ə𝗿 𝗯𝗶𝗿 𝗶𝗻𝘀𝗮𝗻ı𝗻 𝗵ə𝘆𝗮𝘁ı𝗻ı 𝘅𝗶𝗹𝗮𝘀 𝗲𝘁𝗺ə𝗸 üçü𝗻 𝗯𝗮ş𝗾𝗮 𝗯𝗶𝗿𝗶𝗻𝗶𝗻 𝗵ə𝘆𝗮𝘁ı𝗻ı 𝗾𝘂𝗿𝗯𝗮𝗻 𝘃𝗲𝗿𝗺ə𝗹𝗶 𝗼𝗹𝘀𝗮𝘆𝗱ı𝗻ı𝘇, 𝗯𝘂𝗻𝘂 𝗲𝗱ə𝗿𝗱𝗶𝗻𝗶𝘇𝗺𝗶? 🤔⚖️❤️",
"Ə𝗴ə𝗿 𝗵ə𝗾𝗶𝗾ə𝘁𝗶 𝗯𝗶𝗹𝗺ə𝗸 𝘀𝗶𝘇𝗶 𝗶𝗻𝗰𝗶𝗱ə𝗰ə𝗸𝘀ə, 𝘆𝗮𝗹𝗮𝗻ı 𝘀𝗲çə𝗿𝗱𝗶𝗻𝗶𝘇𝗺𝗶? 🔍🖤❓",
"Ə𝗴ə𝗿 𝗴ə𝗹ə𝗰ə𝘆𝗶𝗻𝗶𝘇𝗶 𝗱ə𝘆𝗶ş𝗱𝗶𝗿𝗺ə𝗸 üçü𝗻 𝗸𝗲ç𝗺𝗶ş𝗱ə 𝗯𝗶𝗿 ş𝗲𝘆𝗶 𝗱ü𝘇ə𝗹𝘁𝗺ə𝗸 ş𝗮𝗻𝘀ı𝗻ı𝘇 𝗼𝗹𝘀𝗮, 𝗯𝘂𝗻𝘂 𝗲𝗱ə𝗿𝗱𝗶𝗻𝗶𝘇𝗺𝗶? 🔄⏳🤷‍♂️",
"𝗗ü𝗻𝘆𝗮𝗱𝗮𝗸ı 𝗵ə𝗿 ş𝗲𝘆𝗶 𝗾𝘂𝗿𝗯𝗮𝗻 𝘃𝗲𝗿𝗶𝗯 𝘆𝗮𝗹𝗻ı𝘇 𝗯𝗶𝗿 𝗶𝗻𝘀𝗮𝗻ı 𝘅𝗼ş𝗯ə𝘅𝘁 𝗲𝗱ə 𝗯𝗶𝗹𝘀ə𝗻𝗶𝘇, 𝗯𝘂𝗻𝘂 𝗲𝗱ə𝗿𝗱𝗶𝗻𝗶𝘇𝗺𝗶? 🌍➡️🙂❓",
"𝗦𝗲ç𝗶𝗺 𝗾𝗮𝗿şı𝘀ı𝗻𝗱𝗮 𝗾𝗮𝗹𝘀𝗮𝗻ı𝘇: ö𝘇 𝗮𝗿𝘇𝘂𝗹𝗮𝗿ı𝗻ı𝘇ı, 𝘆𝗼𝘅𝘀𝗮 𝗯𝗮ş𝗾𝗮𝗹𝗮𝗿ı𝗻ı𝗻 𝘀𝗶𝘇𝗱ə𝗻 𝗴ö𝘇𝗹ə𝗱𝗶𝗸𝗹ə𝗿𝗶𝗻𝗶 𝘀𝗲çə𝗿𝗱𝗶𝗻𝗶𝘇? 💭🤝💔",
"Ə𝗴ə𝗿 𝗵ə𝗿 𝗸ə𝘀𝗱ə𝗻 𝗴𝗶𝘇𝗹ə𝗱ə𝗰ə𝗸 𝗯𝗶𝗿 𝘀𝗶𝗿𝗿 𝗯𝗶𝗹𝘀ə𝗻𝗶𝘇, 𝗼𝗻𝘂 𝗽𝗮𝘆𝗹𝗮ş𝗺𝗮𝗾 üçü𝗻 𝗻ə 𝗹𝗮𝘇ı𝗺𝗱ı𝗿? 🕵️‍♂️🔑🤐",
"𝗗ü𝗻𝘆𝗮𝗻ı 𝗱𝗮𝗵𝗮 𝘆𝗮𝘅şı 𝗲𝘁𝗺ə𝗸 üçü𝗻 ö𝘇ü𝗻ü𝘇𝗱ə𝗻 𝗻ə 𝗾𝘂𝗿𝗯𝗮𝗻 𝘃𝗲𝗿ə 𝗯𝗶𝗹ə𝗿𝘀𝗶𝗻𝗶𝘇? 🌟🤲💔",
"Ə𝗴ə𝗿 𝗸𝗶𝗺𝗶𝗻𝘀ə 𝘀𝗶𝘇𝗶 𝘀𝗲𝘃𝗺ə𝘀𝗶 üçü𝗻 𝘆𝗮𝗹𝗮𝗻 𝗱𝗮𝗻ış𝗺𝗮𝗹ı 𝗼𝗹𝘀𝗮𝗻ı𝘇, 𝗯𝘂𝗻𝘂 𝗲𝗱ə𝗿𝗱𝗶𝗻𝗶𝘇𝗺𝗶? 🗣️🤥❤️",
"𝗛ə𝘆𝗮𝘁𝗱𝗮 ə𝗻 𝗯ö𝘆ü𝗸 𝘂ğ𝘂𝗿𝘂𝗻𝘂𝘇 𝘂ğ𝗿𝘂𝗻𝗱𝗮 𝗵𝗮𝗻𝘀ı 𝗱ə𝘆ə𝗿𝗱ə𝗻 𝗶𝗺𝘁𝗶𝗻𝗮 𝗲𝗱ə𝗿𝗱𝗶𝗻𝗶𝘇? 🏆⚖️❓",
"𝗕𝗶𝗿 𝗶𝗻𝘀𝗮𝗻ı𝗻 𝗵𝗶𝘀𝘀𝗹ə𝗿𝗶𝗻𝗶 𝗾𝗼𝗿𝘂𝗺𝗮𝗹ı 𝗼𝗹𝗱𝘂ğ𝘂𝗻𝘂𝘇 𝗯𝗶𝗿 𝗮𝗻𝗱𝗮 𝗼𝗻𝗮 𝗵ə𝗾𝗶𝗾ə𝘁𝗶 𝘀ö𝘆𝗹ə𝗺ə𝗸 𝘀𝗶𝘇𝗶 𝗱𝗮𝗵𝗮 𝘅𝗼ş𝗯ə𝘅𝘁 𝗲𝗱ə𝗿𝗱𝗶, 𝘆𝗼𝘅𝘀𝗮 𝘀𝘂𝘀𝗺𝗮𝗾? 🗣️🤫💭",
"Ə𝗴ə𝗿 𝘆𝗮𝗹𝗻ı𝘇 𝗯𝗶𝗿 𝗱ə𝗳ə 𝗴𝗲𝗿𝗶 𝗾𝗮𝘆ı𝘁𝗺𝗮𝗾 ş𝗮𝗻𝘀ı𝗻ı𝘇 𝗼𝗹𝘀𝗮, 𝗵𝗮𝗻𝘀ı 𝘀ə𝗵𝘃𝗶𝗻𝗶𝘇𝗶 𝗱ü𝘇ə𝗹𝗱ə𝗿𝗱𝗶𝗻𝗶𝘇? 🔄🕰️❌",
"𝗦𝗼𝗻𝘀𝘂𝘇 𝘇ə𝗻𝗴𝗶𝗻𝗹𝗶𝗸, 𝗮𝗺𝗺𝗮 𝘁ə𝗸𝗹𝗶𝗸, 𝘆𝗼𝘅𝘀𝗮 𝘀𝗮𝗱ə 𝗵ə𝘆𝗮𝘁, 𝗮𝗺𝗺𝗮 𝘀𝗲𝘃𝗴𝗶 𝗱𝗼𝗹𝘂? 💰➖👤 𝘃𝘀 🏡❤️",
"𝗦𝗶𝘇𝗶 𝗵𝗲ç 𝘃𝗮𝘅𝘁 𝘂𝗻𝘂𝘁𝗺𝗮𝘆𝗮𝗰𝗮𝗾𝗹𝗮𝗿ı 𝗯𝗶𝗿 ş𝗲𝘆 𝗲𝘁𝗺ə𝗹𝗶𝘀𝗶𝗻𝗶𝘇. 𝗡ə 𝗲𝗱ə𝗿𝗱𝗶𝗻𝗶𝘇? 🌍💥🤔",
"𝗕𝗶𝗿 𝘀𝘂𝗮𝗹ı ö𝗺ü𝗿 𝗯𝗼𝘆𝘂 𝗰𝗮𝘃𝗮𝗯𝘀ı𝘇 𝗯𝘂𝗿𝗮𝘅𝗺𝗮𝗾 𝗶𝘀𝘁ə𝘀ə𝗻𝗶𝘇, 𝗵𝗮𝗻𝘀ı 𝘀𝘂𝗮𝗹 𝗼𝗹𝗮𝗿𝗱ı? ❓🚪❌",
"Ö𝘇 𝘅𝗼ş𝗯ə𝘅𝘁𝗹𝗶𝘆𝗶𝗻𝗶𝘇 𝗯𝗮ş𝗾𝗮𝘀ı𝗻ı𝗻 𝗸ə𝗱ə𝗿𝗶𝗻ə 𝘀ə𝗯ə𝗯 𝗼𝗹𝘀𝗮, 𝘅𝗼ş𝗯ə𝘅𝘁 𝗼𝗹𝗺𝗮ğ𝗮 𝗱𝗮𝘃𝗮𝗺 𝗲𝗱ə𝗿𝗱𝗶𝗻𝗶𝘇𝗺𝗶? 😊➡️😢❓",
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
        return await message.reply("🎧 𝐓𝐀𝐆 𝐀𝐋𝐋 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐒𝐓𝐎𝐏𝐏𝐄𝐃 🎉")

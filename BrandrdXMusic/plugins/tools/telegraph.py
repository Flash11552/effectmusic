import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from BrandrdXMusic import app
import requests


def upload_file(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "json": "true"}
    files = {"fileToUpload": open(file_path, "rb")}
    response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        return True, response.text.strip()
    else:
        return False, f"ᴇʀʀᴏʀ: {response.status_code} - {response.text}"


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Zəhmət olmasa bir şəkil, gif və ya videoya yanıt atın"
        )

    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size

    if file_size > 200 * 1024 * 1024:
        return await message.reply_text("200 MB a qədər fayllar atın")

    try:
        text = await message.reply("Pʀᴏᴄᴇssɪɴɢ...")

        last_percent = 0

        async def progress(current, total):
            nonlocal last_percent
            percent = round(current * 100 / total, 1)
            if percent != last_percent:  # eyni faizdə olarsa edit etmə
                last_percent = percent
                try:
                    await text.edit_text(f"📥 Yüklənir... {percent}%")
                except Exception:
                    pass

        try:
            local_path = await media.download(progress=progress)
            await text.edit_text("📤 Hazır Olur...")

            success, upload_path = upload_file(local_path)

            if success:
                await text.edit_text(
                    f"🌐 | [Hazırdı]({upload_path})",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Buradan Götür",
                                    url=upload_path,
                                )
                            ]
                        ]
                    ),
                )
            else:
                await text.edit_text(
                    f"Xəta\n{upload_path}"
                )

            try:
                os.remove(local_path)
            except Exception:
                pass

        except Exception as e:
            await text.edit_text(f"❌ Xəta\n\n<i>Rᴇᴀsᴏɴ: {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
                pass
            return
    except Exception:
        pass


__HELP__ = """
**ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs**

ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ:

- `/tgm`: ᴜᴘʟᴏᴀᴅ ʀᴇᴘʟɪᴇᴅ ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ.
- `/tgt`: sᴀᴍᴇ ᴀs `/tgm`.
- `/telegraph`: sᴀᴍᴇ ᴀs `/tgm`.
- `/tl`: sᴀᴍᴇ ᴀs `/tgm`.

**ᴇxᴀᴍᴘʟᴇ:**
- ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴡɪᴛʜ `/tgm` ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛ.

**ɴᴏᴛᴇ:**
ʏᴏᴜ ᴍᴜsᴛ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ғɪʟᴇ ғᴏʀ ᴛʜᴇ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴡᴏʀᴋ.
"""

__MODULE__ = "Tᴇʟᴇɢʀᴀᴘʜ"

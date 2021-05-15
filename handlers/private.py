from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hai aku {bn} 🎵

Saya bisa memutar musik di voice chat group anda . Dikembamgkan oleh [xᴛᴀᴀ](https://t.me/xtaaaanj)

Gunakan bot ini dengan baik. Jika terjadi kendala hubungi [xᴛᴀᴀ](https://t.me/xtaaaanj) **
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Penjelasan perintah", url="https://telegra.ph/PERINTAH-04-21")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/gppdahsini"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel ", url="https://t.me/HeartCrackscnl"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/HeartCrackscnl" 
                    ),
                    InlineKeyboardButton(
                        "Instagram own", url="https://https://www.instagram.com/eextaa_"
                    )
                ]
            ]
        )
   )



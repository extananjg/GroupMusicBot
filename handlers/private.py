from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hai aku {bn} 🎵

Aku adalah Musik Bot, bot sumber terbuka yang memungkinkan Anda memutar musik di grup telegram Anda.
Tidak mengetahui cara memakainya? Baca panduan pemakaian agar langsung memahami tanpa bertanya!
━━━━━━━━━━━━━━━━━━━━━━ 

Pemilik bot : [xᴛᴀᴀ](https://t.me/xtaaaanj)
bot Assistant : [xᴛᴀᴀɴᴊᴋɴᴛʟ Assistant](https://t.me/xtaanjkntlasisten) **
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📕panduan perintah", url="https://telegra.ph/PERINTAH-04-21")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group mutualan", url="https://t.me/gppdahsini"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel bucin", url="https://t.me/HeartCrackscnl"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "instagram own", url="https://www.instagram.com/eextaa_"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**xᴛᴀᴀɴᴊᴋɴᴛʟ Music ʙᴏᴛ sedang online bous😎**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel bucin", url="https://t.me/HeartCrackscnl" 
                    ),
                    InlineKeyboardButton(
                        "Instagram own", url="https://www.instagram.com/eextaa_"
                    )
                ]
            ]
        )
   )



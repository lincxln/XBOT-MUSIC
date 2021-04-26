from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Halo 👋! Saya dapat memutar musik dalam obrolan suara Grup Telegram.\n\n✣ Apakah Anda ingin saya memutar musik di obrolan suara grup Telegram Anda? Silakan klik \'📜 Panduan Menggunakan BOT 📜\' tombol di bawah untuk mengetahui bagaimana cara menggunakan saya.\n\n✣ Tambahkan [Assistant Shin Musik](https://t.me/Kuflekkk) ke grup Anda untuk memutar musik di obrolan suara grup Anda.\n\n✣ Info & perintah selengkapnya yang disebutkan di [User Manual](https://telegra.ph/BOT-Music-Man-Voice-Chat-Group-04-16)\n\nManaged With ☕️ By [Feri](https://t.me/xflicks)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Panduan Menggunakan BOT 📜", url="https://telegra.ph/text-04-11-2")
                  ],[
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/masukajaudhh"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/hanyabotferi"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✣ Pemutar Musik Sedang Online ✣**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/masukajaudhh"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/xflicks"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/masukajaudhh"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/xflicks"
                    )
                ]
            ]
        )
   )

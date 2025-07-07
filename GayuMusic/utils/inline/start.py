from pyrogram.types import InlineKeyboardButton

import config
from GayuMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                       text="🍁𝐎ᴡɴᴇʀ🍁", user_id=config.OWNER_ID
                    ),
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
      [
            InlineKeyboardButton(
                        text="🍁𝐒ᴜᴘᴘᴏʀᴛ🍁", url=config.SUPPORT_CHAT
                    ),
            InlineKeyboardButton(
                        text="🍁𝐔ᴘᴅᴀᴛᴇs🍁", url=config.SUPPORT_CHANNEL
                    ),
        ],
    ]
    return buttons

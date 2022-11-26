import traceback
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.errors import UserNotParticipant

from WebStreamer.vars import Var

async def force_sub(client: Client, message:Message):
    if Var.FORCE_UPDATES_CHANNEL:
        try:
            user = await client.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            print(user.status.name)
            if user.status.name == "BANNED":
                await message.reply_text(
                    text=f"__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n  **Cᴏɴᴛᴀᴄᴛ ᴍʏ [Dᴇᴠᴇʟᴏᴘᴇʀ](tg://user?id={Var.OWNER_ID}) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**",
                    parse_mode=ParseMode.MARKDOWN,
                    disable_web_page_preview=True
                )
                return False
        except UserNotParticipant:
            await message.reply_text(
                text="""<i>Jᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ 🔐</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [[ InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}") ]]
                ),
                parse_mode=ParseMode.HTML
            )
            return False
        except Exception as e:
            await message.reply_text(
                text=f"**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍʏ [Dᴇᴠᴇʟᴏᴘᴇʀ](tg://user?id={Var.OWNER_ID})**",
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True)
            return False
    return True
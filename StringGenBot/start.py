from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""ʜᴇʏ {msg.from_user.mention}

ꜱᴀʏᴀ {me2}.
ᴅɪ ʙᴜᴀᴛ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀɴᴛᴜ ᴀɴᴅᴀ ᴍᴇɴɢᴀᴍʙɪʟ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ ᴅᴀɴ ᴀᴍᴀɴ
•––––––––☆–––––––––•
sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴍᴇɴɢᴀᴍʙɪʟ sᴛʀɪɴɢ sᴇssɪᴏɴ !
•––––––––☆–––––––––•

ᴅɪʙᴜᴀᴛ ᴏʟᴇʜ  : [𝚍𝚊𝚛𝚔𝚒𝚎𝚣](tg://user?id={OWNER_ID}) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("ɢʀᴏᴜᴘ", url="t.me/HaoTogelLivedraw"),
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="t.me/haotogel_result")
                ]
            ]
        ),
        disable_web_page_preview=True,
)

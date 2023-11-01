from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://te.legra.ph/file/a35aeb698a07c50f8dfc3.jpg", caption=f"» ᴋᴀᴍᴜ ʜᴀʀᴜꜱ ʙᴇʀɢᴀʙᴜɴɢ ᴅᴇɴɢᴀɴ ɢʀᴜᴘ ᴀɢᴀʀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ꜱᴀʏᴀ [𝐎𝐅𝐅𝐈𝐂𝐄]({link}). ꜱᴇꜱᴜᴅᴀʜ ʙᴇʀɢᴀʙᴜɴɢ ꜱɪʟᴀʜᴋᴀɴ ꜱᴛᴀʀᴛ ꜱᴀʏᴀ ᴋᴇᴍʙᴀʟɪ !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("</> 𝐎𝐅𝐅𝐈𝐂𝐄", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")

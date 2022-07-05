import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os

master_user = os.environ.get("MASTER_USERNAME", None)

if "@" in master_user: 
    master_user.replace("@", "")

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/28146e281d006a2bb57bd.jpg",
        caption=f"""**ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/OFFICIALHACKERERA)
✨ʙᴇsᴛ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ

💫  ᴇᴀsʏ ᴅᴇᴘʟᴏʏ
💫  ʙᴀsᴇᴅ ᴏɴ ᴘʏʀᴏɢʀᴀᴍ
💫  ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛs
💫  ʙᴇᴡ ғᴇᴀᴛᴜʀᴇs
💫  ᴍᴀᴅᴇ ʙʏ ᴍʀ ᴏғғɪᴄɪᴀʟ ʜᴀᴄᴋᴇʀ
💫  ᴀʟᴡᴀʏs ᴡɪʟʟ ᴜᴘᴅᴀᴛᴇ
💫  ʙᴇsᴛ ᴀɴᴅ sᴇᴄᴜʀᴇ
💫  ғᴀsᴛ sᴍᴏᴏᴛʜ ᴀɴᴅ sᴛʏʟɪsʜ

[ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ](t.me/PLUS_MUSIC_BOT?startgroup=new)

**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="• ᴄʜᴀɴɴᴇʟ •",
                            url=f"https://t.me/Broken_Heart_72"),

                            InlineKeyboardButton(
                            text="• ᴏᴡɴᴇʀ •",
                            url=f"https://t.me/OFFICIALHACKERERA"),
                            
                    InlineKeyboardButton(
                            text="• sᴜᴘᴘᴏʀᴛ •",
                            url=f"https://t.me/HEPPYLIFI")
               ]
           ]
       ),
    )





@Client.on_message(command(["alive"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_video(
        video=f"https://te.legra.ph/file/b4cf9fec53289e0957cdb.mp4",
        caption=f"""**ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/OFFICIALHACKERERA)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="• ᴄʜᴀɴɴᴇʟ •",
                            url=f"https://t.me/Broken_Heart_72"),
                            
                    InlineKeyboardButton(
                            text="• sᴜᴘᴘᴏʀᴛ •",
                            url=f"https://t.me/HEPPYLIFI")
                ]
            ]
        ),
    )

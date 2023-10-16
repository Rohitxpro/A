import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VipX import app  

photo = [
    "https://graph.org/file/111c62e57e088390f0cf9.jpg",
    "https://graph.org/file/907a49d138b184d9d3baf.mp4",
    "https://graph.org/file/902657d97d60f4afefd3d.jpg",
    "https://graph.org/file/cf874842285fc69abc2cd.jpg",
    "https://graph.org/file/3af2c579f478ba36fa9be.jpg",
    "https://graph.org/file/ef2d1614b82264bc1ab59.jpg",
    "https://telegra.ph/file/2b5b66c9a0989afa0779a.jpg",
    "https://graph.org/file/c9c0e4fffee6e0a7b6bf8.jpg",
    "https://graph.org/file/d3c07149224225e5dd895.jpg",
    "https://telegra.ph/file/4f877f2843f31fcc32242.jpg",
    "https://graph.org/file/e50925a5e4f1d6a7b270e.jpg",
    "https://telegra.ph/file/2a10683a2166f7cf4940b.jpg",
    "https://telegra.ph/file/cda35ca740e1229626e48.jpg",
    "https://telegra.ph/file/9f7186cd3d87199426e03.jpg",
    "https://telegra.ph/file/7fe39f1baa1a93b9a3f0e.jpg",
    
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🌷𝐇ᴇʏ {message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳**\n\n"
                f"**📝𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**🔐𝐂ʜᴀᴛ 𝐔.𝐍:** @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**💖𝐔ʀ 𝐈d:** {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**✍️𝐔ʀ 𝐔.𝐍:** @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🥳ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄʜᴀᴛ🥳", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))

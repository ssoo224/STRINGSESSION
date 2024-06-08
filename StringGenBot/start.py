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
        text=f"""Hᴇʏ {msg.from_user.mention}🦋,

➬انا بوت {me2},
➬اختصاصي هو استخراج جلسات الخاصه بحسابات التيليجرام❤✨
➬ان كنت تريد تنصيب حسابك تيليثون اضغط علي تيليثون واستخرج جلسة التيرمكس❤✨
➫ان كنت تريد تنصيب حسابك ميوزك او قران اضغط علي بايروجرام (مع مراعات الاصدار)❤✨

لتواصل هنا🌚 ❤ 𝑫𝑬𝑽 : [ᗬẺṨⴼᎯ](https://t.me/U_7h1) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="اضغط لاستخراج الجلسه المناسبه", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("sᴏᴜʀᴄᴇ", url="https://t.me/huntersource"),
                    InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/U_7h1")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )

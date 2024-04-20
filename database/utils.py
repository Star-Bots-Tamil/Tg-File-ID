import math, time
from datetime import datetime
from pytz import timezone
from config import Config, Text 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def send_log(b, u):
    if Config.LOG_CHANNEL is not None:
        curr = datetime.now(timezone("Asia/Kolkata"))
        date = curr.strftime('%d %B, %Y')
        time = curr.strftime('%I:%M:%S %p')
        await b.send_message(
            Config.LOG_CHANNEL,
            f"**#New_User\n\n᚛› Name :- {u.mention}\n᚛› ID :- `{u.id}`\n᚛› Date :- {date}\n᚛› Time :- {time}\n\n᚛› From Bot :- {b.mention}**"
        )

from aiogram import types
from api import get_data_by_ticker
import datetime


async def price(message: types.Message):
    print(message)
    text = message.text.split(" ")

    if len(text) > 1:
        data = await get_data_by_ticker(text[1])
        if data == None:
            await message.reply("Pair is Invalid! Try again.")
            return
            
        date = datetime.datetime.fromtimestamp(int(data['datetime'] / 1000))
        
        await message.reply(f"""
<b>Info for {data['symbol']}</b>

<b>Prices:</b>
    <code>Buy price: {data['buy']} {data['quoteCurrency']}</code>
    <code>Sell price: {data['sell']} {data['quoteCurrency']}</code>
    <code>High price(24h): {data['high']} {data['quoteCurrency']}</code>
    <code>Low price(24h): {data['low']} {data['quoteCurrency']}</code>
<b>Procents:</b>
    <code>Change rate(24h): {round(float(data['changeRate']) * 100, 2)}%</code>
<b>Volumes:</b>
    <code>Left volume(24h): {round(float(data['vol']))} {data['baseCurrency']}</code>
    <code>Right volume(24h): {round(float(data['volValue']))} {data['quoteCurrency']}</code>


<i>Updated at {date:%Y-%m-%d %H:%M:%S}</i>
""", parse_mode="html")
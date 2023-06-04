from aiogram import types
from api import save_rates_by_ticker


async def rates(message: types.Message):
    text = message.text.split(" ")

    if len(text) > 1:
        if len(text) > 2:
            tmp = await save_rates_by_ticker(text[1], text[2])
        else:
            tmp = await save_rates_by_ticker(text[1])

        if tmp is False:
            await message.reply("Pair or Timeframe is Invalid! Try again.")
            return

        await message.reply_photo(open(f"images/{text[1].upper()}.png", "rb"))
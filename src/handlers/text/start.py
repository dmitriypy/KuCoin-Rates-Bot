from aiogram import types


async def bot_start(msg: types.Message):
    await msg.answer("""
Привет, вот мои команды:
/price <pair>* - получить свежую информацию о криптовалютной паре(btc-usdt к примеру)
/rates <pair>* <timeframe> - получить свежий график о криптовалютной паре(btc-usdt к примеру)
""")
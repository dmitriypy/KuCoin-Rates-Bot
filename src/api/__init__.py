import aiohttp
import datetime
import mplfinance as mpf
import pandas as pd
import time
from data.config import kwargs


async def get_data_by_ticker(pair):
    async with aiohttp.ClientSession() as session:
        r = await session.get(url="https://www.kucoin.com/_api/trade-front/market/getSymbolTick",
                              params={"symbols": pair.upper()})
        tmp = await r.json()

        if tmp["data"] == []:
            return None
        return tmp["data"][0]


async def save_rates_by_ticker(pair, timeframe="12hour"):
    unixtime = int(time.time())

    async with aiohttp.ClientSession() as session:
        r = await session.get(url="https://www.kucoin.com/_api/order-book/candles",
                              params={
                                "symbol": pair.upper(),
                                "type": timeframe.lower(),

                                "begin": unixtime - 2678400,
                                "end":   unixtime,
                              })
        
        tmp = await r.json()
        
        if not tmp["data"]:
            return False

        for i in range(len(tmp["data"])):
            tmp["data"][i][0] = datetime.datetime.fromtimestamp(int(tmp["data"][i][0]))
            tmp["data"][i][1:] = map(float, tmp["data"][i][1:])
            

        df = pd.DataFrame.from_dict(tmp["data"])
        df.drop(5, axis=1, inplace=True)

        df.columns=["Date", "Open","Close","High","Low","Volume"]
        df.set_index('Date', inplace=True)

        mpf.plot(df, title=f"\n{pair.upper()}\nTimeFrame: {timeframe.upper()}", **kwargs, savefig=f"images/{pair.upper()}")
from environs import Env
import mplfinance as mpf

env = Env()
env.read_env('data/.env')


BOT_TOKEN: str = env.str('BOT_TOKEN')
mc = mpf.make_marketcolors(up='#8cda65',down='#ee404c',inherit=True, edge="white", wick="white")
style = mpf.make_mpf_style(base_mpf_style='nightclouds',marketcolors=mc)
kwargs=dict(volume=True,type='candle', show_nontrading=True, style=style, scale_width_adjustment=dict(volume=1,candle=1.25), ylabel_lower='Volume(right)', datetime_format='%d-%m-%Y')
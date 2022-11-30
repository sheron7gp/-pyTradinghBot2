import time
import os
import ccxt
#import dontshare_config
from dotenv import load_dotenv


def configure():
    load_dotenv()


gate = ccxt.gate({
    'enbaleRateLimit': True,
    'apiKey': os.getenv('apiKey'),
    'secret': os.getenv('secret'),
})


symbol = 'RIN/USDT'
size = 1

order = gate.create_market_buy_order(symbol, size)
print(order)
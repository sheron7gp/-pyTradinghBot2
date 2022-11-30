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

#print(gate.fetch_balance())


def get_bid_ask():

    btc_phe_book = gate.fetch_order_book('RIN/USDT')  # BTC/USD BC/USDT
    print(btc_phe_book)
#    #btc_bid = btc_phe_book

get_bid_ask()

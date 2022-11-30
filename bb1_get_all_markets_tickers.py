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


markets = gate.load_markets()
print(markets)

for m in markets:
    print((m))
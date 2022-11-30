import ccxt
import config


exchange = ccxt.gate({
    'apiKey': config.GATE_API_KEY_2,
    'secret': config.GATE_SECRET_KEY_2
})

balance = exchange.fetch_balance()





#print(balance)
print(balance['total']['RIN'])
print(balance['total']['USDT'])
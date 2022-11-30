import ccxt
import config


gate = ccxt.gate({
    'enableRateLimit': True,
    'apiKey': config.GATE_API_KEY,
    'secret': config.GATE_SECRET_KEY
})

balance = gate.fetch_balance()

print(balance['total']['RIN'])
print(balance['total']['USDT'])
# print(balance)

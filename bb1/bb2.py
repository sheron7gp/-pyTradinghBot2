import ccxt
import config


exchange = ccxt.gate({
    'apiKey': config.GATE_API_KEY,
    'secret': config.GATE_SECRET_KEY
})

balance = exchange.fetch_balance()
print(balances)
#print(balances['total']['RIN'])
#print(balances['total']['USDT'])
import ccxt
import config



exchange = ccxt.gate({
    'apiKey': config.GATE_API_KEY,
    'secret': config.GATE_SECRET_KEY
})

markets = gate.load_markets()
print(markets)

for m in markets:
    print((m))
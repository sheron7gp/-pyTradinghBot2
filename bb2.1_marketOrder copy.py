import ccxt
import config


gate = ccxt.gate({
    'enableRateLimit': True,
    'apiKey': config.GATE_API_KEY,
    'secret': config.GATE_SECRET_KEY
})

symbols = 'rin_usdt'
size = 1.33
#bid = 0.1185


gate.create_market_buy_order(symbols, size )
print(order)


#balance = exchange.fetch_balance()

#print(balance['total']['RIN'])
#print(balance['total']['USDT'])
#print(balance)

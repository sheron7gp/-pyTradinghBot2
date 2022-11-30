import ccxt
import config


gate = ccxt.gate({
    'enableRateLimit': True,
    'apiKey': config.GATE_API_KEY,
    'secret': config.GATE_SECRET_KEY
})

symbol = 'RIN/USDT'  # 'rin_usdt  'RIN_USDT' '
size = 1.33
#bid = 0.1185


order = gate.create_market_buy_order(symbol, size )
print(order)


#balance = exchange.fetch_balance()

#print(balance['total']['RIN'])
#print(balance['total']['USDT'])
#print(balance)

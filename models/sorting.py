def sort_trades(trades, key=lambda x: x['price'], reverse=False):
    sorted_trades = sorted(trades, key=key, reverse=reverse)
    print("Sorted Trades:")
    for trade in sorted_trades:
        print(trade)
    return sorted_trades

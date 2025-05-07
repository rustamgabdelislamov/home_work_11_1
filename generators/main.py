from generators.generators import filter_by_currency

transactions = input()

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
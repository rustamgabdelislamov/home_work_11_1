def filter_by_currency(transactions, currency_code):
    if not isinstance(transactions, list):
        return 'Вы ввели не список'
    if not transactions or not currency_code:
        return []

    def check_currency(transaction):
        if not isinstance(transaction, dict):
            return False
        code = transaction.get('operationAmount', {}).get('currency', {}).get('code')
        return code == currency_code

    return filter(check_currency, transactions)


transactions = [
    {'id': 1, 'operationAmount': {'amount': '100.00', 'currency': {'code': 'USD'}}},
    {'id': 2, 'operationAmount': {'amount': '200.00', 'currency': {'code': 'EUR'}}},
    {'id': 3, 'operationAmount': {'amount': '150.00', 'currency': {'code': 'USD'}}}
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
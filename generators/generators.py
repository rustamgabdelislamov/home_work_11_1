def filter_by_currency(transactions, currency_code):
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction

def filter_by_currency(transactions, currency_code):
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
       yield transaction["description"]



def filter_by_currency(transactions, currency_code):
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
       yield transaction["description"]


def card_number_generator(start, end):
    for number in range(start, end):
        yield f"{number // 1000000000000000:04} {number // 100000000000 % 10000:04} " \
              f"{number // 10000 % 10000:04} {number % 10000:04}"


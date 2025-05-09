from typing import Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator[dict, None]:
    """
    Функция поочередно выдает транзакции, где валюта операции соответствует заданной
    """

    if not currency:
        raise ValueError("Не указана валюта")
    elif not transactions_list:
        raise ValueError("Не указан список транзакций")
    else:
        for transaction in transactions_list:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, end):
    for number in range(start, end):
        yield f"{number // 1000000000000000:04} {number // 100000000000 % 10000:04} " \
              f"{number // 10000 % 10000:04} {number % 10000:04}"


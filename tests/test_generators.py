import pytest

from src.generators import filter_by_currency

def test_filter_by_currency(
        transactions, transaction_usd_1, transaction_usd_2, transaction_usd_3, transaction_rub_1, transaction_rub_2
):
    #Проверка на валюту "USD"
    test_currency_usd = filter_by_currency(transactions, "USD")
    assert next(test_currency_usd) == transaction_usd_1
    assert next(test_currency_usd) == transaction_usd_2
    assert next(test_currency_usd) == transaction_usd_3

    # Проверка на валюту "RUB"
    test_currency_rub = filter_by_currency(transactions, "RUB")
    assert next(test_currency_rub) == transaction_rub_1
    assert next(test_currency_rub) == transaction_rub_2

    # Проверка на пустое значение валюты
    with pytest.raises(ValueError):
        next(filter_by_currency(transactions, ""))

    # Проверка на отсутствие валюты в списке итеррации
    with pytest.raises(StopIteration):
        next(filter_by_currency(transactions, "EUR"))

    # Проверка на отсутсвие списка транзакции
    with pytest.raises(ValueError):
        next(filter_by_currency([],"RUB"))













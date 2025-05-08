import pytest


from generators.generators import filter_by_currency

@pytest.mark.parametrize("transactions, currency_code, expected", [
    (
        [
            {
                "id": 939719570,
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "RUB",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
            }
        ],
        "USD",
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
        }
    )
])
def test_filter_by_currency(transactions, currency_code, expected):
    result = filter_by_currency(transactions, currency_code)
    assert result == expected

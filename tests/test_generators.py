from generators.generators import filter_by_currency, transaction_descriptions

import pytest


@pytest.mark.parametrize("transactions, currency_code, expected", [
    (
        [
         {'id': 1, 'operationAmount': {'amount': '100.00', 'currency': {'code': 'USD'}}},
         {'id': 2, 'operationAmount': {'amount': '200.00', 'currency': {'code': 'EUR'}}},
         {'id': 3, 'operationAmount': {'amount': '150.00', 'currency': {'code': 'USD'}}}
        ],
        "USD",
        [
         {'id': 1, 'operationAmount': {'amount': '100.00', 'currency': {'code': 'USD'}}},
         {'id': 3, 'operationAmount': {'amount': '150.00', 'currency': {'code': 'USD'}}}
        ]
    ),
    (
        [
         {'id': 1, 'operationAmount': {'amount': '100.00', 'currency': {'code': 'USD'}}},
         {'id': 2, 'operationAmount': {'amount': '200.00', 'currency': {'code': 'EUR'}}},
         {'id': 3, 'operationAmount': {'amount': '150.00', 'currency': {'code': 'USD'}}}
        ],
        "",
        []
    ),
    (
        [],
        "USD",
        []
    ),
    (
        "",
        "USD",
        'Вы ввели не список'
    ),

])


def test_filter_by_currency(transactions, currency_code, expected):
    result = list(filter_by_currency(transactions, currency_code))
    assert result == expected



@pytest.mark.parametrize("transactions, expected", [
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

        ["Перевод организации",
        "Перевод со счета на счет",

        ]
    )
])

def test_transaction_descriptions(transactions, expected):
    result = list(transaction_descriptions(transactions))
    assert result == expected




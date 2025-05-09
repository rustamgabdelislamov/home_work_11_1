from generators.generators import filter_by_currency

transactions = [{
          "id": 939719570,
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "RUB",
                  "code": "RUB"
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
       },
    {
        "id": 939719570,
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
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
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
    }

]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
import json
import requests
from config import money, TOKEN, api_key

class ConvertException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertException(f'Невозможно перевести одинаковые валюты {base}.')

        quote_ticker, base_ticker = money[quote], money[base]

        try:
            quote_ticker = money[quote]
        except KeyError:
            raise ConvertException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = money[base]
        except KeyError:
            raise ConvertException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}\
                         &api_key={api_key}')
        total_base = json.loads(r.content)[money[base]]

# 09adff6f47d08c4b8ea448c04e0d4a318c1c84f3f9d23050dd562321a6d4b2ff
# import json
# import requests
# from config import *
#
#
# class ExchangeException(Exception):
#     pass
#
#
# class Exchange:
#     @staticmethod
#     def get_price(quote: str, base: str, amount: str):
#         if quote == base:
#             raise ExchangeException(
#                 f'Нельзя перевести одинаковые валюты {base}.')
#
#         try:
#             quote_ticker = keys[quote]
#         except KeyError:
#             raise ExchangeException(f'Не смог обработать валюту {quote}')
#
#         try:
#             base_ticker = keys[base]
#         except KeyError:
#             raise ExchangeException(f'Не смог обработать валюту {base}')
#
#         try:
#             amount = int(amount)
#         except ValueError:
#             raise ExchangeException(f'Не смог обработать количество {amount}')
#
#         r = requests.get(
#             f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
#         total_base = float(json.loads(r.content)[keys[quote]])
#         return total_base
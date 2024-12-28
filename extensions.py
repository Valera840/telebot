import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CriptoConvertor:
    @staticmethod
    def convert( quote: str , base: str , amount: str):

        quote_tiker, base_tiker = keys[quote], keys[base]

        if quote == base:
            raise ConvertionException(f'Нельзя перевести одинаковые валюты {base}')



        try:
            quote_tiker == keys[quote]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту {quote}')

        try:
            base_tiker == keys[base]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_tiker}')

        total = json.loads(r.content)[keys[base]]
        return total

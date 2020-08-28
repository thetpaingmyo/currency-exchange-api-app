import requests
from cachetools import cached,TTLCache
from .history import Save_to_history

class OpenCurrencySite:
    END_POINT = 'https://openexchangerates.org/api/'

    def __init__(self, id):
        self.id = id

    @property
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def open_site(self):
        return requests.get(f"{self.END_POINT}latest.json?app_id={self.id}").json()

    def convert(self, from_amount, from_currency, to_currency):
        exchange_rates = self.open_site['rates']
        if from_currency == 'USD':
            to_amount = from_amount * exchange_rates[to_currency]
            result = f"{from_currency}{from_amount} is {to_currency}{to_amount:.2f}."
            to_history = Save_to_history(result)
            to_history.save()
            return result
        else:
            to_amount = from_amount/exchange_rates[from_currency]*exchange_rates[to_currency]
            result = f"{from_currency}{from_amount} is {to_currency}{to_amount:.2f}."
            to_history = Save_to_history(result)
            to_history.save()
            return result
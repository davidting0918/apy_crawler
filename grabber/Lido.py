from datetime import datetime as dt

import requests


class Lido(object):
    def __init__(self):
        self.endpoint = "https://eth-api.lido.fi/v1"

    def get_tvl(self, base=None):
        pass

    def get_currency_apy_last(self, currency):

        currency_list = ["steth", "eth"]
        if currency not in currency_list:
            return None

        url = self.endpoint + f"/protocol/{currency}/apr/last"
        res = requests.get(url).json()

        data = res["data"]
        meta = res["meta"]

        result = {"timestamp": dt.fromtimestamp(data["timeUnix"]), "currency": meta["symbol"], "apy": data["apr"] / 100}
        return result

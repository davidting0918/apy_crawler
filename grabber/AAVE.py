import requests


class Client(object):
    def __init__(self):
        self.endpoint = "https://aave-api-v2.aave.com"

    def get_tvl(self, base=None):

        url = self.endpoint + "/data/tvl"
        res = requests.get(url).json()
        return res

    def get_currency_apy(self, currency=None):
        url = self.endpoint + "/data/markets-data"
        res = requests.get(url).json()
        reserve = res["reserves"]
        return reserve


client = Client()
tvl = client.get_tvl()
market_data = client.get_currency_apy()
pass

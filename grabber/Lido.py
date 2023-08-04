import requests


class Client(object):
    def __init__(self):
        self.endpoint = "https://eth-api.lido.fi/v1"

    def get_tvl(self, base=None):

        pass

    def get_currency_apy_last(self, currency="steth"):
        
        url = self.endpoint + f"/protocol/{currency}/apr/last"
        res = requests.get(url).json()
        
        return res


client = Client()
market_data = client.get_currency_apy_last("usdt")
pass

import requests


class Client(object):
    def __init__(self):
        self.endpoint = "https://openapi.just.network"

    def get_tvl(self, base=None):

        pass

    def get_currency_apy(self, currency=None):
        url = self.endpoint + "/lend/jtoken"
        res = requests.get(url).json()
        
        return res


client = Client()
market_data = client.get_currency_apy()
pass

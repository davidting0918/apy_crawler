import requests

class Client(object):
    
    def __init__(self):
        self.apy_end_point = "https://yields.llama.fi"
        self.basic_end_point = "https://api.llama.fi"
        pass
    
    def get_apy(self, currency=None):
        url = self.apy_end_point + '/pools'
        res = requests.get(url).json()
        apys = res['data']
        return apys
    
    def get_tvl(self, chain=None):
        url = self.basic_end_point + "/protocols"
        protocols = requests.get(url).json()
        return protocols
    
    
client = Client()
apy = client.get_tvl()
pass
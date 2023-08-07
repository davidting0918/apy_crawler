from datetime import datetime as dt

import requests


class DefiLlama(object):
    def __init__(self):
        self.apy_end_point = "https://yields.llama.fi"
        self.basic_end_point = "https://api.llama.fi"

        self.protocol_slug_map = {
            "AAVE": ["aave-v2", "aave-v3", "aave-v1", "aave-arc"],
            "Lido": ["lido"],
            "JustLend": ["justlend"],
            "Compound": ["compound", "compound-v3"],
        }

    def get_apy(self, currency=None):
        url = self.apy_end_point + "/pools"
        res = requests.get(url).json()
        apys = res["data"]
        return apys

    def get_tvl(self, protocol=None):
        url = self.basic_end_point + "/protocols"
        raw_data = requests.get(url).json()

        timestamp = dt.now()
        if protocol not in self.protocol_slug_map.keys():
            return None
        result = {"timestamp": timestamp, "protocol": protocol, "tvl": 0}

        for i in self.protocol_slug_map[protocol]:
            protocol_data = [g for g in raw_data if g["slug"] == i][0]
            result["tvl"] += protocol_data["tvl"]

        return result

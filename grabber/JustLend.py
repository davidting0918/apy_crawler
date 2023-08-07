from datetime import datetime as dt

import requests


class JustLend(object):
    def __init__(self):
        self.endpoint = "https://openapi.just.network"

    def get_tvl(self, base=None):

        pass

    def get_currency_apy(self, currency=None):
        timestamp = dt.now()
        url = self.endpoint + "/lend/jtoken"
        res = requests.get(url).json()
        data = res["data"]["tokenList"]

        # clean data
        columns = ["underlyingSymbol", "borrowRate", "supplyRate", "totalBorrows", "totalSupply"]
        result = []
        if currency is None:
            for i in data:
                currency_result = {column: i[column] for column in columns}
                currency_result["timestamp"] = timestamp
                result.append(currency_result)

            return result

        else:
            currency = currency.upper()
            for i in data:
                if i["underlyingSymbol"] == currency:
                    result = {column: i[column] for column in columns}
                    result["timestamp"] = timestamp
                    return result

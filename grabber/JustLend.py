import requests


class JustLendClient(object):
    def __init__(self):
        self.endpoint = "https://openapi.just.network"

    def get_tvl(self, base=None):

        pass

    def get_currency_apy(self, currency=None):
        url = self.endpoint + "/lend/jtoken"
        res = requests.get(url).json()
        data = res['data']['tokenList']
        
        # clean data
        columns = ['symbol', 'borrowRate', 'supplyRate', 'totalBorrows', 'totalSupply']
        result = []
        if currency is None:
            for i in data:
                i['symbol'] = i['symbol'][1:]
                result.append({column: i[column] for column in columns})
                
            return result
        
        else:
            currency = currency.upper()
            for i in data:
                i['symbol'] = i['symbol'][1:]
                if i['symbol'] == currency:
                    result.append({column: i[column] for column in columns})
                    return result

from requests import Request, Session
import json
import pprint # pprint.pprint to get json data ordered

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'1df34fcc-c5d1-4b7d-8650-9cd124daccb1'
}

BTCparameters = {
    'slug':'bitcoin',
    'convert':'USD'
}

BTC_path_number = "1"

ETHparameters = {
    'slug':'ethereum',
    'convert':'USD'
}

ETH_path_number = "1027"

SLPparameters = {
    'slug':'smooth-love-potion',
    'convert':'USD'
}

SLP_path_number = "5824"

def number_max_length(number, nb_length):
    str_number = str(number)
    
    if len(str_number) -1 < nb_length:
        nb_length = len(str_number) -1

    result_list = []
    for i in range(nb_length):
        result_list.append(str_number[i])
    return "".join(result_list)


def get_token_price(parameters, path):
    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    token_price = json.loads(response.text)['data'][path]['quote']['USD']['price']
    return number_max_length(token_price, 8)


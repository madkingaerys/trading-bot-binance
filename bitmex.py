import requests
from pprint import pprint


def get_contracts():
    response = requests.get("https://www.bitmex.com/api/v1/instrument/active")
    contracts = []
    for instrument in response.json():
        contracts.append(instrument['symbol'])

    return contracts
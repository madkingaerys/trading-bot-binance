import logging
import requests
import pprint

logger = logging.getLogger()

#"https://testnet.binancefuture.com"

#"wss://fstream.binance.com"


def get_contracts():
    response = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
    print(response.status_code)

    contracts = []

    for contract in response.json()['symbols']:
        contracts.append(contract['pair'])

    return contracts

print(get_contracts())
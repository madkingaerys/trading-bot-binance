import tkinter as tk
import logging
from pprint import pprint
from connectors.binance_futures import BinanceFuturesClient


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':
    api_keys = dict()

    file = open("api.txt", "r")
    for l in file.readlines():
        pair = l.split("=")
        api_keys[pair[0]] = pair[1].rstrip()

    binance = BinanceFuturesClient(api_keys['binance_testnet_public'],
                                   api_keys['binance_testnet_secret'],
                                   True)

    #root = tk.Tk()
    #root.mainloop()

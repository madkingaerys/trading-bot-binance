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

    binance = BinanceFuturesClient("ecbbe007e060c1f74cc6c87dd891fe3c63e03024bc12890b35931d538cb5a892",
                                   "b969281bd0f45700c78394b6784c47395c651cdc45e96a91e548f131de01cb65",
                                   True)
    root = tk.Tk()
    root.mainloop()

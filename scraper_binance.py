import time

import requests
import pandas as pd
from datetime import datetime


class BinanceDataHolder:
    def __init__(self):
        self.data: list[dict] = []


    def parse_data(self):
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()
        self.data.append({
            "currency": r["symbol"],
            "price": r["price"],
            "time": str(datetime.now())
        })

    def print_dataframe(self):
        print(self.dataframe)


if __name__ == '__main__':
    dataholder = BinanceDataHolder()
    for i in range(30):
        dataholder.parse_data()
        time.sleep(1)

    for el in dataholder.data:
        print("time:", el["time"], "price:", el["price"])


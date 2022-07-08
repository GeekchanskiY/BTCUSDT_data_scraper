import time

import requests
from database import DB
from datetime import datetime


class BinanceDataScraper:
    def __init__(self, database: DB):
        self.data: list[dict] = []
        self.database: DB = database

    def parse_data(self):
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()
        self.database.add_price(symbol=r["symbol"], date=str(datetime.now()), price=r["price"])


if __name__ == '__main__':
    db = DB()
    dataholder = BinanceDataScraper(db)
    while True:
        try:
            dataholder.parse_data()
        except Exception as e:
            print(str(e))
        print(len(list(db.cur.execute('SELECT * FROM price_data'))))
        time.sleep(60)




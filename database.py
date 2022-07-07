import sqlite3


class DB:
    def __init__(self):
        self.con: sqlite3.Connection = sqlite3.connect('data.db')
        self.cur: sqlite3.Cursor = self.con.cursor()
        try:
            self.cur.execute('''CREATE TABLE price_data
                           (datetime text, symbol text, price real)''')
        except sqlite3.OperationalError:
            pass
        try:
            self.cur.execute('''CREATE TABLE news_data
                           (date text, symbol text, title text, link text, time: text)''')
        except sqlite3.OperationalError:
            pass
        self.con.commit()

    def add_price(self, symbol: str, date: str, price: float):
        self.cur.execute(f"INSERT INTO price_data VALUES ('{date}', '{symbol}', {price})")
        self.con.commit()

    def add_news(self, symbol: str, date: str, time: str, link: str, text: str):
        self.cur.execute(f"INSERT INTO news_data VALUES ('{date}', '{symbol}', '{text}', '{link}', '{time}')")
        self.con.commit()

    def print_prices(self):
        for row in self.cur.execute('SELECT * FROM price_data'):
            print(row)


if __name__ == '__main__':
    database: DB = DB()
    database.print_prices()

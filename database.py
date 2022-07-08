import sqlite3


class DB:
    def __init__(self):
        self.con: sqlite3.Connection = sqlite3.connect('data.db')
        self.cur: sqlite3.Cursor = self.con.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS price_data
                       (datetime text, symbol text, price real)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS news_data
                           (date text, symbol text, title text, link text, time text,
                           CONSTRAINT link_unique UNIQUE (link))''')

        self.con.commit()

    def add_price(self, symbol: str, date: str, price: float):
        self.cur.execute(f"INSERT INTO price_data VALUES ('{date}', '{symbol}', {price})")
        self.con.commit()

    def add_news(self, symbol: str, date: str, time: str, link: str, text: str):
        self.cur.execute(f"INSERT OR IGNORE INTO news_data VALUES ('{date}', '{symbol}', '{text}', '{link}', '{time}')")
        self.con.commit()

    def print_prices(self):
        for row in self.cur.execute('SELECT * FROM price_data'):
            print(row)

    def print_news(self):
        for row in self.cur.execute('SELECT link FROM news_data'):
            print(row)


if __name__ == '__main__':
    database: DB = DB()
    database.print_news()

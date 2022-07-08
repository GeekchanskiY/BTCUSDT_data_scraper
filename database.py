import sqlite3
import pandas


class DB:
    def __init__(self):
        self.con: sqlite3.Connection = sqlite3.connect('data.db')
        self.cur: sqlite3.Cursor = self.con.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS price_data
                       (datetime text, symbol text, price real)''')
        self.cur.execute('''CREATE INDEX IF NOT EXISTS data_idx ON price_data (datetime)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS news_data
                           (date text, symbol text, title text, link text, time text,
                           CONSTRAINT link_unique UNIQUE (link))''')
        self.cur.execute('''CREATE INDEX IF NOT EXISTS news_idx ON news_data (date)''')

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

    def get_prices_dataframe(self):
        dataframe = pandas.read_sql_query("SELECT * FROM price_data", self.con)
        print(dataframe)
        return dataframe

    def get_news_dataframe(self):
        dataframe = pandas.read_sql_query("SELECT * FROM news_data", self.con)
        print(dataframe)
        return dataframe


if __name__ == '__main__':
    database: DB = DB()
    database.get_news_dataframe()

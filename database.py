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
        self.cur.execute(f"INSERT INTO price_data VALUES (?, ?, ?)",
                         (date, symbol, price))
        self.con.commit()

    def add_news(self, symbol: str, date: str, time: str, link: str, text: str):
        self.cur.execute(f"INSERT OR IGNORE INTO news_data VALUES (?, ?, ?, ?, ?)",
                         (date, symbol, text, link, time))
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

    def create_table(self):
        output_str: str = ""
        news: str = ""
        with open("app.html", "r", encoding="utf-8") as f:
            template: str = f.read()
        for row in self.cur.execute('SELECT * FROM price_data'):
            date: str = row[0]
            price: float = row[2]
            news: str = ""

            output_str += "{price: " + str(price) + ", date_str: '" + date.replace(" ", 'T') + "'},"
        for row2 in self.cur.execute('SELECT * FROM news_data'):
            news += "{date: '" + row2[0] + "T" + row2[4] + "', title: \"" + row2[2].replace("\"", " ")\
                .replace("'", " ") + "\", link: '" + row2[3] + "'},"
        print(output_str)
        output_template = template.replace("/*DATA_TO_IMPORT HERE*/", output_str)\
            .replace("/*NEWS_TO_IMPORT_HERE*/", news)
        with open("output.html", "w", encoding="utf-8") as f:
            f.write(output_template)


if __name__ == '__main__':
    database: DB = DB()
    database.create_table()

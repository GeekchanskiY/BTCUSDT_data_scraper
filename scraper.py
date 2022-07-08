import time

from scraper_utoday import get_utoday_news
from scraper_bitcoin import get_bitcoin_news
from scraper_decrypt import get_decrypt_news
from scraper_dailyhodl import get_dailyhold_news
from scraper_binance import BinanceDataScraper

from database import DB

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class ScrapersHandler:
    def __init__(self, delay_minutes: int):
        self.driver: webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.db: DB = DB()
        self.binance_data_scraper = BinanceDataScraper(self.db)
        self.mainloop(delay_minutes*60)

    def mainloop(self, delay_seconds: int):
        while True:
            self.binance_data_scraper.parse_data()
            self.scrap_all_selenium()
            self.scrap_all_requests()
            time.sleep(delay_seconds)

    def scrap_all_selenium(self):
        data = get_dailyhold_news(self.driver)
        self.add_news_to_db(data)
        data = get_bitcoin_news(self.driver)
        self.add_news_to_db(data)
        data = get_decrypt_news(self.driver)
        self.add_news_to_db(data)

    def scrap_all_requests(self):
        data = get_utoday_news()
        self.add_news_to_db(data)

    def add_news_to_db(self, data: list[dict]):
        for d in data:
            self.db.add_news(
                symbol="BTCUSDT",
                date=d["date"],
                time=d["time"],
                link=d["link"],
                text=d["name"]
            )


if __name__ == '__main__':
    scraper = ScrapersHandler(10)
    scraper.scrap_all_selenium()

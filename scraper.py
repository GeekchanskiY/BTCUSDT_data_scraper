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
    def __init__(self):
        self.driver: webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.db: DB = DB()

    def scrap_all_selenium(self):
        data = get_dailyhold_news(self.driver)
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
    scraper = ScrapersHandler()
    scraper.scrap_all_selenium()

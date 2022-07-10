import time

from scraper_utoday import get_utoday_news
from scraper_bitcoin import get_bitcoin_news
from scraper_decrypt import get_decrypt_news
from scraper_dailyhodl import get_dailyhold_news
from scraper_cointelagraph import get_cointelegraph_news
from scraper_coingape import get_coingape_news
from scraper_theblock import get_theblock_news
from scraper_bitcoinmagazine import get_bitcoinmagazine_news
from scraper_blockworks import get_blockworks_news
from scraper_bitcoinist import get_bitcoinist_news
# from scraper_cryptopotato import get_cryptopotato_news
from scraper_beincrypto import get_beincrypto_news


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
            self.driver.quit()
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            time.sleep(delay_seconds)

    def scrap_all_selenium(self):
        try:
            data = get_dailyhold_news(self.driver)
            self.add_news_to_db(data)
        except Exception as e:
            print(f"dailyHodl error {str(e)}")
        try:
            data = get_bitcoin_news(self.driver)
            self.add_news_to_db(data)
        except Exception as e:
            print(f"bitcoin error {str(e)}")
        try:
            data = get_decrypt_news(self.driver)
            self.add_news_to_db(data)
        except Exception as e:
            print(f"decrypt error {str(e)}")
        try:
            data = get_cointelegraph_news(self.driver)
            self.add_news_to_db(data)
        except Exception as e:
            print(f"cointelegraph error {str(e)}")
        try:
            data = get_coingape_news(self.driver)
            self.add_news_to_db(data)
        except Exception as e:
            print(f"coingape error {str(e)}")

        try:
            data = get_theblock_news(self.driver)
            self.add_news_to_db(data)
        except Exception as e:
            print(f"theblock error {str(e)}")

        try:
            data = get_blockworks_news(self.driver)
            self.add_news_to_db(data)
        except Exception as e:
            print(f"blockworks error {str(e)}")

    def scrap_all_requests(self):
        data = get_utoday_news()
        self.add_news_to_db(data)
        data = get_bitcoinmagazine_news()
        self.add_news_to_db(data)
        # Cryptopotato is not available at the moment

        #data = get_cryptopotato_news()
        #self.add_news_to_db(data)

        data = get_beincrypto_news()
        self.add_news_to_db(data)
        data = get_bitcoinist_news()
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

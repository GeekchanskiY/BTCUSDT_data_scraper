from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dateutil.relativedelta import relativedelta
import datetime


def get_coingape_news(driver: webdriver):
    output_data: list[dict] = []
    driver.get("https://coingape.com/category/news/bitcoin-news/")
    articles = driver.find_elements(By.TAG_NAME, "article")
    for article in articles:
        date = article.find_element(By.CLASS_NAME, "entry-meta-date").text
        try:
            date = datetime.datetime.strptime(date, "%b %d, %Y")
        except Exception as e:
            date = datetime.date.today()

        date_str = date.strftime("%Y-%m-%d")
        time_str = date.strftime("%H:%M")
        output_data.append({
            "link": article.find_elements(By.TAG_NAME, "a")[1].get_attribute("href"),
            "name": article.find_element(By.TAG_NAME, "h3").text,
            "date": date_str,
            "time": time_str
        })
    return output_data


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    data = get_coingape_news(driver)
    print(data)

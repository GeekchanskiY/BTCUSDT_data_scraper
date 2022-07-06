import time
import undetected_chromedriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_cryptopotato_news() -> list[dict]:
    output_data: list[dict] = []
    driver = undetected_chromedriver.Chrome()


    driver.get("https://cryptopotato.com/?s=bitcoin")
    time.sleep(5)
    articles = driver.find_elements(By.CLASS_NAME, "article")
    print(len(articles))
    return output_data


if __name__ == '__main__':
    data = get_cryptopotato_news()
    print(data)
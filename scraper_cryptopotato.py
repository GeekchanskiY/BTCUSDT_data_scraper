import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_cryptopotato_news(driver: webdriver) -> list[dict]:
    output_data: list[dict] = []
    driver.get("https://cryptopotato.com/?s=bitcoin")
    handle = driver.current_window_handle
    driver.service.stop()
    time.sleep(6)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://cryptopotato.com/?s=bitcoin")
    time.sleep(5)
    articles = driver.find_elements(By.CLASS_NAME, "article")
    print(len(articles))
    return output_data

if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    data = get_cryptopotato_news(driver)
    print(data)
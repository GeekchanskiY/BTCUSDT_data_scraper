from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_decrypt_news(driver: webdriver) -> list[dict]:
    driver.get("https://decrypt.co/search/all/bitcoin")


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    data = get_decrypt_news(driver)
    print(data)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime


def get_decrypt_news(driver: webdriver) -> list[dict]:
    import time
    output_data: list[dict] = []
    driver.get("https://decrypt.co/search/all/bitcoin")
    time.sleep(1)
    articles = driver.find_elements(By.CLASS_NAME, "block")
    for article in articles:
        try:
            date = article.find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0]
            time = article.find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[1]
            time = "{}:{}".format(time.split(":")[0], time.split(":")[1])
        except:
            continue
        output_data.append({
            "name": article.find_element(By.TAG_NAME, "h2").text,
            "link": article.get_attribute("href"),
            "date": date,
            "time": time
        })

    return output_data


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    data = get_decrypt_news(driver)
    print(data)

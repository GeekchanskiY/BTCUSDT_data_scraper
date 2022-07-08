from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime


def get_dailyhold_news(driver: webdriver) -> list[dict]:
    output_data: list[dict] = []
    driver.get("https://dailyhodl.com/bitcoin-news/")
    articles = driver.find_elements(By.TAG_NAME, "article")
    for article in articles:
        time = article.find_element(By.CLASS_NAME, "jeg_meta_date").text
        print(time)
        date = datetime.strptime(time, "%B %d, %Y")
        output_data.append({
            "date": date.strftime("%Y-%m-%d"),
            "name": article.find_element(By.TAG_NAME, "h3").text,
            "link": article.find_element(By.TAG_NAME, "a").get_attribute("href"),
            "time": datetime.strftime(datetime.now(), "%H:%M")
        })

    return output_data


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    data = get_dailyhold_news(driver)
    print(data)

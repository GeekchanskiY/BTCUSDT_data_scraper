from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime


def get_blockworks_news(driver: webdriver) -> list[dict]:
    output_data: list[dict] = []
    driver.get("https://blockworks.co/news/")
    articles = driver.find_elements(By.CLASS_NAME, "card")
    for article in articles:
        date_str = article.find_element(By.CLASS_NAME, "post-creation-details").text.split(" / ")[-1]
        date_str = date_str.replace(" EDT", "")
        try:
            date = datetime.datetime.strptime(date_str, "%B %d, %Y, %H:%M %p")
        except ValueError:
            continue
        output_data.append({
            "name": article.find_element(By.CLASS_NAME, "card_title").text,
            "link": article.find_element(By.TAG_NAME, "a").get_attribute("href"),
            "date": date.strftime("%Y-%m-%d"),
            "time": date.strftime("%H:%M")
        })
    return output_data


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    data = get_blockworks_news(driver)
    print(data)
        
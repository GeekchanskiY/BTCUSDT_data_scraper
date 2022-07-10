from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime


def get_theblock_news(driver: webdriver) -> list[dict]:
    output_data: list[dict] = []
    driver.get("https://www.theblock.co/search?query=bitcoin")
    articles = driver.find_elements(By.TAG_NAME, "article")
    for article in articles:
        date = article.find_element(By.CLASS_NAME, "pubDate").text.replace("PM", " PM").replace("AM", " AM")\
            .replace("EDT", "")
        while True:
            if date[-1] == " ":
                date = date[:-1]
            else:
                break
        date = datetime.datetime.strptime(date, "%B %d, %Y, %H:%M %p")
        output_data.append({
            "link": article.find_element(By.TAG_NAME, "a").get_attribute("href"),
            "text": article.find_element(By.TAG_NAME, "h2").text,
            "date": date.strftime("%Y-%m-%d"),
            "time": date.strftime("%H:%M")
        })
    return output_data


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    data = get_theblock_news(driver)
    print(data)
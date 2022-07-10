from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime


def get_cointelegraph_news(driver: webdriver) -> list[dict]:
    """
        Get bitcoin news from https://cointelegraph.com/
    :param driver:
    :return:
    """
    output_data: list = []
    driver.get("https://cointelegraph.com/tags/bitcoin")
    articles = driver.find_elements(By.CLASS_NAME, "post-card-inline")
    for article in articles:
        output_data.append(
            {
                "link": article.find_element(By.TAG_NAME, "a").get_attribute("href"),
                "name": article.find_element(By.CLASS_NAME, "post-card-inline__title").text,
                "date": article.find_element(By.CLASS_NAME, "post-card-inline__date").get_attribute("datetime"),
                "time": datetime.now().strftime("%H:%M")
            }
        )

    return output_data


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    data = get_cointelegraph_news(driver)
    print(data)

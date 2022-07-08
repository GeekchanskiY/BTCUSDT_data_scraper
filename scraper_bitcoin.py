from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dateutil.relativedelta import relativedelta
from selenium.common.exceptions import NoSuchElementException
import datetime


def get_past_date(str_days_ago):
    TODAY = datetime.date.today()
    splitted = str_days_ago.split()
    if len(splitted) == 1 and splitted[0].lower() == 'today':
        return TODAY
    elif len(splitted) == 1 and splitted[0].lower() == 'yesterday':
        date = TODAY - relativedelta(days=1)
        return date
    elif splitted[1].lower() in ['hour', 'hours', 'hr', 'hrs', 'h']:
        date = datetime.datetime.now() - relativedelta(hours=int(splitted[0]))
        return date
    elif splitted[1].lower() in ['day', 'days', 'd']:
        date = TODAY - relativedelta(days=int(splitted[0]))
        return date
    elif splitted[1].lower() in ['wk', 'wks', 'week', 'weeks', 'w']:
        date = TODAY - relativedelta(weeks=int(splitted[0]))
        return date
    elif splitted[1].lower() in ['mon', 'mons', 'month', 'months', 'm']:
        date = TODAY - relativedelta(months=int(splitted[0]))
        return date
    elif splitted[1].lower() in ['yrs', 'yr', 'years', 'year', 'y']:
        date = TODAY - relativedelta(years=int(splitted[0]))
        return date
    else:
        return "Wrong Argument format"


def get_bitcoin_news(driver: webdriver) -> list[dict]:
    output_data: list[dict] = []
    driver.get("https://news.bitcoin.com/")
    articles = driver.find_elements(By.CLASS_NAME, "story")
    for article in articles:
        try:
            date_ago = get_past_date(article.find_element(By.CLASS_NAME, "story__footer")
                                     .find_element(By.TAG_NAME, "span").text)
        except (IndexError, NoSuchElementException):
            continue

        if date_ago == "Wrong Argument format":
            date_ago = datetime.datetime.now()
        output_data.append({
            "link": article.find_element(By.TAG_NAME, "a").get_attribute("href"),
            "name": article.find_element(By.CLASS_NAME, "story__title").text,
            "date": date_ago.strftime("%Y-%m-%d"),
            "time": date_ago.strftime("%H:%M")
        })
    return output_data


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    data = get_bitcoin_news(driver)
    print(data)

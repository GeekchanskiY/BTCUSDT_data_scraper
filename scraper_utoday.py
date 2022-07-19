import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_utoday_news() -> list[dict]:
    output_data: list[dict] = []
    r = requests.get("https://u.today/bitcoin-news").text
    soup = BeautifulSoup(r, 'html.parser')
    articles = soup.find_all("div", attrs={"class": "category-item"})
    for article in articles:
        try:
            time = datetime.strptime(article.find("div", attrs={"class": "humble--time"}).text, "%m/%d/%Y - %H:%M")
        except ValueError:
            continue
        output_data.append(
            {
                "name": article.find("div", attrs={"class": "category-item__title"}).text,
                "link": article.find("a", attrs={"class": "category-item__title-link"})["href"],
                "date": datetime.strftime(time, "%Y-%m-%d"),
                "time": datetime.strftime(time, "%H:%M")
            }
        )

    return output_data


if __name__ == '__main__':
    data = get_utoday_news()
    print(data)
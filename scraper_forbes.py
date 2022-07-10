import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_forbes_news() -> list[dict]:
    output_data: list[dict] = []
    r = requests.get("https://www.forbes.com/search/?q=bitcoin")
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.find_all("article")
    for article in articles:
        date_str = article.find("div", attrs={"class": "stream-item__date"}).text
        try:
            date = datetime.strptime(date_str, "%b %d, %Y")
        except ValueError:
            date = datetime.now()
        output_data.append({
            "name": article.find("a").text,
            "link": article.find("a")["href"],
            "date": date.strftime("%Y-%m-%d"),
            "time": date.strftime("%H:%M")
        })
    return output_data


if __name__ == '__main__':
    data = get_forbes_news()
    print(data)
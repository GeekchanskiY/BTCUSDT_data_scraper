import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_bitcoinmagazine_news() -> list[dict]:
    output_data: list[dict] = []
    r = requests.get("https://bitcoinmagazine.com/articles").text
    soup = BeautifulSoup(r, 'html.parser')
    articles = soup.find_all("div", attrs={"class": "l-grid--item"})
    for article in articles:
        try:
            date = datetime.strptime(article.find("span", attrs={"class": "mm-card--metadata-text"}).text, "%b %d, %Y")
        except (ValueError, AttributeError):
            date = datetime.now()
        output_data.append({
            "name": article.find("h2").text,
            "link": "https://bitcoinmagazine.com"+article.find("a")["href"],
            "date": date.strftime("%Y-%m-%d"),
            "time": date.strftime("%H:%M")
        })
    return output_data


if __name__ == '__main__':
    print(get_bitcoinmagazine_news())
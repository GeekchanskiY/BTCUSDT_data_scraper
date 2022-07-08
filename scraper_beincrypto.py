import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_beincrypto_news() -> list:
    output_data: list[dict] =[]
    r = requests.get("https://beincrypto.com/page/1/?s=bitcoin").text
    soup = BeautifulSoup(r, 'html.parser')
    cards = soup.find_all("article", attrs={"class": "multi-news-card"})
    for card in cards:
        date = datetime.strptime(card.find("span", attrs={"class": "date"}).text, "%b %d, %Y")
        str_date = date.strftime("%Y-%m-%d")
        output_data.append(
            {
                "link": card.find("a")["href"],
                "name": card.find("div", attrs={"class": "title"}).text.replace("\n", ""),
                "date": str_date,
                "time": datetime.now().strftime("%H:%M")
            }
        )
    return output_data


if __name__ == '__main__':
    a = get_beincrypto_news()
    print(a)

import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_bitcoinist_news() -> list[dict]:
    output_data: list[dict] = []
    r = requests.get("https://bitcoinist.com/category/bitcoin/")
    soup = BeautifulSoup(r.text, "html.parser")
    articles = soup.find_all("article", attrs={"class": "jeg_post"})
    for article in articles:
        date_str = article.find("div", attrs={"class": "jeg_meta_date"}).text
        date = datetime.strptime(date_str, " %B %d, %Y")
        output_data.append({
            "name": article.find("h3", attrs={"class": "jeg_post_title"}).text.replace("\n", ""),
            "link": article.find("a")["href"],
            "date": datetime.strftime(date, "%Y-%m-%d"),
            "time": datetime.strftime(date, "%H:%M")
        })
    return output_data


if __name__ == '__main__':
    data = get_bitcoinist_news()
    print(data)

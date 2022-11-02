from pprint import pprint

from bs4 import BeautifulSoup as BS
import requests
URL = "https://ru.pyramida.kg/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_="col-lg-4 col-md-6")
    news = []
    for item in items:
        new = ({
            'name': item.find('div', class_="text-wrap").find('a').getText(),
            'link': item.find('div', class_="text-wrap").find('a').get('href'),
            'img': item.find('div', class_="news-item").find('a').get('href')
        })
        news.append(new)
    pprint(news)
    return news
html = get_html(URL)

get_data(html.text)



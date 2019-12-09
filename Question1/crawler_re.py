import re
import requests
from bs4 import BeautifulSoup

req = requests.get('https://news.ycombinator.com/')

html = req.text
soup = BeautifulSoup(html, 'html.parser')
news_table = soup.find('table', {'class': 'itemlist'})
itemlist = news_table.find_all('tr', {'class': 'athing'})

article_list = {"article_list": []}

for item in itemlist:
    posting = item.find_all('td')
    ranking = posting[0].get_text()[:-1]
    original_title = posting[-1].find('a').get_text()
    preprocessed_title = r'{}'.format(original_title)
    preprocessed_title = re.sub(r'[\\\/:*?"<>|]', '', preprocessed_title)
    link = posting[-1].find('a').attrs['href']

    article_list["article_list"].append({'ranking': ranking,
                                         'original_title': original_title,
                                         'preprocessed_title': preprocessed_title,
                                         'link': link})

    req = requests.get(link)
    filename = f"{ranking}.{preprocessed_title}.html"
    f = open(filename, "w", encoding='utf-8')
    f.write(req.text)
    f.close()

for article in article_list['article_list']:
    print(f"글 랭크: {article['ranking']}")
    print(f"글 제목: {article['original_title']}")
    print(f"글 링크: {article['link']}")
    
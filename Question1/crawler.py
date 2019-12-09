import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

req = requests.get('https://news.ycombinator.com/')

html = req.text
soup = BeautifulSoup(html, 'html.parser')
news_table = soup.find('table', {'class': 'itemlist'})

for row in news_table.find_all('tr'):
    col = row.find_all('td')
    title = col[2].contents[0].contents
    link = col[2].contents[0].find(attrs={'class': 'storylink'})
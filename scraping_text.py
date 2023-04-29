from bs4 import BeautifulSoup
import requests

url = 'https://www.ifo.de/pressemitteilung/2023-04-20/mehr-stornierungen-im-wohnungsbau'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('meta', attrs={'name': 'twitter:title'})['content']
text_list = soup.find_all('p')
text = " ".join([t.get_text() for t in text_list])

print(title)
print(text)

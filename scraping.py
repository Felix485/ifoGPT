from bs4 import BeautifulSoup
import requests

url = 'https://www.ifo.de/pressemitteilung/2023-04-28/konsum-und-industrie-senden-gegensaetzliche-impulse-fuer-deutsche'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

img_tags = soup.find_all('img')
img_urls = [img.get('data-src') for img in img_tags]

print(img_urls)
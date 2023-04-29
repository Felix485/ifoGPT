from bs4 import BeautifulSoup
import requests
import os


def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Image saved to {save_path}")
    except Exception as e:
        print(f"Error downloading image from {url}: {e}")


url = 'https://www.ifo.de/pressemitteilung/2023-04-28/konsum-und-industrie-senden-gegensaetzliche-impulse-fuer-deutsche'
#url = 'https://www.ifo.de/fakten/2023-04-27/ifo-geschaeftsklima-ostdeutschland-index-gestiegen-april-2023'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

img_tags = soup.find_all('img')
img_urls = [img.get('data-src') for img in img_tags]
img_urls = [url for url in img_urls if url is not None]


print(img_urls)


save_directory = "downloaded_images"
cv_directory = "cv_images"
graphic_directory = "graphic_images"

if not os.path.exists(save_directory):
    os.makedirs(save_directory)
if not os.path.exists(os.path.join(save_directory, cv_directory)):
    os.makedirs(os.path.join(save_directory, cv_directory))
if not os.path.exists(os.path.join(save_directory, graphic_directory)):
    os.makedirs(os.path.join(save_directory, graphic_directory))

# Download the images
for url in img_urls:
    url = url.split("?")[0]
    filename = os.path.basename(url)
    if filename.startswith("cvfoto"):
        save_path = os.path.join(save_directory, cv_directory, filename)
    else:
        save_path = os.path.join(save_directory, graphic_directory, filename)
    download_image(url, save_path)



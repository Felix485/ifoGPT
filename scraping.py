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


#url = 'https://www.ifo.de/pressemitteilung/2023-04-28/konsum-und-industrie-senden-gegensaetzliche-impulse-fuer-deutsche'



def scrapeurl(url):
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

    directory = os.path.join(save_directory, cv_directory)

    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Loop through the files and delete each one
    for file in files:
        # Construct the full file path
        file_path = os.path.join(directory, file)

        # Check if the file is a file (not a subdirectory)
        if os.path.isfile(file_path):
            # Delete the file
            os.remove(file_path)

    directory = os.path.join(save_directory, graphic_directory)

    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Loop through the files and delete each one
    for file in files:
        # Construct the full file path
        file_path = os.path.join(directory, file)

        # Check if the file is a file (not a subdirectory)
        if os.path.isfile(file_path):
            # Delete the file
            os.remove(file_path)

    # Download the images
    for url in img_urls:
        url = url.split("?")[0]
        filename = os.path.basename(url)
        if filename.startswith("cvfoto"):
            save_path = os.path.join(save_directory, cv_directory, filename)
        else:
            save_path = os.path.join(save_directory, graphic_directory, filename)
        download_image(url, save_path)


    # Text
    title = soup.find('meta', attrs={'name': 'twitter:title'})['content']
    text_list = soup.find_all('p')
    text = " ".join([t.get_text() for t in text_list])

    return text

from bs4 import BeautifulSoup
import requests
import os
import re


def download_image(image_url, save_path):
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Image saved to {save_path}")
    except Exception as e:
        print(f"Error downloading image from {image_url}: {e}")


def scrape_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    img_tags = soup.find_all('img')
    img_urls = [img.get('data-src') for img in img_tags]
    img_urls = [url for url in img_urls if url is not None]

    print(img_urls)

    save_directory = "downloaded_images"
    cv_directory = "cv_images"
    graphic_directory = "graphic_images"
    output_directory = "output_image"

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    if not os.path.exists(os.path.join(save_directory, cv_directory)):
        os.makedirs(os.path.join(save_directory, cv_directory))
    if not os.path.exists(os.path.join(save_directory, graphic_directory)):
        os.makedirs(os.path.join(save_directory, graphic_directory))
    if not os.path.exists(os.path.join(save_directory, output_directory)):
        os.makedirs(os.path.join(save_directory, output_directory))

    # Clear old files in the cv_images and graphic_images directories
    for dir_name in [cv_directory, graphic_directory]:
        directory = os.path.join(save_directory, dir_name)

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

    # Scrape text
    title = soup.find('meta', attrs={'name': 'twitter:title'})['content']
    text_list = soup.find_all('p')
    text_string = " ".join([t.get_text() for t in text_list])
    text = title + text_string
    citations = re.findall(r'„(.*?)“', text)

    return text, citations

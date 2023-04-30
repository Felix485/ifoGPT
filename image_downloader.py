import requests
import os

# Read the API key from the file
with open('pexels.txt', 'r') as file:
    api_key = file.read().strip()


def download_pexels_image(query, number=0):
    """
    Download an image from Pexels based on a given query.

    :param query: Search query for the image
    :param number: Image number in the search results (default: 0)
    """

    # Create 'stock_images' folder if it doesn't exist

    current_directory = os.getcwd()
    subdirectory = 'downloaded_images'
    temp_directory = os.path.join(current_directory, subdirectory)
    folder_name = 'stock_images'
    stock_images_directory = os.path.join(temp_directory, folder_name)

    if not os.path.exists(stock_images_directory):
        os.makedirs(stock_images_directory)

    # Remove all files in the 'stock_images' folder if number is 0
    if number == 0:
        files = os.listdir(stock_images_directory)

        for file in files:
            file_path = os.path.join(stock_images_directory, file)

            if os.path.isfile(file_path):
                os.remove(file_path)

    # Save the image in the 'stock_images' folder
    file_name = f'image{number}.jpg'
    save_path = os.path.join(stock_images_directory, file_name)

    headers = {'Authorization': api_key}
    url = f'https://api.pexels.com/v1/search?query={query}&per_page=1&page=1'

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    if data['photos']:
        image_url = data['photos'][number]['src']['original']
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f'Image saved as {save_path}')
    else:
        print(f'No images found for query: {query}')

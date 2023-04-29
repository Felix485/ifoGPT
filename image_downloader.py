import requests
import os

def download_pexels_image( query):
    api_key = 'S1TbnIy3DI6LeqZ4xqHOxAYViQFrn1a2laS7xrUKcIfFy4EK7f9w7fzG'
    # Create 'stock images' folder if it doesn't exist
    subdirectory = 'downloaded_images'
    current_directory = os.getcwd()
    temp_directory = os.path.join(current_directory, subdirectory)
    folder_name = 'stock_images'
    temp_directory = os.path.join(temp_directory, folder_name)

    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)

    # Update save_path to point to the 'Temp' folder
    file_name = 'image.jpg'
    save_path = os.path.join(temp_directory, file_name)

    headers = {'Authorization': api_key}
    url = f'https://api.pexels.com/v1/search?query={query}&per_page=1&page=1'

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    if data['photos']:
        image_url = data['photos'][0]['src']['original']
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f'Image saved as {save_path}')
    else:
        print(f'No images found for query: {query}')



#download_pexels_image( "monkey")

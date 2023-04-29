import requests
import os

def download_pexels_image(query, number = 0):
    api_key = 'S1TbnIy3DI6LeqZ4xqHOxAYViQFrn1a2laS7xrUKcIfFy4EK7f9w7fzG'
    # Create 'stock images' folder if it doesn't exist
    subdirectory = 'downloaded_images'
    current_directory = os.getcwd()
    temp_directory = os.path.join(current_directory, subdirectory)
    folder_name = 'stock_images'
    temp_directory = os.path.join(temp_directory, folder_name)

    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)

    if number == 0:
        directory = os.path.join(temp_directory)

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

    # Update save_path to point to the 'Temp' folder
    file_name = 'image' + str(number) +'.jpg'
    save_path = os.path.join(temp_directory, file_name)

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



#download_pexels_image( "monkey")

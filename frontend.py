import streamlit as st
import backend_api
import image_downloader
import scraping
import os
import image_generator
from PIL import Image
import urllib.parse
import base64


def image_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
    return encoded_string


def main():
    # some Styling
    st.image("ifo_logo.png", width=200)
    st.markdown("""
           <style>
               .stApp {
                   background-image: url("https://media.istockphoto.com/id/469182248/de/foto/zeitung-mit-der-überschrift-pressemitteilung.jpg?s=612x612&w=0&k=20&c=3_NyeC_mcGb-ZT40axoq2e5wusnuxf4crCxx0QlRWDw=") !important;
                   background-size: cover !important;
               }
           </style>
           """, unsafe_allow_html=True)
    st.markdown("""
           <style>
               .stApp .main {
                   background-color: rgba(255, 255, 255, 0.9) !important;
                   padding: 20px;
                   border-radius: 10px;
               }
           </style>
           """, unsafe_allow_html=True)
    st.markdown("""
          <style>
              .custom-header {
                  background-color: #0D4080;
                  padding: 20px;
                  text-align: center;
                  font-size: 24px;
                  color: white;
                  font-family: "Helvetica", sans-serif;
                  margin-bottom: 20px;
              }
          </style>
          """, unsafe_allow_html=True)
    st.markdown('<div class="custom-header">ifoGPT</div>', unsafe_allow_html=True)
    st.subheader("A twitter post generator")

    pages = {
        "Generate": generate_page,
        "Edit": edit_page,
    }

    page = st.sidebar.radio("Select a page:", list(pages.keys()))

    # Display the selected page with the session state
    pages[page]()


def generate_page():

    global citations
    global user_link

    user_link = st.text_input("Provide the url of the press release:")

#  Wird gemacht wenn Knopf gedrückt wird
    if st.button("Generate tailored twitter post"):
        user_input, allcitations = scraping.scrape_url(user_link)
        st.session_state.allcitations = allcitations
        result = backend_api.twitter_text(user_input)
        st.session_state.generated_text = result + " " + user_link
        # Stockfoto runterladen
        image_downloader.download_pexels_image("economy",0)
        st.header("Navigate to the Edit page now!")


def edit_page():
    st.header("Edit the twitter post caption, if desired:")
    # Bearbeitbares Textfeld
    if 'generated_text' in st.session_state:
        editable_text = st.text_area("", st.session_state.generated_text, height=200)
        st.header("Choose a picture to accompany the post:")
        # Load images from multiple folders within the 'images' folder
        parent_image_folder = 'downloaded_images'
        subfolders = ['cv_images', 'graphic_images', 'stock_images']  # Replace with the names of your image subfolders

        # create list with all relevant images from all subfolders in downloaded_images
        image_files = []
        selected_images = []  # Initialize an empty list to store selected image paths

        # Create the columns for the images and checkboxes
        col1, col2, col3 = st.columns([1, 2, 1.5])

        for subfolder in subfolders:
            folder_path = os.path.join(parent_image_folder, subfolder)
            image_files.extend([(subfolder, f) for f in os.listdir(folder_path)])
            image_files2 = [f"{parent_image_folder}/{subfolder}/{filename}" for filename in os.listdir(folder_path)]

            # Add a heading for the column
            if subfolder == 'cv_images':
                col1.subheader("Writers")
                column = col1
            elif subfolder == 'graphic_images':
                col2.subheader("Graphs")
                column = col2
            else:
                col3.subheader("Stock Picture")
                column = col3

            for i, image_file in enumerate(image_files2):
                # Load the image and display it in the column
                image = Image.open(image_file)
                column.image(image, use_column_width=True)

                # Display the checkbox with a unique key based on the image filename
                if column.checkbox("", key=f"{subfolder}_{i}_{os.path.basename(image_file)}"):
                    selected_images.append(image_file)  # Add the path of the selected image to the list

        # Users can choose citations they want to include and edit them
        st.header("Select and edit citation(s):")
        selected_citations = []  # Create an empty list to store the selected citations

        # Create a checkbox for each citation and add it to the selected_citations list if it's checked
        for i, citation in enumerate(st.session_state.allcitations):
            checkbox = st.checkbox(citation, key=f"checkbox_{i}")
            if checkbox:
                selected_citations.append(citation)
        selected_citations_str = st.text_area("Edit citations if desired", value="\n".join(selected_citations),
                                              height=150)

    # Create the preview
        if st.button("Update preview"):
            st.header("Preview:")
            st.write(editable_text)
            selected_path = selected_images[0]

            if selected_citations_str == '':
                image = Image.open(selected_path)
                image.save("downloaded_images/output_image/output.png")
                image.close()
            else:
                image_generator.create_image_with_text(input_path=selected_path,text= selected_citations_str,
                                                       output_path="downloaded_images/output_image/output.png")

            # Display the  selected image (first = the selected one)
            if selected_images:
                first_subfolder = "output_image"
                first_image = "output.png"
                first_image_path = os.path.join(parent_image_folder, first_subfolder, first_image)
                first_image_obj = Image.open(first_image_path)
                st.image(first_image_obj)
    # Twitter Button
            st.header("Preview on Twitter")
            st.write("Add image by selecting path: downloaded_images\\output_image\\output.png ")
            encoded_tweet_text = urllib.parse.quote(editable_text)
            twitter_url = f"https://twitter.com/intent/tweet?text={encoded_tweet_text}"
            encoded_twitter_image = image_to_base64("./twitter.png")
            tweet_button = f'<a href="{twitter_url}" target="_blank"><img src="data:image/png;base64,' \
                           f'{encoded_twitter_image}" alt="Tweet" width="50" height="50"/></a>'
            st.markdown(tweet_button, unsafe_allow_html=True)
    else:
        st.write("No generated text to edit. Please go to the Generate page to create a tailored Twitter post.")


if __name__ == "__main__":
    main()
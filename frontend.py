import streamlit as st
import backend_api
import image_downloader
import scraping
import os
import image_generator
from PIL import Image



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

    if st.button("Generate tailored twitter post!"):
        user_input, allcitations = scraping.scrapeurl(user_link)
        with open("citation.txt", "w") as file:
            # Write some text to the file
            file.write(allcitations[0])

        result = backend_api.twitter_text(user_input)
        st.session_state.generated_text = result
        #searchword = backend_api.keyword(result)
        image_downloader.download_pexels_image("economy",0)
        st.write("Navigate to the Edit page now!")


        # Navigate to the Edit page
        #st.sidebar.radio("Select a page:", list(pages.keys()), index=1)

def edit_page():
   # st.write("URL to the original press release: " + user_link)
    st.header("Edit your post:")

    if 'generated_text' in st.session_state:
        editable_text = st.text_area("Edit the post caption:", st.session_state.generated_text)

        # Load images from multiple folders within the 'images' folder
        parent_image_folder = 'downloaded_images'
        subfolders = ['cv_images', 'graphic_images', 'stock_images']  # Replace with the names of your image subfolders

        image_files = []
        for subfolder in subfolders:
            folder_path = os.path.join(parent_image_folder, subfolder)
            image_files.extend([(subfolder, f) for f in os.listdir(folder_path)])

        # Display image previews with checkboxes
        st.write("Select image(s):")
        selected_images = []
        for subfolder, image_file in image_files:
            image_path = os.path.join(parent_image_folder, subfolder, image_file)
            image = Image.open(image_path)

            unique_key = f"{subfolder}-{image_file}"
            col1, col2 = st.columns([1, 4])
            selected = col1.checkbox("", key=unique_key)
            col2.image(image, width=300)

            if selected:
                selected_images.append((subfolder, image_file))
            elif (subfolder, image_file) in selected_images:
                selected_images.remove((subfolder, image_file))

        if st.button("Update preview"):
            st.write("Preview:")
            st.write(editable_text)
            selected_path = "downloaded_images/" + selected_images[0][0] + "/"+ selected_images[0][1]
            # Open the file for reading
            with open("citation.txt", "r") as file:
                # Read the contents of the file into a string variable
                citations = file.read()
            image_generator.create_image_with_text(input_path=selected_path,text= citations, output_path="downloaded_images/output_image/output.png")

            # Display the first selected image
            if selected_images:
                first_subfolder = "output_image"
                first_image = "output.png"
                first_image_path = os.path.join(parent_image_folder, first_subfolder, first_image)
                first_image_obj = Image.open(first_image_path)
                st.image(first_image_obj)
    else:
        st.write("No generated text to edit. Please go to the Generate page to create a tailored Twitter post.")


if __name__ == "__main__":
    main()

import streamlit as st
import backend_api
import os
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
    user_input = st.text_input("Paste the entire press release:")

    if st.button("Generate tailored twitter post!"):
        result = backend_api.twitter_text(user_input)
        st.session_state.generated_text = result
        print("Navigate to the Edit page now! ")

        # Navigate to the Edit page
        st.sidebar.radio("Select a page:", list(pages.keys()), index=1)

def edit_page():
    #TODO Url noch austauschen
    st.write("URL to the original press release: https://www.ifo.de/pressemitteilung/2023-04-28/konsum-und-industrie-senden-gegensaetzliche-impulse-fuer-deutsche")
    st.header("Edit your post:")

    if 'generated_text' in st.session_state:
        editable_text = st.text_area("Edit the post caption:", st.session_state.generated_text)

        # Load images from the 'images' folder
        image_folder = 'images'
        image_files = os.listdir(image_folder)

        # Display image previews with checkboxes
        st.write("Select image(s):")
        selected_images = []
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            image = Image.open(image_path)

            col1, col2 = st.columns([1, 4])
            selected = col1.checkbox("", key=image_file)
            col2.image(image, width=400)

            if selected:
                selected_images.append(image_file)
            elif image_file in selected_images:
                selected_images.remove(image_file)

        if st.button("Update preview"):
            st.write("Preview:")
            st.write(editable_text)

            # Display the first selected image
            if selected_images:
                first_image = Image.open(os.path.join(image_folder, selected_images[0]))
                st.image(first_image)
    else:
        st.write("No generated text to edit. Please go to the Generate page to create a tailored Twitter post.")


if __name__ == "__main__":
    main()

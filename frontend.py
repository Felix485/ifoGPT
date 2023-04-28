import streamlit as st
import backend_api

def main():
    # some Styling
    st.image("ifo_logo.png", width = 200)
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
    st.subheader("A press release generator")

    user_input = st.text_input("Enter keywords for the press release:")
    if st.button("Generate release!"):
        prompt = modify_prompt(user_input)
        result = backend_api.generate_response(prompt)
        result = "Press release - 29 April 2023 \n" + result
        st.header("Suggested press release:")
        st.write(f"{result}")

#Adds all the extra info to the prompts
def modify_prompt(user_input):
    user_input =  "Create a very short press release using the following keywords:" + user_input  #very short entfernen
    return user_input


if __name__ == "__main__":
    main()


import streamlit as st
import backend_api

def main():
    st.image("ifo_logo.png", width = 200)
    st.title("ifoGPT")
    st.markdown(
        "\n"
        "        <style>\n"
        "        body {\n"
        "        background-color: #f0f0f0;\n"
        "    }\n"
        "    </style>\n"
        "        ", unsafe_allow_html=True
    )
    st.subheader("A press release generator")
    user_input = st.text_input("Enter some text:")
    if st.button("Submit"):
        prompt = user_input
        result = backend_api.generate_response(prompt)
        st.header("Suggested press release:")
        st.write(f"{result}")





if __name__ == "__main__":
    main()


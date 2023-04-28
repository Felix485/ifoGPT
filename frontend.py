

import streamlit as st
def main():
    st.title("ifoGPT")
    st.image("ifo_logo.png", width = 200)
    st.markdown("""
    <style>
        body {
            background-color: #0D4080;
        }
    </style>
    """, unsafe_allow_html=True)
    st.subheader("A press release generator")
    user_input = st.text_input("Enter some text:")
    if st.button("Submit"):
        st.header("Suggested press release:")
        st.write(f"{user_input}")

    prompt = user_input
    result = myfunction(prompt)



if __name__ == "__main__":
    main()


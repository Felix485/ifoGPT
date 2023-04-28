

import streamlit as st
def main():
    st.title("ifoGPT")
    st.subheader("A press release generator")
    user_input = st.text_input("Enter some text:")
    if st.button("Submit"):
        st.header("Suggested press release:")
        st.write(f"{user_input}")
if __name__ == "__main__":
    main()


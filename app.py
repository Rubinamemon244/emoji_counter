import streamlit as st # type: ignore
import demoji # type: ignore

#DOWNLOAD DEMOJI DATA
demoji.download_codes()
st.set_page_config(page_title="Emoji Counter", page_icon=":smiley:", layout="centered")
st.title("Convert Your Emoji into Text")
user_input = st.text_input("Enter your emoji or text with emojis here:")
if st.button("Convert"):
        emoji_dict = demoji.findall(user_input)
        for emoji, desc in emoji_dict.items():
                user_input = user_input.replace(emoji, f"{{{desc}}}")
        st.write("Converted Text:", user_input)
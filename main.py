import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/my_photo.png",)

with col2:
    st.title("Beckham Vinoth")
    content = """
    Hi, I am Vinoth ! I am a programmer, This is my playground to play with
    my python projects. Have a nice day, Cheers :)
    """
    st.info(content)

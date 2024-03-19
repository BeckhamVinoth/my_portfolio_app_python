import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/my_photo.png",)

with col2:
    st.title("Beckham Vinoth")
    content = """
    Hi, I'm Vinoth !, A passionate Python developer with a flair for crafting innovative solutions 
    to real-world problems. With a strong background in computer science and years of hands-on experience,
    I thrive on turning ideas into tangible software products. My journey in programming began with a curiosity-driven 
    exploration of Python's versatility and elegance, and since then, I've embarked on numerous projects that 
    showcase the power and flexibility of this language.
    """
    st.info(content)

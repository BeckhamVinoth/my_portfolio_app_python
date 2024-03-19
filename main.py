import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/my_photo.png",)

with col2:
    st.title("Beckham Vinoth")
    author_content = """
    Hi, I'm Vinoth !, A passionate Python developer with a flair for crafting innovative solutions 
    to real-world problems. With a strong background in computer science and years of hands-on experience,
    I thrive on turning ideas into tangible software products. My journey in programming began with a curiosity-driven 
    exploration of Python's versatility and elegance, and since then, I've embarked on numerous projects that 
    showcase the power and flexibility of this language.
    """
    st.info(author_content)

projects_info_content = """
Below you can find some of the apps which I built in python. Feel free to contact me !
"""
st.write(projects_info_content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

csv_data = pandas.read_csv('data.csv', sep=";")

with col3:
    for i, row in csv_data[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source code]({row['url']})")

with col4:
    for i, row in csv_data[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

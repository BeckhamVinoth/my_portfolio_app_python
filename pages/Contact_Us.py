import streamlit as st

st.header('Contact Me')

with st.form(key='email_form'):
    email_add = st.text_input("Enter your email address")
    email_body = st.text_area("Drop in your message")
    st.form_submit_button("Submit")

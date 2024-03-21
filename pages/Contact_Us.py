import streamlit as st
import re
from send_email import send_email_from_users


st.header('Contact Me')


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False


with st.form(key='email_form'):
    email_add = st.text_input("Enter your email address")
    email_body = st.text_area("Drop in your message")
    message = f"""\
Subject: New email from {email_add}
        
From: {email_add}

{email_add} \n {email_body}
"""
    button = st.form_submit_button("Submit")
    if button:
        if is_valid_email(email_add):
            send_email_from_users(message)
            st.success("Email sent successfully!")
        else:
            st.error("Invalid email address. Please enter a valid email.")

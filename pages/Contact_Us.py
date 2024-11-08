import streamlit as st
from send_email import send_email

st.header ("Contact Me")

with st.form(key="email_forms"):
    user_name = st.text_input("Name")
    user_subject = st.text_input("Subject")
    user_email = st.text_input("Email")
    raw_message = st.text_area("Your Message")
    message = f"""\
User_name: New User_name
Subject: New email form {user_email}

from: {user_email}
{raw_message}

"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        st.info("Your email was sent successfully")


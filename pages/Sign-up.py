import streamlit as st

st.title("Split It")

form = st.form("Singup Form")
Name = form.text_input("Name", value="", key="name")
Email = form.text_input("Email", value="", key="email")
username = form.text_input("Username", value="", key="username")
password = form.text_input("Password", value="", key="password")
Confirm_password = form.text_input("Confirm Password", value="", key="Confirm_password")

# Add a submit button to the form
submit_button = form.form_submit_button("Sign up")

if submit_button:
    # Handle login submission (e.g., validate credentials, perform authentication)
    if username != "" and password != "" and nam:
        st.success("Sign up successful!")
    else:
        st.error("Invalid username or password. Try again!")
import streamlit as st

import pypyodbc as odbc

# Title and header
st.title("Split IT")
st.header("Log in")

# Create a form with two fields: username and password
form = st.form("Login Form")
username = form.text_input("Username", value="", key="username")
password = form.text_input("Password", value="", key="password")

# Add a submit button to the form
submit_button = form.form_submit_button("Log in")

if submit_button:
    # Handle login submission (e.g., validate credentials, perform authentication)
    if username == "admin" and password == "password":
        st.success("Login successful!")
    else:
        st.error("Invalid username or password. Try again!")

st.page_link("pages/Sign-up.py", label="Sign Up")
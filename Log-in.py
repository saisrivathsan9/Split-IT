import streamlit as st
from email_validator import validate_email, EmailNotValidError
import pyodbc
import db_connection as dbcon

st.title("Split IT")

login_tab, signup_tab = st.tabs(["Log in", "Sign up"])
#new log in (delte comment)

# --- LOGIN TAB ---
with login_tab:
    st.header("Log in")
    form = st.form("Login Form")
    username = form.text_input("Username", value="", key="username")
    password = form.text_input("Password", value="", key="password")

    # Add a submit button to the form
    submit_button = form.form_submit_button("Log in")

    if submit_button:
        # Handle login submission (e.g., validate credentials, perform authentication)
        try:
            conn = dbcon.create_connection()  # Use your DB connection from db_connection.py
            if conn:
                cursor = conn.cursor()
                # Query to check if the username and password exist in the database
                query = "SELECT * FROM Customer WHERE username = ? AND password = ?"
                cursor.execute(query, (username, password))
                result = cursor.fetchone()
                
                if result:
                    st.success("Login successful!")
                else:
                    st.error("Invalid username or password. Try again!")
                cursor.close()
                conn.close()
        except Exception as e:
            st.error(f"Error during login: {e}")

# --- SIGNUP TAB ---
with signup_tab:
    st.header("Sign up")

    def email_validation(email):
        try:
            validate_email(email) 
            return True
        except EmailNotValidError as e:
            st.error(f"Invalid email: {e}")
            return False

    def save_user(fName, sName, email, pass1, pass2):
        if pass1 != pass2:
            st.error("Passwords do not match.")
            return
        if len(pass1) < 8:
            st.error("Password must be more than 8 characters in length.")
            return
        if not email_validation(email):
            st.error("Invalid email format.")
            return
        
        # Insert user details into the database
        try:
            conn = dbcon.create_connection()  # Use your DB connection from db_connection.py
            if conn:
                cursor = conn.cursor()
                # SQL Insert query
                query = """
                INSERT INTO Customer (username, password, FirstName, LastName, email)
                VALUES (?, ?, ?, ?, ?)
                """
                cursor.execute(query, (email.split('@')[0], pass1, fName, sName, email))
                conn.commit()  # Commit the transaction
                st.success("Account Created Successfully!")
                cursor.close()
                conn.close()
        except Exception as e:
            st.error(f"Error saving data: {e}")

    # Signup form
    with st.form(key="sign_up_form"):
        fName = st.text_input("First Name", key="first_name")
        sName = st.text_input("Second Name", key="second_name")
        email = st.text_input("Email", key="email")
        st.info("**Password Requirements:** \n- At least 8 characters long")
        pass1 = st.text_input("Create Password", key="create_password", type="password")
        pass2 = st.text_input("Confirm Password", key="confirm_password", type="password")
        
        # On form submit, call the save_user function
        st.form_submit_button("Sign Up", on_click=lambda: save_user(fName, sName, email, pass1, pass2))

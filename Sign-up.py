import json
import streamlit as st
from email_validator import validate_email, EmailNotValidError
import pyodbc 
import db_connection as dbcon

st.title("Sign Up")

def email_validation(email):
    try:
        validate_email(email) 
        return True
    except EmailNotValidError as e:
        st.error(f"Invalid email: {e}")
        return False

def save_user(fName, sName, email, pass1, pass2):
    if st.session_state.create_password != st.session_state.confirm_password:
        st.error("Password do not match.")
        return
    if len(st.session_state.create_password ) < 8:
        st.error("Password must be more than 8 characters in length.")
        return
    email = st.session_state.email
    if not email_validation(email): st.error("Invalid email format.")
    else :
        st.success(f"Account Created")
        # Database insertion
    try:
        conn = dbcon.create_connection()
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


with st.form(key = "sign_up_form"):
    fName = st.text_input("First Name",key = "first_name")
    sName = st.text_input("Second Name",key = "second_name")
    email = st.text_input("Email",key = "email")
    st.info("**Password Requirements:** \n- At least 8 characters long")
    pass1 = st.text_input("Create Password",key = "create_password", type="password")
    pass2 = st.text_input("Confirm Password",key = "confirm_password",type="password")
    st.form_submit_button("Sign Up", on_click=save_user(fName, sName, email, pass1, pass2))




import streamlit as st
st.title("Sign Up")

def save_user():
    if st.session_state.create_password != st.session_state.confirm_password:
        st.error("Password do not match.")
        return
    if len(st.session_state.create_password ) < 8:
        st.error("Password must be more than 8 characters in length.")
        return
    else :
        st.success("Account Created")
    

with st.form(key = "sign_up_form"):
    st.text_input("First Name",key = "first_name")
    st.text_input("Second Name",key = "second_name")
    st.text_input("Email",key = "email")
    st.info("**Password Requirements:** \n- At least 8 characters long")
    st.text_input("Create Password",key = "create_password", type="password")
    st.text_input("Confirm Password",key = "confirm_password",type="password")
    st.form_submit_button("Sign Up", on_click=save_user)
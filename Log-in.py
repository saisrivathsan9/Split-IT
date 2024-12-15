import streamlit as st

st.title("Split IT")

login_tab , signup_tab = st.tabs(["Log in", "Sign up"])

login_tab.header("Log in")
signup_tab.header("Sign up")


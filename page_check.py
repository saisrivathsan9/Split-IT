import streamlit as st

create_page = st.Page("Log-in.py", title="Create entry", icon=":material/add_circle:")
delete_page = st.Page("Sign-up.py", title="Delete entry", icon=":material/delete:")

pg = st.navigation([create_page, delete_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()
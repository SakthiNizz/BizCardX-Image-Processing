import streamlit as st

def main_page():
    st.markdown("# Home Pageð")
    st.sidebar.markdown("# Home page ð")

def page2():
    st.markdown("# Database âï¸")
    st.sidebar.markdown("# Database âï¸")

page_names_to_funcs = {
    "Home Page": main_page,
    "Database": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
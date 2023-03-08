import streamlit as st

def main_page():
    st.markdown("# Home Page🎈")
    st.sidebar.markdown("# Home page 🎈")

def page2():
    st.markdown("# Database ❄️")
    st.sidebar.markdown("# Database ❄️")

page_names_to_funcs = {
    "Home Page": main_page,
    "Database": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
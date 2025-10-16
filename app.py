import streamlit as st

# Define and hide default nav if you want your own links
pages = [
    st.Page("pages/wwdc.py", title="WWDC Embedding View", default=True),
    st.Page("pages/vae.py", title="VAE Embedding View"),
    st.Page("pages/documentation.py", title="Documentation"),
]
nav = st.navigation(pages, position="top")

nav.run()

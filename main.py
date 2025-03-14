import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Day2Page",
    page_icon= ":shark:",
    layout = "wide"
)

st.markdown('# This is the main page...')
st.sidebar.write('Home')



im = Image.open('Dell_Logo.svg.png')
st.image(im, width=300)

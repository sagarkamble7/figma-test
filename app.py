import streamlit as st
from PIL import Image

# Define a dictionary of pages with their corresponding image filenames
pages = {
    "Homepage": "image1.png",
    "Produce Page": "image2.png",
    "Basket Page": "image3.png",

}

# Sidebar selector for navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to:", list(pages.keys()))

# Display the selected page and its image
st.title(selected_page)

# Load and display the image for the selected page
image_path = pages[selected_page]
image = Image.open(image_path)
st.image(image, use_container_width=True)

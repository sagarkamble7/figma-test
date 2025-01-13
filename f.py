import streamlit as st

# Function to read HTML file
def read_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Read the HTML files
Shopping_Cart = read_html(r'D:\Sagar_Kamble_DiabetesPrediction\shopping.html')
Product_page = read_html(r'D:\Sagar_Kamble_DiabetesPrediction\product.html')

# Display title
st.title("Figma")

# Function to display content with borders
def display_content(content, title):
    st.markdown(
        f"""
        <div style="border: 2px solid black; padding: 10px; margin: 10px 0;">
            <h3>{title}</h3>
            {content}
        </div>
        """, 
        unsafe_allow_html=True
    )

# Display content of File 2
display_content(Product_page, "Product_page")
# Display content of File 1
display_content(Shopping_Cart, "Shopping_Cart")


import streamlit as st
from database import add_product

st.title("🔐 Admin Panel")

pw = st.sidebar.text_input("Admin Password", type="password")
if pw == "admin123":
    with st.form("new_product"):
        name = st.text_input("Name")
        price = st.number_input("Price", min_value=0.0)
        desc = st.text_area("Description")
        img = st.text_input("Image URL")
        if st.form_submit_button("Add Product"):
            add_product(name, price, desc, img)
            st.success("Product Added!")
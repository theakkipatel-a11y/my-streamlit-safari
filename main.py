import streamlit as st
from database import init_db

st.set_page_config(page_title="Streamlit Amazon", layout="wide")

# Initialize DB on first run
init_db()

st.title("Welcome to the Streamlit Mega-Store")
st.write("Use the sidebar to start shopping or manage inventory.")

if "cart" not in st.session_state:
    st.session_state.cart = []

st.image("https://images.unsplash.com/photo-1472851294608-062f824d29cc?auto=format&fit=crop&q=80&w=1000", use_container_width=True)
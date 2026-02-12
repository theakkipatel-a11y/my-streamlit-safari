import streamlit as st
from database import get_all_products

st.title("🛍️ Product Catalog")

products = get_all_products()

if not products:
    st.info("No products found. Add some in the Admin panel!")
else:
    cols = st.columns(3)
    for i, p in enumerate(products):
        p_id, name, price, desc, img = p
        with cols[i % 3]:
            st.image(img if img else "https://via.placeholder.com/150")
            st.subheader(name)
            st.write(f"**${price:.2f}**")
            if st.button(f"Add to Cart", key=f"btn_{p_id}"):
                st.session_state.cart.append({"name": name, "price": price})
                st.toast(f"Added {name}!")
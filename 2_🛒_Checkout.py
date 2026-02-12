import streamlit as st
import stripe

# In production, use: stripe.api_key = st.secrets["STRIPE_SECRET_KEY"]
stripe.api_key = "sk_test_your_key_here" 

st.title("🛒 Your Cart")

if not st.session_state.cart:
    st.write("Your cart is empty.")
else:
    total = 0
    for item in st.session_state.cart:
        st.write(f"- {item['name']}: **${item['price']}**")
        total += item['price']
    
    st.divider()
    st.subheader(f"Total: ${total:.2f}")

    if st.button("Pay with Stripe"):
        # Create Stripe Session
        line_items = [{"price_data": {"currency": "usd", "product_data": {"name": i["name"]}, "unit_amount": int(i["price"]*100)}, "quantity": 1} for i in st.session_state.cart]
        
        session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url="http://localhost:8501", # Change to your live URL later
            cancel_url="http://localhost:8501",
        )
        st.link_button("Complete Payment", session.url)
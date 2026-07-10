import streamlit as st
from client import get_client
from utils import place_order

st.set_page_config(page_title="Trading Bot", layout="centered")

st.title("📈 Binance Futures Trading Bot")

# Input area
symbol = st.text_input("Symbol", "BTCUSDT")

side = st.selectbox("Order Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])

quantity = st.number_input("Quantity", min_value=0.0001, step=0.0001)

price = None
if order_type == "LIMIT":
    price = st.number_input("Price", min_value=1.0)

# Button
if st.button("🚀 Place Order"):

    client = get_client()

    st.subheader(" Order Summary")
    st.write({
        "Symbol": symbol,
        "Side": side,
        "Type": order_type,
        "Quantity": quantity,
        "Price": price
    })

    try:
        order = place_order(client, symbol, side, order_type, quantity, price)

        if order:
            st.success(" Order Placed Successfully!")
            st.json(order)

            # Fetch updated order info
            order_status = client.futures_get_order(
                symbol=symbol,
                orderId=order["orderId"]
            )

            st.subheader("📊 Order Details")
            st.write("Status:", order_status["status"])
            st.write("Executed Price:", order_status.get("avgPrice"))

        else:
            st.error("Order Failed")

    except Exception as e:
        st.error(f"Error: {e}")

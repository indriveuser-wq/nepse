import streamlit as st
from core.watchlist import load_watchlist, add_stock, remove_stock
from data.fetch import get_live_price

st.set_page_config(page_title="NEPSE Watchlist", layout="wide")

st.title("📈 NEPSE Watchlist")

# --- Add stock ---
symbol = st.text_input("Enter Stock Symbol (e.g., NABIL)")

if st.button("Add"):
    if symbol:
        add_stock(symbol.upper())
        st.rerun()

# --- Load watchlist ---
watchlist = load_watchlist()

st.subheader("Your Watchlist")

if not watchlist:
    st.info("No stocks added yet")

# --- Display watchlist ---
for stock in watchlist:
    col1, col2, col3 = st.columns([2, 2, 1])

    # Stock name
    with col1:
        st.write(f"### {stock}")

    # Price
    with col2:
        with st.spinner("Fetching..."):
            price = get_live_price(stock)

        # ✅ FIXED CONDITION
        if price is not None:
            st.success(f"Rs. {price}")
        else:
            st.error("No data")

    # Remove button
    with col3:
        if st.button("Remove", key=f"remove_{stock}"):
            remove_stock(stock)
            st.rerun()
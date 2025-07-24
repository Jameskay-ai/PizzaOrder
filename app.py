import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="🍕 Python Pizza Deliveries", layout="centered")

# --- Custom Background Image ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1601924582975-dfdb0f3f9297");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        color: white;
        font-family: 'Courier New', monospace;
    }
    .block-container {
        background-color: rgba(0, 0, 0, 0.75);
        padding: 2rem;
        border-radius: 10px;
    }
    h1, h2, h3, h4 {
        color: #ffcc00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- App Title ---
st.markdown("<h1 style='text-align: center;'>🍕 Welcome to Python Pizza Deliveries!</h1>", unsafe_allow_html=True)

# --- Order Section ---
with st.container():
    st.subheader("Customize Your Pizza Order")

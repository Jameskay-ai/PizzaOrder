# Standard Core components for Streamnlit / pandas / numpy
import streamlit as st
import pandas as pd
import numpy as np

# Custom CSS styling
st.markdown(
    """
    <style>
        /* Sidebar background and text color */
        [data-testid="stSidebar"] {
            background-color: #001f3f !important; /* Navy blue */
            color: white;
        }

        /* Sidebar elements (text, headings) */
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Main content area background and text color */
        .main, .block-container {
            background-color: #ffffff;
            color: #001f3f !important; /* Navy blue text */
        }

        /* Adjust all headers and markdown inside main to navy */
        .block-container h1, 
        .block-container h2,
        .block-container h3,
        .block-container h4,
        .block-container h5,
        .block-container h6,
        .block-container p,
        .block-container li {
            color: #001f3f !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar text display

with st.sidebar:
        # Button to redirect to Python Landing page
    st.caption("To view other projects click here")
    st.markdown(
        """
        <a href="https://jameskay-ai.github.io/" target="_blank">
            <button style="background-color:#004080; color:white; padding:10px; border:none; border-radius:5px;">
                Back to main
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
    st.divider()
    st.markdown("PROJECT DETAILS:")
    st.markdown("Category: Basic Level")
    st.markdown("""
   
    - ## **Key Concepts Covered:**
    - ##### if / elif / else statements (Nesting)
    - ##### Variable usage             
    - ##### Arithmetic operations and logic
    - ##### Variable assignment
    - ##### Output formatting with **round()** and f-strings
    """)   

    st.markdown("""
    ## **Detailed Explanation**
    Understanding the Python Code:
     """)         
    st.header("📘 Code Summary")
    st.markdown("""
### 🧾 **Python Pizza Deliveries Summary**

| Step | Description |
|------|-------------|
| 1 | **Greet the user** with a welcome message. |
| 2 | **Take inputs** Size (S/M/L) Pepperoni (Y/N) Extra Cheese (Y/N) |
| 3 | **Set initial bill** to 0. |
| 4 | **Add base cost**: (S = $15)(M = $20)(L = $25) 
""")
    st.markdown("""
| 5 | **Add for pepperoni**:(S = +$2)(M/L = +$3) 
| 6 | **Add $1** for extra cheese if selected |
| 7 | **Print final bill** to the user |

---
### 💡 Example:
**Size:** M  
**Pepperoni:** Y  
**Extra Cheese:** Y  

**Total Bill:** $24
""")             
    st.markdown("""      
    - ### **Real World Applications:**
    - ##### Order Processing - Fundamental POS systems calculation
    - ##### E-commerce checkout logic - Based on user selection options
    - ##### Survey or Form Input Validation
    - ##### Modular cost calculations""")  
                
# Main App display right side Interactive Portal
# --- Main Title ---
st.title("🍕 Python Pizza Order")
st.markdown("#### A fun logic-based ordering app built with Python and Streamlit")
st.markdown("##### 👨‍💻 By James Kay")
st.markdown("---")

# --- Pizza Order UI ---
st.subheader("🍽️ Build Your Pizza")
st.write("Choose your size and toppings below:")

size = st.radio("Select Pizza Size:", ["S", "M", "L"])
pepperoni = st.checkbox("Add Pepperoni")
extra_cheese = st.checkbox("Add Extra Cheese")

# Calculation
# --- Billing Logic ---
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni:
    bill += 2 if size == "S" else 3

if extra_cheese:
    bill += 1

# --- Result ---
st.markdown("---")
st.subheader(f"💰 Total: **${bill}**")
st.success("Thank you for your order! 🍕")

with st.expander("Show Python Code"):
    st.code("""
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
    """, language="python")

import streamlit as st

# Set the dark theme and page title
st.set_page_config(page_title="Price Difference Calculator", layout="centered")
st.markdown(
    """
    <style>
        body {
            background-color: #2B2B2B;
            color: #FFFFFF;
        }
        input {
            color: #000000;
        }
        .stTextInput > label {
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Price Difference Calculator")
st.write("Enter prices for comparison, and the tool will calculate the percentage difference for up to 10 rows.")

# Helper function to parse numbers with "," or "."
def parse_number(number_str):
    return float(number_str.replace(",", "."))

# Initialize columns for input and output
col1, col2, col3 = st.columns([3, 3, 4])
col1.header("Price A")
col2.header("Price B")
col3.header("Difference (%)")

# Input fields for 10 rows
for i in range(10):
    with col1:
        price_a = st.text_input(f"Price A - Row {i + 1}", value="")
    with col2:
        price_b = st.text_input(f"Price B - Row {i + 1}", value="")
    
    # Calculate difference if both inputs are provided
    if price_a and price_b:
        try:
            # Parse numbers and calculate percentage difference
            price_a = parse_number(price_a)
            price_b = parse_number(price_b)
            difference = ((1 / price_a) - (1 / price_b)) * 100
            formatted_diff = f"{difference:.2f}%"
        except ValueError:
            formatted_diff = "Invalid input"
    else:
        formatted_diff = "N/A"
    
    with col3:
        st.write(formatted_diff)

#  "Initial commit"

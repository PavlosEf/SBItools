import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Off prices Calculator", layout="centered")

st.markdown(
    """
    <style>
        /* Change background color and make all text white */
        .stApp {
            background-color: #1E1E1E;  /* Dark grey */
            color: white;  /* White text */
        }
        div, label, span, p {
            color: white !important;  /* Make text inside all elements white */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page title and description
st.title("Off prices Calculator")
st.markdown("Enter prices below to calculate the percentage difference for up to 10 rows.")

# Helper function to parse numbers (handles commas and periods)
def parse_number(number_str):
    try:
        return float(number_str.replace(",", "."))
    except ValueError:
        return None

# Create input fields and calculate results
results = []
for i in range(10):
    col1, col2, col3 = st.columns(3)

    # Input for Price A
    with col1:
        price_a = st.text_input(f"Price A)", key=f"price_a_{i}")
    
    # Input for Price B
    with col2:
        price_b = st.text_input(f"Price B)", key=f"price_b_{i}")
    
    # Output for percentage difference
    with col3:
        if price_a and price_b:
            parsed_a = parse_number(price_a)
            parsed_b = parse_number(price_b)
            if parsed_a and parsed_b and parsed_a > 0 and parsed_b > 0:
                difference = ((1 / parsed_a) - (1 / parsed_b)) * 100
                col3.write(f"{difference:.2f}%")
            else:
                col3.write("Invalid input")
        else:
            col3.write("Enter values")


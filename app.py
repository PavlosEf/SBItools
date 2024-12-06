import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Price Difference Calculator", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #2B2B2B;  /* Dark gray background */
            color: #FFFFFF;  /* White text */
        }
        .stTextInput > label {
            font-size: 16px;
            color: #FFFFFF;  /* White input labels */
        }
        .stTextInput {
            margin-bottom: 20px;  /* Add spacing between input sections */
        }
        input {
            background-color: #EAEAEA; /* Light gray input fields */
            color: #000000; /* Black text inside input fields */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page title and description
st.title("Price Difference Calculator")
st.markdown("Enter prices below to calculate the percentage difference for up to 10 rows.")

# Helper function to parse numbers (handles commas and periods)
def parse_number(number_str):
    try:
        return float(number_str.replace(",", "."))
    except ValueError:
        return None

# Create input fields and calculate results
st.sidebar.header("Input Prices")  # Align to the top-left sidebar
results = []
for i in range(10):
    # Input for Price A and Price B in the sidebar
    price_a = st.sidebar.text_input(f"Price A {i + 1}", key=f"price_a_{i}")
    price_b = st.sidebar.text_input(f"Price B {i + 1}", key=f"price_b_{i}")
    
    # Calculate and display the percentage difference
    if price_a and price_b:
        parsed_a = parse_number(price_a)
        parsed_b = parse_number(price_b)
        if parsed_a and parsed_b and parsed_a > 0 and parsed_b > 0:
            difference = ((1 / parsed_a) - (1 / parsed_b)) * 100
            results.append(f"Row {i + 1}: {difference:.2f}%")
        else:
            results.append(f"Row {i + 1}: Invalid input")
    else:
        results.append(f"Row {i + 1}: Enter values")

# Display results on the main page
st.header("Results")
for result in results:
    st.write(result)




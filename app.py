import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Price Difference Calculator", layout="centered")

# Add custom CSS for dark background and styling
st.markdown(
    """
    <style>
        /* Change background color of the main content */
        .stApp {
            background-color: #1E1E1E;  /* Dark grey background */
        }
        /* Make all text white */
        * {
            color: #FFFFFF;  /* White text */
        }
        .stTextInput > label {
            color: #FFFFFF; /* Ensure input labels are white */
        }
        /* Style for input boxes */
        input {
            width: 33%; /* Reduce input box width to 1/3 size */
            background-color: #EAEAEA; /* Light grey input fields */
            color: #000000; /* Black text inside input fields */
        }
        .result-box {
            border: 2px solid #FFFFFF;  /* White border */
            padding: 5px;
            margin: 5px;
            text-align: center;
            border-radius: 5px;
            min-width: 70px;
        }
        .ok {
            color: #00FF00; /* Green for OK */
        }
        .off2 {
            color: #800080; /* Purple for OFF 2 */
        }
        .off1 {
            color: #FF0000; /* Red for OFF 1 */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page title and description
st.title("Off Prices Calculator")
st.markdown("Enter prices below to calculate the percentage difference for up to 10 rows.")

# Helper function to parse numbers (handles commas and periods)
def parse_number(number_str):
    try:
        return float(number_str.replace(",", "."))
    except ValueError:
        return None

# Calculate label outcome based on the difference
def get_label(difference):
    if difference > 2:
        return '<div class="outcome-box ok">OK</div>'
    elif -2 <= difference <= 3:
        return '<div class="outcome-box off2">OFF 2</div>'
    elif difference > 3:
        return '<div class="outcome-box off1">OFF 1</div>'

# Create input fields and calculate results
for i in range(10):
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])  # Adjust column sizes
    
    with col1:
        price_a = st.text_input(f"Kaizen Odds : ", key=f"price_a_{i}")
    with col2:
        price_b = st.text_input(f"Competition Odds :", key=f"price_b_{i}")
    
    if price_a and price_b:
        parsed_a = parse_number(price_a)
        parsed_b = parse_number(price_b)
        if parsed_a and parsed_b and parsed_a > 0 and parsed_b > 0:
            # Calculate percentage difference
            difference = ((1 / parsed_a) - (1 / parsed_b)) * 100
            
          with col3:
    # Display percentage difference in a styled box
    st.markdown(
        f'<div class="result-box">{difference:.2f}%</div>',
        unsafe_allow_html=True,
    )
with col4:
    # Display label in a styled box
    st.markdown(get_label(difference), unsafe_allow_html=True)
 unsafe_allow_html=True)  # Display label



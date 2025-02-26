import streamlit as st

# Function to convert units
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        # Length
        'meters': 1, 'kilometers': 0.001, 'miles': 0.000621371,
        # Mass
        'grams': 1, 'kilograms': 0.001, 'pounds': 0.00220462,
        # Volume
        'liters': 1, 'gallons': 0.264172,
        # Time
        'seconds': 1, 'minutes': 1/60
    }
    
    # Temperature conversion separately handled
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32, "Multiply by 9/5 and add 32"
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9, "Subtract 32, then multiply by 5/9"
    elif from_unit in conversion_factors and to_unit in conversion_factors:
        factor = conversion_factors[to_unit] / conversion_factors[from_unit]
        return value * factor, f"Multiply by {factor}"
    else:
        return None, None

# Streamlit UI
st.title("🔢Google Unit Converter")
st.write("Convert between different units of measurement easily.")

# User input
value = st.number_input("Enter the value to convert:", min_value=0.0, format="%.4f")
from_unit = st.selectbox("Select the unit to convert from:", 
                          ['meters', 'kilometers', 'miles', 
                           'grams', 'kilograms', 'pounds', 
                           'liters', 'gallons',
                           'seconds', 'minutes',
                           'celsius', 'fahrenheit'])
to_unit = st.selectbox("Select the unit to convert to:", 
                        ['meters', 'kilometers', 'miles', 
                         'grams', 'kilograms', 'pounds', 
                         'liters', 'gallons',
                         'seconds', 'minutes',
                         'celsius', 'fahrenheit'])

# Convert button
if st.button("🔄 Convert"):
    result, formula = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}.")
        if formula:
            st.info(f"**Formula:** {formula}")
    else:
        st.error("⚠ Invalid conversion units selected.")

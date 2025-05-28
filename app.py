# import streamlit as st

# def convert_units(value: float, unit_from: str, unit_to: str):
#     # print("value>>>",value)
#     # print("unit_from>>>",unit_from)
#     # print("unit_to>>>",unit_to)

#     # 1 killometer = 1000 meters
#     # 1 meter = 0.001 kilimeter
#     # 1 kilogram = 1000 grams
#     # 1 gram = 0.001 kilograms
    
#     if unit_from == "kilometers" and unit_to == "meters" :
#         return value * 1000
#     elif unit_from == "meters" and unit_to == "kilometers" :
#         return value * 0.001
#     elif unit_from == "kilograms" and unit_to == "grams" :
#         return value * 1000
#     elif unit_from == "grams" and unit_to == "kilograms" :
#         return value * 0.001
#     else:
#         return "conversion is not supported"


# # result1 = convert_units(3, "kilometers", "meters")
# # print("The value in meter is:", result1)
# # result2 = convert_units(5, "grams", "kilograms")
# # print("The value in kilograms is:", result2)



# def main():
#     st.title("Unit Converter")
#     st.write("Welcome to unit converter!")
#     value = st.number_input("Enter the value you want to convert:", min_value=0.0)
#     unit_from = st.text_input("Enter the value you want to convert from: (e.g. meters, kilometers, grams, kilograms)")
#     unit_to = st.text_input("Enter the value you want from conversion: (e.g. meters, kilometers, grams, kilograms)")
    
#     if st.button("Covert"):
#         result = convert_units(value, unit_from, unit_to)
#         st.write("Converted value is:", result)

      

# #     print("Unit Converter")
# #     print("Welcome to unit converter!")
# #     value = float (input("Enter the value you want to convert:"))
# #     unit_from = input("Enter the value you want from (e.g. meters, kilometers, grams, kilograms)")
# #     unit_to = input("Enter the value you want from conversion (e.g. meters, kilometers, grams, kilograms)")
# #     print("value", value)
# #     print("unit_from", unit_from)
# #     print("unit_to", unit_to)
# #     result = convert_units(value, unit_from, unit_to)
# #     print("Converted value is:", result)

# main()

## 🧠 **Python Streamlit App Code – `app.py`**

import streamlit as st

# Title and description
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🌐 Unit Converter")
st.markdown("Convert between different units instantly!")

# Unit categories and options
unit_categories = {
    "Length": {
        "units": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
        "conversion": {
            "Meters": 1,
            "Kilometers": 0.001,
            "Miles": 0.000621371,
            "Feet": 3.28084,
            "Inches": 39.3701,
        }
    },
    "Weight": {
        "units": ["Kilograms", "Grams", "Pounds", "Ounces"],
        "conversion": {
            "Kilograms": 1,
            "Grams": 1000,
            "Pounds": 2.20462,
            "Ounces": 35.274,
        }
    },
    "Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"]
    }
}

# Select category
category = st.selectbox("Select Unit Category", list(unit_categories.keys()))

# Input value
value = st.number_input("Enter value to convert", format="%.4f")

# Unit options
from_unit = st.selectbox("From Unit", unit_categories[category]["units"])
to_unit = st.selectbox("To Unit", unit_categories[category]["units"])

def convert_temperature(val, from_u, to_u):
    if from_u == to_u:
        return val
    if from_u == "Celsius":
        return val * 9/5 + 32 if to_u == "Fahrenheit" else val + 273.15
    elif from_u == "Fahrenheit":
        return (val - 32) * 5/9 if to_u == "Celsius" else (val - 32) * 5/9 + 273.15
    elif from_u == "Kelvin":
        return val - 273.15 if to_u == "Celsius" else (val - 273.15) * 9/5 + 32

# Conversion logic
if category != "Temperature":
    base_val = value / unit_categories[category]["conversion"][from_unit]
    result = base_val * unit_categories[category]["conversion"][to_unit]
else:
    result = convert_temperature(value, from_unit, to_unit)

# Show result
st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

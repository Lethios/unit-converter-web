import streamlit as st
from pint import UnitRegistry

length_tab, weight_tab, temperature_tab = st.tabs(["Length", "Weight", "Temperature"])


def unit_conversion(value, source_unit, target_unit):
    ureg = UnitRegistry()

    from_unit = source_unit.lower()
    to_unit = target_unit.lower()

    if from_unit == "celsius":
        from_unit = "degC"
    elif from_unit == "fahrenheit":
        from_unit = "degF"

    if to_unit == "celsius":
        to_unit = "degC"
    elif to_unit == "fahrenheit":
        to_unit = "degF"

    original_value = ureg.Quantity(value, ureg[from_unit])
    final_value = original_value.to(ureg[to_unit])

    return final_value

with length_tab:
    with st.form(key="length_conversion_form"):
        value = st.number_input("Enter length to convert")
        from_unit = st.selectbox("Convert from", ["Millimeter", "Centimeter", "Meter", "Kilometer", "Inch", "Foot", "Yard", "Miles"])
        to_unit = st.selectbox("Convert to", ["Millimeter", "Centimeter", "Meter", "Kilometer", "Inch", "Foot", "Yard", "Miles"])

        submit = st.form_submit_button("Convert")

        if submit:
            converted_value = unit_conversion(value, from_unit, to_unit)
            st.success(f"{value:.4g} {from_unit.lower()} = {converted_value:.4g}")

with weight_tab:
    with st.form(key="weight_conversion_form"):
        value = st.number_input("Enter weight to convert")
        from_unit = st.selectbox("Convert from", ["Milligram", "Gram", "Kilogram", "Ounce", "Pound"])
        to_unit = st.selectbox("Convert to", ["Milligram", "Gram", "Kilogram", "Ounce", "Pound"])

        submit = st.form_submit_button("Convert")
        
        if submit:
            converted_value = unit_conversion(value, from_unit, to_unit)
            st.success(f"{value:.4g} {from_unit.lower()} = {converted_value:.4g}")

with temperature_tab:
    with st.form(key="temperature_conversion_form"):
        value = st.number_input("Enter temperature to convert")
        from_unit = st.selectbox("Convert from", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("Convert to", ["Celsius", "Fahrenheit", "Kelvin"])

        submit = st.form_submit_button("Convert")

        if submit:
            converted_value = unit_conversion(value, from_unit, to_unit)
            st.success(f"{value:.4g} {from_unit.lower()} = {converted_value:.4g}")

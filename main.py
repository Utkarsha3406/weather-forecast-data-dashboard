import streamlit as st

st.title("weather forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view",("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


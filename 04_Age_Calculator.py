import streamlit as st
from datetime import date

today = date.today()
# print("Today's date:", today)

st.write(f"Current Date: {today}")


dob1 = st.date_input("Enter your date of Birth")

st.write(f"You are {dob1.year - today.year} year old")


import streamlit as st
from datetime import datetime


min_date = datetime(1900, 1, 1)
max_date = datetime.now()

st.title("User Information Form")

with st.form(key="User_info_form", clear_on_submit=True):
    name = st.text_input("Enter your name")

    birth_date = st.date_input("Enter your birth date", min_value=min_date, max_value=max_date)

    if birth_date:
        age = max_date.year - birth_date.year 
        if birth_date.month > max_date.month or (birth_date.month == max_date.month and birth_date.month < max_date.month):
            age -= 1

        # Only after the submit you will display the age (calculated) because in form it can not re runs so we have an state management
        st.write(f"Your calculated age is {age} years")

    submit_button = st.form_submit_button(label="Submit Form")
import streamlit as st
import pandas as pd
import time
from datetime import datetime

# from streamlit_extras.let_it_rain import rain
# rain(emoji="🎈", font_size=60, falling_speed=5)

st.title("User Information Form")

form_value = {
    "name": None,
    "age": None,
    "height": None,
    "gender": None,
    "dob": None,
    "time": None,
    "choice": None,
    "feedback": None,
    "file": None
}

# We also able to give max and min dates
min_date = datetime(1990, 1, 1)
max_date = datetime.now()


with st.form(key="Smaple_form", clear_on_submit=True):
    
    # Text Input
    st.subheader("Text Input")
    form_value["name"] = st.text_input("Enter your Name")
    form_value["age"] = st.number_input("Enter your age: ", min_value=1, max_value=100)
    form_value["height"] = st.number_input("Enter height")
    form_value["feedback"] = st.text_area("Provide your feedback")
    form_value["file"] = st.file_uploader("Upload file", type=["pdf"])

    # It can not re run the application (If you click submit then it reruns the app)
    # print(name, age, feedback)

    # Date and Time Inputs
    st.subheader("Data and Time Inputs")
    form_value["dob"] = st.date_input("Select your date of birth", max_value=max_date, min_value=min_date)
    form_value["time"] = st.time_input("Choose a preferred time")


    # Selectors
    st.subheader("Selectors")
    form_value["choice"] = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
    form_value["gender"] = st.selectbox("Select your gender", ["Male", "Female", "Other"])
    slider_value = st.select_slider("Select a range", options=[1, 2, 3, 4, 5])


    # Toggles and Checkboxes
    st.subheader("Toggle & Checkboxes")
    notification = st.checkbox("Receive notification?")
    toggle_value = st.checkbox("Enable dark mode?", value=False)

    # Submit Buttons for the form
    submit_button = st.form_submit_button(label="Submit")
    print("after submit")
    if submit_button:
        print("In if")
        if not all(form_value.values()):
            st.warning("Please fill in all of the fields")

            # Shows a red error box.
            st.error("Something went wrong.")
        else:
            # Shows floating balloons animation.
            st.balloons()

            # Shows falling snowflakes.
            st.snow()

            # Shows a blue informational box.
            st.info("This is some helpful information.")

            # Displays a small popup message like a toast notification.
            st.toast("Data saved successfully!")

            # Shows a green success box.
            st.success("Operation completed successfully!")

            # Temporarily shows a loading spinner during a task.
            with st.spinner("Loading..."):
                time.sleep(3)
            st.success("Done!")

            for (key, value) in form_value.items():
                st.write(f"{key} = {value}")


# Outside of the form
st.subheader("Buttons")

if st.button("Click me"):
    st.write(f"Hello, {form_value["name"]}")

if submit_button:
    st.write(form_value)

# 
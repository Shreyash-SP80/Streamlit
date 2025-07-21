import streamlit as st
import time

# Caching in Streamlit is a mechanism that helps speed up your app by storing the results of expensive computations (like data processing, API calls, or ML model loading) so that they don’t run again unless necessary.


# = Why Use Caching?
# When you run a function in Streamlit (like reading a large file or calling an API), it takes time. Streamlit remembers the result using caching, and next time you run the app, it shows the stored result instead of re-running the function, saving time.


# = How to Use Caching in Streamlit
#   Using @st.cache_data (Streamlit v1.18+)

# Example:
# @st.cache_data
# def load_data():
#     df = pd.read_csv("big_data.csv")
#     return df

# df = load_data()
# st.write(df)

#  This tells Streamlit:
# “If load_data() has already been run with the same inputs, don’t run it again — just use the cached result.”


# = Streamlit reuses the cached value only if:
#   The function code hasn’t changed.
#   The input arguments are the same.
#   The Python environment is the same.

@st.cache_data
def return_data(name):
    time.sleep(4)
    return f"Hello this is {name}"

if st.button("Click to fetch data"):
    st.subheader("1st Fetching data..")
    st.write(return_data("Shreyash"))

    st.subheader("2nd Fetching data..")
    st.write(return_data("Shreyash"))  # This uses the cached data because input parameters are the same

    st.subheader("3rd Fetching data..")
    st.write(return_data("Rohit"))   # This actuals calls an function because input parameter is changed
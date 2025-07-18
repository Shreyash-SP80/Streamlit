import streamlit as st
import pandas as pd

# Title
st.title("Streamlit Elements")

# DataFrame Selection
st.subheader("DataFrame")

df = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104],
    'Name': ['John', 'Emma', 'Noah', 'Olivia'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing'],
    'Salary': [50000, 60000, 55000, 52000]
})

# Render DataFrame 
st.dataframe(df)

# Data Editor Section (Editable Dataframe)
st.subheader("Data Editor")
editable_df =  st.data_editor(df)
print(editable_df)  # If you update then it can give updated 


# Metrices Section
st.subheader("Metrices")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Salary", value=round(df['Salary'].mean(), 1))


# Static Table Section
st.subheader("Static Table")
st.table(df)

# JSON and Dict Section
st.subheader("JSON and Dict")
smaple_dict = {
    "name": "Shreyash",
    "age": 20,
    "Skills": ["Java", "Python", "C++", "C"]
}
st.json(smaple_dict)


# Also show it as dictionary
st.write("Dictionary view", smaple_dict)





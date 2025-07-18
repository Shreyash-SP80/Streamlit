import streamlit as st

st.title("Simple web App")
st.header("This is an Header")
st.subheader("This is subHeader")
st.markdown("This is **Markdown**")
st.markdown("This is _Markdown_")
st.caption("This is caption")

# This Adds code 
code_example = """
def greet(name):
    print("Hello", name)
"""

st.code(code_example, language="python")

# This adds divided like line
st.divider()
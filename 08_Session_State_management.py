import streamlit as st

# counter = 0

# With out session state issue

# st.write(f"Counter value: {counter}")

# if st.button("Increment counter"):
#     counter += 1
#     print("In")
#     st.write(f"Counter incremented to {counter}")
# else:
#     st.write(f"Counter stays at {counter}")


# Solution with session state

if "counter" not in st.session_state:
    st.session_state.counter = 0


if st.button("Increment counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")
if st.button("Reset"):
    st.session_state.counter = 0
    st.write("Counter reseted to 0")
else:
    st.write("Counter is not reseted")

st.write(f"Counter value: {st.session_state.counter }")
st.write(st.session_state)


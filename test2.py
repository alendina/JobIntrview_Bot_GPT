import streamlit as st
import openai

print("\nopenai version is", openai.__version__, end="\n\n") 

if "show_text" not in st.session_state:
    st.session_state.show_text = False

if st.button("Show/Hide Text"):
    st.session_state.show_text = not st.session_state.show_text

if st.session_state.show_text:
    st.write("Hello, Streamlit!")

# Initialize counter in session state
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Click Me"):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")  # Persists value

def increase():
    st.session_state.count += 1

# Initialize counter
if "count" not in st.session_state:
    st.session_state.count = 0

st.write("")
st.button("Increase", on_click=increase)  # Calls increase() on click
st.write(f"Count: {st.session_state.count}")
import streamlit as st

st.title("Nested Buttons Example")

st.session_state.setdefault('show_second_button', False)
if 'second_button_clicked' not in st.session_state:
    st.session_state.setdefault('second_button_clicked', False)
# First button
if st.button("First Button"):
    st.session_state.show_second_button = True
    # When the first button is clicked, show the second button
    st.session_state.show_second_button = True
# Check the state of the first button
if st.session_state.show_second_button:
    st.write("Revealed")
    # Second button: This button appears after the first button is clicked
    # and sets 'second_button_clicked' to True when clicked.
    # Second button
    if st.button("Second Button"):
        st.session_state.second_button_clicked = True

# Check the state of the second button
if st.session_state.second_button_clicked:
    st.write("Second Button Clicked!")

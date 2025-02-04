import streamlit as st
import pandas as pd
import numpy as np

if "counter" not in st.session_state:
    st.session_state.page = 2
st.write(f"page {st.session_state.page}")

st.title('_MyMy_ :blue[first app] :speech_balloon:')

if st.session_state.page == 1:
    st.write("Це мій перший застосунок на Streamlit!")
    st.header(":green[Завантаження даних]")
    st.subheader(":violet[Maths Formulas]")
    st.write(r":violet[$\int_{-1}^{1} e^x \,dx$]")

    name = ''
    name = st.text_input("Введіть ваше ім'я:")
    if name:
        st.write(f"Привіт, {name}!")    

    if st.button(f"Натисніть мене {name}"):
        st.session_state.page += 1
        st.write(f"page {st.session_state.page}")
        st.write(f":violet[Hi once more time, {name}!]")
    
    
    st.chat_message("Привіт!")
    if st.chat_input("Введіть ваше повідомлення тут..."):
        st.session_state.page += 1
        st.write(f"page {st.session_state.page}")
        st.rerun()
elif st.session_state.page > 1:
    st.chat_message("Привіт! Як я можу вам допомогти?")
    if st.chat_input("KuKu"):
        st.write("Ваше повідомлення було успішно надіслано!")

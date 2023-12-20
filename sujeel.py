import streamlit as st


name = st.text_input("enter your name : ")
fname = st.text_input("enter your father name : ")
adr = st.text_area("enter your text : ")

button = st.button("done")


import streamlit as st
st.title("My first streamlit app")
name=st.text_input("Enter your name")
if st.button("Say Hello"):
    if name:
        st.success(f"Hello {name}, Welcome to my page")
    else:
        st.warning("please enter your name") 



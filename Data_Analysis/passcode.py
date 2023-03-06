#in this file I saved the password as a string and this will not upload to github
import streamlit as st # Importing streamlit, a python library for creating web apps.
def pcode(): # Creating a function for the password.
    password = st.text_input("Enter a password", type="password") # Creating a password input.
    # if password is blank text will be displayed
    if password == "":
        st.text("Parolni kiriting")

    elif password == "12345": # If the password is correct, then the sidebar will be displayed.
        return True
    
    else:
        return st.text("Parol notog'ri") # If the password is incorrect, then the text will be displayed.

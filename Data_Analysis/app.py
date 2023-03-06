import streamlit as st # Importing streamlit, a python library for creating web apps. 
import pandas as pd # Importing pandas, a python library for data analysis.
import matplotlib.pyplot as plt # Importing matplotlib, a python library for data visualization.
import seaborn as sns # Importing seaborn, a python library for data visualization.
from password import pcode # Importing the password.py file.
from graph_page import show_data, graph_plot, graph_plot2 # Importing the graph_page.py file.
from PIL import Image # Importing the PIL library for image processing.
import os # Importing the os library for operating system functions.

header = st.container() # Creating a container for the header.
dataset = st.container() # Creating a container for the dataset.
features = st.container() # Creating a container for the features.

with header: # Creating a header.
    img_path = os.path.join(os.getcwd(), 'assets', 'picture.png') # Creating a variable for the logo image.
    st.sidebar.image(img_path, use_column_width=True) # Adding the logo image to the sidebar.
    st.sidebar.markdown("<h1 style='text-align: center; color: black;'>DATA TEAM</h1>", unsafe_allow_html=True) # Creating a header.
    menu = ["Bosh Sahifa", "Ma'lumotlar Tahlili", "Jamoa Haqida", "Aloqa"]
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == "Bosh Sahifa":
        st.markdown("<h1 style='text-align: center; color: black;'>BOSH SAHIFA</h1>", unsafe_allow_html=True) # Creating a header.
        st.text("Test rejimida ishlamoqda")
    
    elif choice == "Ma'lumotlar Tahlili":
        st.markdown("<h1 style='text-align: center; color: black;'>MA'LUMOTAR TAHLILI</h1>", unsafe_allow_html=True) # Creating a header.
        if pcode() is True:
            show_data()
            graph_plot()
            graph_plot2()

            
    elif choice == "Jamoa Haqida":
        st.markdown("<h1 style='text-align: center; color: black;'>JAMOA HAQIDA</h1>", unsafe_allow_html=True)
        st.text("Test rejimida ishlamoqda")
    
    elif choice == "Aloqa":
        st.markdown("<h1 style='text-align: center; color: black;'>ALOQA</h1>", unsafe_allow_html=True)
        st.text("Test rejimida ishlamoqda")

        



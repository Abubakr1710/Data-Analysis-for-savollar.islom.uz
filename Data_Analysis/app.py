import streamlit as st # Importing streamlit, a python library for creating web apps. 
import pandas as pd # Importing pandas, a python library for data analysis.
import matplotlib.pyplot as plt # Importing matplotlib, a python library for data visualization.
import seaborn as sns # Importing seaborn, a python library for data visualization.
from password import pcode # Importing the password.py file.
header = st.container() # Creating a container for the header.
dataset = st.container() # Creating a container for the dataset.
features = st.container() # Creating a container for the features.

with header: # Creating a header.
    st.markdown("<h1 style='text-align: center; color: black;'>DATA ANALYSIS</h1>", unsafe_allow_html=True)
    pcode() # Calling the password function from the password.py file.


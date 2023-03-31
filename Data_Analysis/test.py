import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/all_data.csv')
left_column, middle_column, right_column = st.columns(3)

st.sidebar.markdown("<h1 style='text-align: center; color: black;'>DATA TEAM</h1>", unsafe_allow_html=True) # Creating a header.
menu = ["Bosh Sahifa", "Ma'lumotlar Tahlili", "Jamoa Haqida", "Aloqa"]
choice = st.sidebar.selectbox('Menu', menu)
if choice == "Bosh Sahifa":
    st.markdown("<h1 style='text-align: center; color: black;'>BOSH SAHIFA</h1>", unsafe_allow_html=True) # Creating a header.
    
elif choice == "Ma'lumotlar Tahlili":
    st.markdown("<h1 style='text-align: center; color: black;'>MA'LUMOTAR TAHLILI</h1>", unsafe_allow_html=True)
    with left_column:
        st.subheader('Umumiy')
        #creating multiselect with years
        years = st.multiselect('Select', df['date'])
        #displaying multiselect
        st.write(years)
    st.dataframe(df, use_container_width=True)
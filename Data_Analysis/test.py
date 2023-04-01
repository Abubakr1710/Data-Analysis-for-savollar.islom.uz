import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('new_data.csv')
udf = df.copy()
ydf = df.copy()
bdf = df.copy()


st.sidebar.markdown("<h1 style='text-align: center; color: black;'>DATA TEAM</h1>", unsafe_allow_html=True) # Creating a header.
menu = ["Bosh Sahifa", "Umumiy Tahlil", "Yillik Tahlil", "Bo'limlar Tahlili" , "Smart Qidiruv"]
choice = st.sidebar.selectbox('Menu', menu)


if choice == "Bosh Sahifa":
    st.markdown("<h1 style='text-align: center; color: black;'>BOSH SAHIFA</h1>", unsafe_allow_html=True) # Creating a header.
    #st.dataframe(df, use_container_width=True)



elif choice == "Umumiy Tahlil":
    st.markdown("<h1 style='text-align: center; color: black;'>Umumiy Tahlil</h1>", unsafe_allow_html=True)
    if st.button("Ma'lumotlar", use_container_width=True):
        st.dataframe(udf, use_container_width=True)


    st.markdown("<br><h3 style='text-align: center; color: black;'>Bo'limlar bo'yicha savollar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(udf['section'].value_counts(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center; color: black;'>Bo'limlar bo'yicha umumiy ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(udf.groupby('section')['views'].sum(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center; color: black;'>Yillik savollar soni</h3><br>", unsafe_allow_html=True) 
    st.bar_chart(udf['year'].value_counts(), use_container_width=True, height=500, width=500)
    st.line_chart(udf['year'].value_counts(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center; color: black;'>Yillik ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(udf.groupby('year')['views'].sum(), use_container_width=True, height=500, width=500)
    st.line_chart(udf.groupby('year')['views'].sum(), use_container_width=True, height=500, width=500)



elif choice == "Yillik Tahlil":
    st.markdown("<h1 style='text-align: center; color: black;'>Yillik Tahlil</h1>", unsafe_allow_html=True)

    menu2 = ydf['year'].unique()
    side_year = st.sidebar.selectbox('Tanlov', menu2)
    ydf = ydf[ydf['year'] == side_year]
    display_data = ydf.copy()
    display_data = display_data[['section', 'views', 'date']]

    if st.button("Ma'lumotlar", use_container_width=True):
        st.dataframe(display_data, use_container_width=True)

    st.markdown("<br><h3 style='text-align: center; color: black;'>Bo'limlar bo'yicha savollar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(ydf['section'].value_counts(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center; color: black;'>Bo'limlar bo'yicha umumiy ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(ydf.groupby('section')['views'].sum(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center; color: black;'>Bo'limlar bo'yicha oylik ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(ydf.groupby('month')['views'].sum(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center; color: black;'>Bo'limlar bo'yicha oylik ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.line_chart(ydf.groupby('month')['views'].sum(), use_container_width=True, height=500, width=500)



elif choice == "Bo'limlar Tahlili":
    st.markdown("<h1 style='text-align: center; color: black;'>Bo'limlar Tahlil</h1>", unsafe_allow_html=True)

    bmenu = bdf['section'].unique()
    side_section = st.sidebar.selectbox('Tanlov', bmenu)
    bdf = bdf[bdf['section'] == side_section]
    bdisplay_data = bdf.copy()
    bdisplay_data = bdisplay_data[['section', 'views', 'date']]

    if st.button("Ma'lumotlar", use_container_width=True):
        st.dataframe(bdisplay_data, use_container_width=True)

    st.markdown("<br><h3 style='text-align: center; color: black;'>Yillar bo'yicha savollar</h3><br>", unsafe_allow_html=True)
    st.bar_chart(bdf['year'].value_counts(), use_container_width=True, height=500, width=500)
    st.line_chart(bdf['year'].value_counts(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center; color: black;'>Yillar bo'yicha umumiy ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(bdf.groupby('year')['views'].sum(), use_container_width=True, height=500, width=500)
    st.line_chart(bdf.groupby('year')['views'].sum(), use_container_width=True, height=500, width=500)



elif choice == "Smart Qidiruv":
    st.markdown("<h1 style='text-align: center; color: black;'>Smart Qidiruv</h1>", unsafe_allow_html=True)

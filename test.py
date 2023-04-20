import streamlit as st
import pandas as pd
import io
from pathlib import Path
st.cache(allow_output_mutation=True)

#data = Path('new_data.csv').parents[0] / 'Data-Analysis-for-savollar.islom.uz/Data_Analysis/new_data.csv'
df = pd.read_csv('new_data.csv', encoding='utf-8')
udf = df.copy()
ydf = df.copy()
bdf = df.copy()


st.sidebar.markdown("<h1 style='text-align: center;'>DATA CLUB</h1>", unsafe_allow_html=True) # Creating a header.
menu = ["Bosh Sahifa", "Umumiy Tahlil", "Yillik Tahlil", "Bo'limlar Tahlili" , "Smart Qidiruv"]
choice = st.sidebar.selectbox('Menu', menu)


if choice == "Bosh Sahifa":
    st.markdown("<h1 style='text-align: center;'>BOSH SAHIFA</h1>", unsafe_allow_html=True) # Creating a header.
    st.markdown("<h5 style='text-align: center;'>DATA CLUB tomonidan savollar.islom.uz veb ilovasi uchun tayyorlangan Ma'lumotlar tahlili.</h5>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Tahlil haqida</h2>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Tahlil savolllar.islom.uz ilovasiga 2006-2022 yillar oralig'ida berilgan savollar va javoblarlar, savol berilagan vaqt hamda ko'rishlar soni orqali tuzildi. Umumiy savollar soni: 71607. Ilovaga umumiy tashrif buyurganlar soni: 181808962. Asosiy bo'limlar: Turli Savollar, Dolzarb Savollar, Oila va Turmush hamda Halol va Harom. Ilova orqali 2016-2021 yillar oralig'ida yiliga o'rtacha 6000-6500 savolga javob berilgan. 2022-yilda esa 4700 savol kelib tushgan. 2022-yilda eng ko'p savollar Turli Savollar(1011), Halol va Harom(657), Moliya va Tijorat(525), Oila va Turmush(511), Namoz(383) bo'limida.</h5>", unsafe_allow_html=True)



elif choice == "Umumiy Tahlil":
    st.markdown("<h1 style='text-align: center;'>Umumiy Tahlil</h1>", unsafe_allow_html=True)
    if st.button("Ma'lumotlar", use_container_width=True):
        st.dataframe(udf, use_container_width=True)


    st.markdown("<br><h3 style='text-align: center;'>Bo'limlar bo'yicha savollar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(udf['section'].value_counts(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center;'>Bo'limlar bo'yicha umumiy ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(udf.groupby('section')['views'].sum(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center;'>Yillik savollar soni</h3><br>", unsafe_allow_html=True) 
    st.bar_chart(udf['year'].value_counts(), use_container_width=True, height=500, width=500)
    st.line_chart(udf['year'].value_counts(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center;'>Yillik ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(udf.groupby('year')['views'].sum(), use_container_width=True, height=500, width=500)
    st.line_chart(udf.groupby('year')['views'].sum(), use_container_width=True, height=500, width=500)



elif choice == "Yillik Tahlil":
    st.markdown("<h1 style='text-align: center;'>Yillik Tahlil</h1>", unsafe_allow_html=True)

    menu2 = ydf['year'].unique()
    side_year = st.sidebar.selectbox('Tanlov', menu2)
    ydf = ydf[ydf['year'] == side_year]
    display_data = ydf.copy()
    display_data = display_data[['section', 'views', 'date']]

    if st.button("Ma'lumotlar", use_container_width=True):
        st.dataframe(display_data, use_container_width=True)

    st.markdown("<br><h3 style='text-align: center;'>Bo'limlar bo'yicha savollar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(ydf['section'].value_counts(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center;'>Bo'limlar bo'yicha umumiy ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(ydf.groupby('section')['views'].sum(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center;'>Bo'limlar bo'yicha oylik ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(ydf.groupby('month')['views'].sum(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center;'>Bo'limlar bo'yicha oylik ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.line_chart(ydf.groupby('month')['views'].sum(), use_container_width=True, height=500, width=500)



elif choice == "Bo'limlar Tahlili":
    st.markdown("<h1 style='text-align: center;'>Bo'limlar Tahlil</h1>", unsafe_allow_html=True)

    bmenu = bdf['section'].unique()
    side_section = st.sidebar.selectbox('Tanlov', bmenu)
    bdf = bdf[bdf['section'] == side_section]
    bdisplay_data = bdf.copy()
    bdisplay_data = bdisplay_data[['section', 'views', 'date']]

    if st.button("Ma'lumotlar", use_container_width=True):
        st.dataframe(bdisplay_data, use_container_width=True)

    st.markdown("<br><h3 style='text-align: center;'>Yillar bo'yicha savollar</h3><br>", unsafe_allow_html=True)
    st.bar_chart(bdf['year'].value_counts(), use_container_width=True, height=500, width=500)
    st.line_chart(bdf['year'].value_counts(), use_container_width=True, height=500, width=500)

    st.markdown("<br><h3 style='text-align: center;'>Yillar bo'yicha umumiy ko'rishlar soni</h3><br>", unsafe_allow_html=True)
    st.bar_chart(bdf.groupby('year')['views'].sum(), use_container_width=True, height=500, width=500)
    st.line_chart(bdf.groupby('year')['views'].sum(), use_container_width=True, height=500, width=500)



elif choice == "Smart Qidiruv":
    st.markdown("<h1 style='text-align: center;'>Smart Qidiruv</h1>", unsafe_allow_html=True)

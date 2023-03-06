import streamlit as st # Importing streamlit, a python library for creating web apps.
import pandas as pd # Importing pandas, a python library for data analysis.
import matplotlib.pyplot as plt # Importing matplotlib, a python library for data visualization.
import plotly.express as px # Importing plotly express, a python library for data visualization.
import seaborn as sns # Importing seaborn, a python library for data visualization.
from password import pcode # Importing the password.py file.
# st.set_page_config( layout='wide') # Setting the page layout to wide.

#df = pd.read_csv('dataset.csv') # Reading the heart.csv file.
df = px.data.gapminder() # Reading the gapminder dataset.

def show_data(): # Creating a function for displaying the dataset.
    st.markdown("<h2 style='text-align: center; color: black;'>MA'LUMOTLAR</h2>", unsafe_allow_html=True) # Creating a header.
    st.write(df) # Displaying the dataset.

def graph_plot(): # Creating a function for displaying the graphs.
    st.markdown("<h2 style='text-align: center; color: black;'>Grafik</h2>", unsafe_allow_html=True) # Creating a header.
    #year_options = df['year'].unique().tolist() # Creating a variable for the year.
    #year = st.selectbox('Yilni tanlang', year_options, 0) # Creating a selectbox for the year.
    #df_year = df[df['year'] == year] # Creating a variable for the year.

    fig = px.scatter(df , x = 'gdpPercap', y = 'lifeExp', 
                     size ='pop', color = 'continent', hover_name = 'continent', 
                     log_x = True, size_max = 55, range_x = [180,180000], range_y = [25,90],
                     animation_frame="year", animation_group="country") # Creating a scatter plot.
    
    fig.update_layout(width = 800)
    st.write(fig) # Displaying the scatter plot.

def graph_plot2():
    st.markdown("<h2 style='text-align: center; color: black;'>Grafik</h2>", unsafe_allow_html=True) # Creating a header.
    covid = pd.read_csv('https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv') # Reading the covid-19 dataset.
    covid.columns = ['Country', 'Code', 'Date', 'Confirmed', 'Days since confirmed'] # Renaming the columns.
    covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d') # Converting the date column to datetime.
    st.write(covid) # Displaying the dataset.

    country_options = covid['Country'].unique().tolist() # Creating a variable for the country.
    date_options = covid['Date'].unique().tolist() # Creating a variable for the date.
    #date = st.selectbox('Sana tanlang', date_options, 100) # Creating a selectbox for the date.
    country = st.multiselect('Mamlakatni tanlang', country_options, ['China']) # Creating a multiselect for the country.

    covid = covid[covid['Country'].isin(country)] # Creating a variable for the country.
    #covid = covid[covid['Date'] == date] # Creating a variable for the date.

    fig = px.bar(covid, x = 'Country', y = 'Confirmed', color = 'Country', range_y=[0,35000], animation_frame="Date", animation_group="Country") # Creating a bar plot.
    
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 30 # Setting the animation speed.
    fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 5 # Setting the animation speed.

    fig.update_layout(width = 800)
    st.write(fig) # Displaying the bar plot.
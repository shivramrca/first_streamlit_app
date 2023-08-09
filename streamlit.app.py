import streamlit
streamlit.title("My parents healthy new diner")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hardboiled FreeRange Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets put a picklist here so that users can pick the fruits of their choice
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index,default=['Avacado','Strawberries']))

# display the table on the list
streamlit.dataframe(my_fruit_list)


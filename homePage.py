import streamlit as st
from PIL import Image

st.set_page_config( layout='centered', initial_sidebar_state='expanded')

st. sidebar.image('./Data/App_icon.png')

image = Image.open('./rrr.jpg')
st.image(image, use_column_width=True)
st.warning("THE APP TO GET YOU TO THE CLOSEST AND MOST HIGHLY RATED PLACES TO EAT!! :cake:")
st.markdown("Based on data from TripAdvisor, the app covers restaurants form 5 cities across New York, New Jersey, California, Texas and Washington to recommend the 10 most similar restaurants to the one you like. ")
st.markdown("This app uses Natural Language Processing and Content Based Recommender Systems with focusing on user comments as the main feature.")
st.success(" Hunger is also an emergency!! :ambulance:" ":100:")

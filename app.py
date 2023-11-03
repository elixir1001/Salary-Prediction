import streamlit as st

from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))
# We're using a select box to select which page we're going to show, which itself is going to be on the side bar.
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
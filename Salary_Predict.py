import streamlit as st
from predict_page import show_predict_page 
from explore_page import show_explore_page

a = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))
if a == "Predict":
    show_predict_page()
else:
    show_explore_page()


st.write("""Created By Chetan :)""")
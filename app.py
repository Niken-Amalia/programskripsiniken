import streamlit as st

st.title("Tes Streamlit")

import pandas as pd
st.write("Pandas:", pd.__version__)

import sklearn
st.write("Sklearn:", sklearn.__version__)

import joblib
st.write("Joblib:", joblib.__version__)

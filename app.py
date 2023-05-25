import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st


df = pd.read_csv('./data_df.csv', encoding='cp949')

st.subheader('this is table')
st.table(df.head())

st.subheader('this is data frame')
st.dataframe(df.head())

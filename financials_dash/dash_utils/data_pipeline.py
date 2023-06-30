import pandas as pd
import streamlit as st

@st.cache_data
def join_dataset(df_1,df_2):
    joined_set = df_1.merge(df_2, left_on = df_1.company, right_on=df_2.company)
    return joined_set


df_finance = pd.read_csv('data/sample_financial_data.csv')
df_investor = pd.read_csv('data/sample_investor_data.csv')
df_joined = join_dataset(df_finance,df_investor)

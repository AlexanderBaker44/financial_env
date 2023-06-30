import streamlit as st
import pandas as pd
from dash_utils.data_pipeline import df_finance, df_investor, df_joined
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.header('Financial Dash')
companies = list(set(df_finance['company']))
input_company = st.selectbox('Select Company',companies)
seq_list = st.multiselect('Select Sequences',['revenue','rnd','net_income','free_cash_flow'],'revenue')


filtered_df_finance = df_finance[df_finance['company'] == input_company]
filtered_df_investor = df_investor[df_investor['company'] == input_company]



year = st.slider('Select Year',min(df_joined['year_x']), max(df_joined['year_x']), value = (2015,2020))
filtered_df_year_and_comp = filtered_df_finance[(filtered_df_finance['year'] >= year[0]) & (filtered_df_finance['year'] <= year[1])]
filtered_df_investor_year_and_comp = filtered_df_investor[(filtered_df_investor['year'] >= year[0]) & (filtered_df_investor['year'] <= year[1])]

st.subheader(f'Information for Company: {input_company}')
col1,col2 = st.columns(2)
with col1:
    filtered_df_finance.groupby('year').sum()[seq_list].plot(kind='line',ylabel = 'USD ($)')
    st.pyplot()
    st.write('Overall FInancials')
    filtered_df_year_and_comp.groupby('company').sum().plot(kind='bar', title = f'Finance Data for Years: {year[0]} through {year[1]}', ylabel = 'USD ($)')
    st.pyplot()

with col2:
    filtered_df_investor.groupby(['year','customer']).sum().unstack().plot(kind='bar',stacked=True,ylabel = 'Amount USD ($)')
    st.pyplot()
    filtered_df_investor.groupby('customer').sum()['amount'].plot(kind = 'pie', title = f'Total Revenue per Customer',ylabel = 'Amount USD ($)')
    st.pyplot()

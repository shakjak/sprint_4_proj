import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

df["model_year"] = df["model_year"].fillna(0).astype(int)
df["cylinders"] = df["cylinders"].fillna(0).astype(int)
df["odometer"] = df["odometer"].fillna(0).astype(int)
df["is_4wd"] = df["is_4wd"].fillna(0).astype(int)
df["date_posted"] = pd.to_datetime(df["date_posted"])
df["type"] = df["type"].str.lower()
df["paint_color"] = df["paint_color"].fillna('no color')
df = df.sort_values(by="date_posted")
df = df.reset_index(drop=True)
company_and_model = df['model'].str.split(' ')
df['company'] = company_and_model.apply(lambda lst: lst[0])
df['model'] = company_and_model.apply(lambda lst: " ".join(lst[1:]))
df['month_posted'] = df['date_posted'].dt.to_period('M')   

fig = px.histogram(df,x='type',title='Histogram for type')

st.header('Histogram Graphs')
st.plotly_chart(fig,use_container_width=True)

fig2 = px.scatter(df,x='date_posted',y='price',title='Price of Vehichiles by Date',color='type')
checkbox = st.checkbox('Scatter plot of Vehicle Prices and Date Posted')

if checkbox:
    st.header('Scatter plot of Vehicle Prices and Date Posted')
    st.plotly_chart(fig2)
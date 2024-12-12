import pandas as pd
import streamlit as st
import plotly.express as px

try:
    df = pd.read_csv('vehicles_us.csv')
except: 
    df = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv')

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

st.write("""In our data set, most of the vehicles were either, 
         sedans, trucks, pickups, and suvs. The amount of other type 
         of vehicle were quite minimal in comparison to the volume of 
         the main 4 vehicle types.""")

fig2 = px.scatter(df,x='date_posted',y='price',title='Price of Vehichiles by Date',color='type')

checkbox = st.checkbox('Scatter plot of Vehicle Prices and Date Posted')

if checkbox:
    st.header('Scatter plot of Vehicle Prices and Date Posted')
    st.plotly_chart(fig2)
    st.write("""The data in the scatter plot reflects that the prices
              for their inventory didn't have too much devitation. The bulk 
             of the pricing stayed within the 5000 to 170000 dollar range.""")
    
st.header("Conlcusion")
st.write("""In the data vehicles_us data, we found that the bulk of the inventory
          was divided between 4 vehicle types. Sedan, Suv, Trucks, and Pickups.
          
         The averages of the price per type is,truck: 16734.89,suv: 11149.40, 
         sedan: 6965.35, and pickup: 16057.41. Also noted in the data is that they 
         looked to have a consitant abmount of inventory at the location at all times. 
         This is based on the scatter plot data.""")
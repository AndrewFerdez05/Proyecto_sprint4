import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Data de venta de vehículos')
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_histogram = st.button('Construir histograma') # crear un botón
disp_button = st.button('Construir diagrama de dispersión') # crear un botón

        
if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
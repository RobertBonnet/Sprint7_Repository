import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('/Users/robert.bonnet/Documents/Notebooks/Repositorys/Sprint7_Repository/vehicles_us.csv') # leer los datos

# Título de la aplicación
st.title("Cuadro de Mandos de Análisis de Datos de Coches")

# Descripción general de la aplicación
st.write("""
    Esta aplicación permite explorar y analizar datos de coches de segunda mano.
    El conjunto de datos incluye información sobre el precio, el kilometraje (odómetro),
    la marca, el modelo y otras características relevantes.
""")

# Agregar un encabezado
st.header("Análisis Exploratorio de Datos (EDA)")

# Agregar una breve explicación debajo del encabezado
st.write("""
    A continuación, podrás explorar visualmente diferentes características del conjunto de datos,
    como la distribución del precio de los coches y la relación entre el precio y el kilometraje.
""")

# Mostrar las primeras filas del conjunto de datos
st.write("Vista previa de los datos:")
st.dataframe(car_data.head())

# Gráfico de dispersión entre precio y odómetro
fig = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión: Odometer vs Price")
st.plotly_chart(fig)

# Gráfico de histograma del precio
fig2 = px.histogram(car_data, x="price", title="Distribución del Precio de los Coches")
st.plotly_chart(fig2)

# Agregar un botón para generar el gráfico de dispersión
if st.button('Generar gráfico de dispersión'):
    fig3 = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión generado por botón")
    st.plotly_chart(fig3)

# Agregar un botón para generar el histograma
if st.button('Generar histograma de precios'):
    # Crear el histograma de precios
    hist_fig = px.histogram(car_data, x="price", title="Distribución de los Precios de los Coches")
    # Mostrar el histograma
    st.plotly_chart(hist_fig)

if st.checkbox('Generar gráfico de dispersión: Year vs Price'):
    fig4 = px.scatter(car_data, x="year", y="price", title="Gráfico de dispersión: Año vs Precio")
    st.plotly_chart(fig4)

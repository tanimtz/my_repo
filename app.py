import pandas as pd
import plotly.express as px
import streamlit as st

# ----------------------------
# Título de la app
# ----------------------------
st.header("Análisis de Anuncios de Vehículos en EE.UU.")

# ----------------------------
# Cargar datos
# ----------------------------
df = pd.read_csv("vehicles_us.csv")

# Limpieza básica (opcional si ya lo hiciste en EDA, pero es buena práctica repetirlo aquí)
df["date_posted"] = pd.to_datetime(df["date_posted"])
df["model_year"] = df["model_year"].fillna(df["model_year"].median())
df["cylinders"] = df["cylinders"].fillna(df["cylinders"].median())
df["odometer"] = df["odometer"].fillna(df["odometer"].median())
df["paint_color"] = df["paint_color"].fillna("unknown")
df["is_4wd"] = df["is_4wd"].fillna(0).astype(int)

# ----------------------------
# Texto descriptivo
# ----------------------------
st.write("Esta aplicación permite explorar datos de anuncios de vehículos usados en Estados Unidos.")

# Botón para histograma
# ----------------------------  
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de vehículos')
    fig_hist = px.histogram(df, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# ----------------------------
# Botón para gráfico de dispersión
# ----------------------------
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión precio vs kilometraje')
    fig_scatter = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)

import streamlit as st
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("valorant champions istanbul.csv")

st.title("Datos que creemos te gustaíran saber")

keyword = st.text_input("Ingrese la palabra clave:", "")

def mejor_rendimiento():
    # Seleccionar las filas 1 y 7 (recuerda que el índice comienza en 0)
    filas_seleccionadas = df.iloc[[5]]  

    # Mostrar las filas seleccionadas como un DataFrame en Streamlit
    st.dataframe(filas_seleccionadas)

def peor_rendimiento():
    # Seleccionar las filas 1 y 7 (recuerda que el índice comienza en 0)
    filas_seleccionadas = df.iloc[[20]]  

    # Mostrar las filas seleccionadas como un DataFrame en Streamlit
    st.dataframe(filas_seleccionadas)

def mas_kills():
    # Seleccionar las filas 1 y 7 (recuerda que el índice comienza en 0)
    filas_seleccionadas = df.iloc[[5]]  

    # Mostrar las filas seleccionadas como un DataFrame en Streamlit
    st.dataframe(filas_seleccionadas)

def mejor_rendimiento_por_equipo():
    # Seleccionar las filas 1 y 7 (recuerda que el índice comienza en 0)
    filas_seleccionadas = df.iloc[[4,5,11,19,24,27,33,36]]  

    # Mostrar las filas seleccionadas como un DataFrame en Streamlit
    st.dataframe(filas_seleccionadas)

if st.button("Cuál fué jugador con mejor rendimiento global del torneo"):
    mejor_rendimiento()

if st.button("Cuál fué ugador con peor rendimiento global del torneo"):
    peor_rendimiento()

if st.button("Cuál fué el jugador con más kills?"):
   mas_kills()
    
if st.button("Cuales fueron los jugadores con mejor rendimiento de cada equipo."):
    mejor_rendimiento_por_equipo()


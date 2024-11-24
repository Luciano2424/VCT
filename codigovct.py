import streamlit as st
import pandas as pd

# Carga de datos
df = pd.read_csv("valorant champions istanbul.csv")

# Definición de funciones para cada "página"
def mejor_rendimiento():
    filas_seleccionadas = df.iloc[[5]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)

def peor_rendimiento():
    filas_seleccionadas = df.iloc[[19]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)

def mas_kills():
    filas_seleccionadas = df.iloc[[5]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)

def mejor_rendimiento_por_equipo():
    filas_seleccionadas = df.iloc[[3, 5, 10, 17, 22, 25, 32, 35]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)

# Título principal
st.title("Navegación entre Páginas de Datos")

# Crear el selectbox para navegar entre las páginas
page_selection = st.selectbox(
    "Selecciona una opción para ver los datos:",
    [
        "Seleccione una opción",
        "Mejor rendimiento global",
        "Peor rendimiento global",
        "Jugador con más kills",
        "Mejor rendimiento por equipo"
    ]
)

# Cambiar el título de la página dinámicamente
if page_selection == "Mejor rendimiento global":
    st.set_page_config(page_title="Página 1")  # Cambiar título de la página
    mejor_rendimiento()
elif page_selection == "Peor rendimiento global":
    st.set_page_config(page_title="Página 2")  # Cambiar título de la página
    peor_rendimiento()
elif page_selection == "Jugador con más kills":
    st.set_page_config(page_title="Página 3")  # Cambiar título de la página
    mas_kills()
elif page_selection == "Mejor rendimiento por equipo":
    st.set_page_config(page_title="Página 4")  # Cambiar título de la página
    mejor_rendimiento_por_equipo()
else:
    st.write("Selecciona una opción válida.")

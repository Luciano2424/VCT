import streamlit as st
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("valorant champions istanbul.csv")

# Asegúrate de que la imagen de fondo esté en el mismo directorio
image_path = "Fondo.jpg"

# Funciones para mostrar los datos
def mejor_rendimiento():
    filas_seleccionadas = df.iloc[[5]]  
    st.dataframe(filas_seleccionadas)

def peor_rendimiento():
    filas_seleccionadas = df.iloc[[19]]  
    st.dataframe(filas_seleccionadas)

def mas_kills():
    filas_seleccionadas = df.iloc[[5]]  
    st.dataframe(filas_seleccionadas)

def mejor_rendimiento_por_equipo():
    filas_seleccionadas = df.iloc[[3,5,10,16,22,25,32,35]]  
    st.dataframe(filas_seleccionadas)

# Establece el fondo de la página con la imagen "fondo.jpg"
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background-image: url({image_path});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            color: white;
        }}
        .stButton>button {{
            background-color: rgba(0, 0, 0, 0.5);
            color: white;
            font-size: 20px;
            border-radius: 8px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la página
st.title("Datos que creemos te gustarán saber")

# Función para manejar la navegación entre páginas
if "page" not in st.session_state:
    st.session_state.page = "home"

# Página principal (home)
if st.session_state.page == "home":
    if st.button("Cuál fue el jugador con mejor rendimiento global del torneo"):
        st.session_state.page = "mejor_rendimiento"
    if st.button("Cuál fue el jugador con peor rendimiento global del torneo"):
        st.session_state.page = "peor_rendimiento"
    if st.button("Cuál fue el jugador con más kills?"):
        st.session_state.page = "mas_kills"
    if st.button("Cuáles fueron los jugadores con mejor rendimiento de cada equipo?"):
        st.session_state.page = "mejor_rendimiento_por_equipo"

# Página para mostrar el "mejor rendimiento"
elif st.session_state.page == "mejor_rendimiento":
    mejor_rendimiento()
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

# Página para mostrar el "peor rendimiento"
elif st.session_state.page == "peor_rendimiento":
    peor_rendimiento()
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

# Página para mostrar el "jugador con más kills"
elif st.session_state.page == "mas_kills":
    mas_kills()
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

# Página para mostrar el "mejor rendimiento por equipo"
elif st.session_state.page == "mejor_rendimiento_por_equipo":
    mejor_rendimiento_por_equipo()
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"


import streamlit as st
import pandas as pd
from PIL import Image  # Asegúrate de que esta importación esté presente

# Establecer la configuración de la página al principio
st.set_page_config(page_title="Página de Datos", page_icon="📊", layout="centered")

# Cargar el archivo CSV
df = pd.read_csv("valorant champions istanbul.csv")

image_yay = "yay.jpeg"
image_Cryocells = "Cryocells.jpg"
image_ANGE1 = "ANGE1.jpg"
image_Derke = "Derke.jpg"
image_MaKo = "MaKo.jpg"
image_Scream = "Scream.jpg"
image_kiNgg = "kiNgg.jpg"
image_suygetsu = "suygetsu.jpg"
image_Less = "Less.jpeg"

# Definir las funciones para cada "página"
def mejor_rendimiento():
    filas_seleccionadas = df.iloc[[5]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)
    
    # Asegúrate de que la imagen "yay.jpg" esté en la misma carpeta que el código
    try:
        image_yay = Image.open("yay.jpeg")  # Verifica que el archivo yay.jpg esté en la carpeta correcta
        st.image(image_yay, caption="yay - Mejor rendimiento")
    except Exception as e:
        st.error(f"No se pudo cargar la imagen: {e}")
    
    # Volver a la página principal
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

def peor_rendimiento():
    filas_seleccionadas = df.iloc[[19]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)
    # Asegúrate de que la imagen "yay.jpg" esté en la misma carpeta que el código
    try:
        image_yay = Image.open("yay.jpeg")  # Verifica que el archivo yay.jpg esté en la carpeta correcta
        st.image(image_yay, caption="ANGE1 - Rendimiento más bajo")
    except Exception as e:
        st.error(f"No se pudo cargar la imagen: {e}")    
        
    # Volver a la página principal
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

def mas_kills():
    filas_seleccionadas = df.iloc[[5]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)
    
    # Volver a la página principal
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

def mejor_rendimiento_por_equipo():
    filas_seleccionadas = df.iloc[[3, 5, 10, 17, 22, 25, 32, 35]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)
    
    # Volver a la página principal
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

# Configurar la página de inicio si no existe en el estado de sesión
if "page" not in st.session_state:
    st.session_state.page = "home"

# Página principal (home)
if st.session_state.page == "home":
    st.title("Bienvenido a la página principal")
    
    # Selección de la página a navegar
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

    # Cambiar el estado de la página
    if page_selection == "Mejor rendimiento global":
        st.session_state.page = "mejor_rendimiento"
    elif page_selection == "Peor rendimiento global":
        st.session_state.page = "peor_rendimiento"
    elif page_selection == "Jugador con más kills":
        st.session_state.page = "mas_kills"
    elif page_selection == "Mejor rendimiento por equipo":
        st.session_state.page = "mejor_rendimiento_por_equipo"

# Página 1: Mejor rendimiento
elif st.session_state.page == "mejor_rendimiento":
    st.title("Página 1 - Mejor rendimiento global")
    mejor_rendimiento()

# Página 2: Peor rendimiento
elif st.session_state.page == "peor_rendimiento":
    st.title("Página 2 - Peor rendimiento global")
    peor_rendimiento()

# Página 3: Jugador con más kills
elif st.session_state.page == "mas_kills":
    st.title("Página 3 - Jugador con más kills")
    mas_kills()

# Página 4: Mejor rendimiento por equipo
elif st.session_state.page == "mejor_rendimiento_por_equipo":
    st.title("Página 4 - Mejor rendimiento por equipo")
    mejor_rendimiento_por_equipo()

import streamlit as st
import pandas as pd
from PIL import Image  

df = pd.read_csv("valorant champions istanbul.csv")

image_yay = "yay.jpeg"
image_ANGE1 = "ANGE1.jpg"
image_MaKo = "MaKo.jpg"
image_suygetsu = "suygetsu.jpg"


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
    filas_seleccionadas = df.iloc[[3,5,10,17,22,25,32,35]]  
    st.dataframe(filas_seleccionadas)

if "page" not in st.session_state:
    st.session_state.page = "home"

def resize_image(image_path, width=130, height=152):
    img = Image.open(image_path)  
    img_resized = img.resize((width, height))  
    return img_resized

# Función para mostrar imagen y leyenda centrados
def display_image_with_caption(image_path, caption):
    img_resized = resize_image(image_path)
    col = st.columns(1)  # Usamos 1 columna para centrar la imagen
    with col[0]:
        st.image(img_resized)
        st.markdown(
            f"""
            <style>
            .caption {{
                font-family: 'Arial Black', sans-serif;
                font-size: 18px;
                font-weight: bold;
                text-align: center;
            }}
            </style>
            <p class="caption">{caption}</p>
            """, unsafe_allow_html=True
        )

if st.session_state.page == "home":
    st.title("Datos que creemos te gustarán saber")
    
    if st.button("Cuál fue el jugador con mejor rendimiento global del torneo"):
        st.session_state.page = "mejor_rendimiento"
    if st.button("Cuál fue el jugador con peor rendimiento global del torneo"):
        st.session_state.page = "peor_rendimiento"
    if st.button("Cuál fue el jugador con más kills?"):
        st.session_state.page = "mas_kills"
    if st.button("Cuáles fueron los jugadores con mejor rendimiento de cada equipo?"):
        st.session_state.page = "mejor_rendimiento_por_equipo"

elif st.session_state.page == "mejor_rendimiento":
    st.title("Jugador con mejor rendimiento")
    mejor_rendimiento()
    display_image_with_caption(image_yay, "Presentación yay")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "peor_rendimiento":
    st.title("Jugador con rendimiento más bajo")
    peor_rendimiento()
    display_image_with_caption(image_ANGE1, "Presentación ANGE1")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "mas_kills":
    st.title("Jugador con más bajas")
    mas_kills()
    col1, col2 = st.columns(2)
        with col1:
            display_image_with_caption(image_MaKo, "Presentación yay")
        with col2:
            display_image_with_caption(image_br, "Nacionalidad")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "mejor_rendimiento_por_equipo":
    st.title("Jugadores con el mejor rendimiento por equipo")
    mejor_rendimiento_por_equipo()

    # Usando las columnas para mostrar las imágenes
    col1, col2, col3, col4 = st.columns(4)  
    with col1:
        display_image_with_caption(image_MaKo, "MaKo Top 1")

    with col2:
        display_image_with_caption(image_yay, "yay Top 2")

    with col3:
        display_image_with_caption(image_MaKo, "MaKo Top 3")

    with col4:
        display_image_with_caption(image_suygetsu, "suygetsu Top 4")

    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

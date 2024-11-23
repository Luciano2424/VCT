import streamlit as st
import pandas as pd
from PIL import Image  

df = pd.read_csv("valorant champions istanbul.csv")

image_path_fondo = "Fondo.png"
image_path_duelistas = "duelistas.jpg"
image_yay = "yay.jpeg"
image_Cryocells = "Cryocells.jpg"
image_ANGE1 = "ANGE1.jpg"
image_Derke = "Derke.jpg"
image_MaKo = "MaKo.jpg"
image_Scream = "Scream.jpg"
image_kiNgg = "kiNgg.jpg"
image_suygetsu = "suygetsu.jpg"
image_Less = "Less.jpeg"


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

if st.session_state.page == "home":  
    st.title("Datos que creemos te gustarán saber")

if "page" not in st.session_state:
    st.session_state.page = "home"

def resize_image(image_path, width=130, height=152):
    img = Image.open(image_path)  
    img_resized = img.resize((width, height))  
    return img_resized

if st.session_state.page == "home":
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
    img_resized_yay = resize_image(image_yay)
    st.image(img_resized_yay, caption="Presentación yay")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "peor_rendimiento":
    st.title("Jugador con rendimiento mas bajo")
    peor_rendimiento()
    img_resized_ange1 = resize_image(image_ANGE1)
    st.image(img_resized_ange1, caption="Presentación ANGE1")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "mas_kills":
    st.title("Jugador con más bajas")
    mas_kills()
    img_resized_yay = resize_image(image_yay)
    st.image(img_resized_yay, caption="Presentación yay")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "mejor_rendimiento_por_equipo":
    st.title("Jugadores con el mejor rendimiento por equipo")
    mejor_rendimiento_por_equipo()
    
    col1, col2, col3, col4 = st.columns(4)  
    with col1:
        img_resized_Less = resize_image(image_Less)
        st.image(img_resized_Less, caption="Less Top 1")

    with col2:
        img_resized_yay = resize_image(image_yay)
        st.image(img_resized_yay, caption="yay Top 2")

    with col3:
        img_resized_MaKo = resize_image(image_MaKo)
        st.image(img_resized_MaKo, caption="MaKo Top 3")

    with col4:
        img_resized_suygetsu = resize_image(image_suygetsu)
        st.image(img_resized_suygetsu, caption="suygetsu Top 4")

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        img_resized_Cryocells = resize_image(image_Cryocells)
        st.image(img_resized_Cryocells, caption="Cryocells Top 5")

    with col6:
        img_resized_Derke = resize_image(image_Derke)
        st.image(img_resized_Derke, caption="Derke Top 6")

    with col7:
        img_resized_Scream = resize_image(image_Scream)
        st.image(img_resized_Scream, caption="Scream Top 7")

    with col8:
        img_resized_kiNgg = resize_image(image_kiNgg)
        st.image(img_resized_kiNgg, caption="kiNgg Top 8")

    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

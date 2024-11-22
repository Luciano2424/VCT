import streamlit as st
import pandas as pd
from PIL import Image

# Cargar el archivo CSV
df = pd.read_csv("valorant champions istanbul.csv")

# Asegúrate de que las imágenes estén en el mismo directorio
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
    filas_seleccionadas = df.iloc[[3,5,10,17,22,25,32,35]]  
    st.dataframe(filas_seleccionadas)

# Función para redimensionar la imagen
def resize_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))  # Redimensiona la imagen
    return img

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
    # Redimensionar la imagen y mostrarla
    st.tittle("Jugador con mejor rendimiento del torneo")
    img_yay = resize_image(image_yay, 240, 288)
    st.image(img_yay, caption="")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

# Página para mostrar el "peor rendimiento"
elif st.session_state.page == "peor_rendimiento":
    peor_rendimiento()
    # Redimensionar la imagen y mostrarla
    st.tittle("Jugador con peor rendimiento del torneo")
    img_ange1 = resize_image(image_ANGE1, 240, 288)
    st.image(img_ange1, caption="Presentación ANGE1")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

# Página para mostrar el "jugador con más kills"
elif st.session_state.page == "mas_kills":
    mas_kills()
    # Redimensionar la imagen y mostrarla
    st.tittle("Jugador conmás kills del torneo")
    img_yay = resize_image(image_yay, 240, 288)
    st.image(img_yay, caption="Presentación yay")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

# Página para mostrar el "mejor rendimiento por equipo"
elif st.session_state.page == "mejor_rendimiento_por_equipo":
    mejor_rendimiento_por_equipo()
    # Redimensionar las imágenes y mostrarlas
    st.tittle("Jugadores con mejor rendimiento del torneo por equipo")
    img_Less = resize_image(image_Less, 240, 288)
    img_yay = resize_image(image_yay, 240, 288)
    img_MaKo = resize_image(image_MaKo, 240, 288)
    img_suygetsu = resize_image(image_suygetsu, 240, 288)
    img_Cryocells = resize_image(image_Cryocells, 240, 288)
    img_Derke = resize_image(image_Derke, 240, 288)
    img_Scream = resize_image(image_Scream, 240, 288)
    img_kiNgg = resize_image(image_kiNgg, 240, 288)

    # Mostrar las imágenes redimensionadas
    st.image(img_Less, caption="Presentación Less")
    st.image(img_yay, caption="Presentación yay")
    st.image(img_MaKo, caption="Presentación MaKo")
    st.image(img_suygetsu, caption="Presentación suygetsu")
    st.image(img_Cryocells, caption="Presentación Cryocells")
    st.image(img_Derke, caption="Presentación Derke")
    st.image(img_Scream, caption="Presentación Scream")
    st.image(img_kiNgg, caption="Presentación kiNgg")

    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

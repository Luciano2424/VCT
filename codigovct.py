import streamlit as st
import pandas as pd
from PIL import Image  # Añadir esta importación para trabajar con imágenes

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

# Título de la página
st.title("Datos que creemos te gustarán saber")

# Función para manejar la navegación entre páginas
if "page" not in st.session_state:
    st.session_state.page = "home"

# Función para redimensionar imágenes
def resize_image(image_path, width=113, height=152):
    img = Image.open(image_path)  # Abrir la imagen
    img_resized = img.resize((width, height))  # Redimensionar la imagen
    return img_resized

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
    # Redimensionar y mostrar las imágenes
    img_resized_yay = resize_image(image_yay)
    st.image(img_resized_yay, caption="Presentación yay")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

# Página para mostrar el "peor rendimiento"
elif st.session_state.page == "peor_rendimiento":
    peor_rendimiento()
    # Redimensionar y mostrar las imágenes
    img_resized_ange1 = resize_image(image_ANGE1)
    st.image(img_resized_ange1, caption="Presentación ANGE1")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

# Página para mostrar el "jugador con más kills"
elif st.session_state.page == "mas_kills":
    mas_kills()
    # Redimensionar y mostrar las imágenes
    img_resized_yay = resize_image(image_yay)
    st.image(img_resized_yay, caption="Presentación yay")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

# Página para mostrar el "mejor rendimiento por equipo"
elif st.session_state.page == "mejor_rendimiento_por_equipo":
    mejor_rendimiento_por_equipo()
    # Redimensionar y mostrar las imágenes
    img_resized_Less = resize_image(image_Less)
    st.image(img_resized_Less, caption="Presentación Less")
    
    img_resized_yay = resize_image(image_yay)
    st.image(img_resized_yay, caption="Presentación yay")
    
    img_resized_MaKo = resize_image(image_MaKo)
    st.image(img_resized_MaKo, caption="Presentación MaKo")
    
    img_resized_suygetsu = resize_image(image_suygetsu)
    st.image(img_resized_suygetsu, caption="Presentación suygetsu")
    
    img_resized_Cryocells = resize_image(image_Cryocells)
    st.image(img_resized_Cryocells, caption="Presentación Cryocells")
    
    img_resized_Derke = resize_image(image_Derke)
    st.image(img_resized_Derke, caption="Presentación Derke")
    
    img_resized_Scream = resize_image(image_Scream)
    st.image(img_resized_Scream, caption="Presentación Scream")
    
    img_resized_kiNgg = resize_image(image_kiNgg)
    st.image(img_resized_kiNgg, caption="Presentación kiNgg")
    
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

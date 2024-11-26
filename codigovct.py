import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("valorant champions istanbul.csv")

# Rutas de imágenes
image_yay = "yay.jpeg"
image_Cryocells = "Cryocells.jpg"
image_ANGE1 = "ANGE1.jpg"
image_Derke = "Derke.jpg"
image_MaKo = "MaKo.jpg"
image_Scream = "Scream.jpg"
image_kiNgg = "kiNgg.jpg"
image_suygetsu = "suygetsu.jpg"
image_Less = "Less.jpeg"
image_LEV = "LEV.jpg"
image_DRX = "DRX.jpg"
image_XSET = "XSET.jpg"
image_FNC = "FNC.jpg"
image_FPX = "FPX.jpg"
image_OPTC = "OPTC.jpg"
image_TL = "TL.jpg"
image_LOUD = "LOUD.jpg"

# Funciones para mostrar las estadísticas
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

# Inicializar la página si no está definida
if "page" not in st.session_state:
    st.session_state.page = "home"

# Función para redimensionar imágenes
def resize_image(image_path, width=130, height=152):
    img = Image.open(image_path)
    img_resized = img.resize((width, height))
    return img_resized

# Función para mostrar imagen con su pie de foto
def display_image_with_caption(image_path, caption):
    img_resized = resize_image(image_path)
    st.image(img_resized)
    
    st.markdown(
        f"""
        <style>
        .caption {{
            font-family: 'Arial Black', sans-serif;
            font-size: 15px;
            font-weight: bold;
        }}
        </style>
        <p class="caption">{caption}</p>
        """, unsafe_allow_html=True
    )

# Función para mostrar los logos de los equipos
def imagenes_logos(image_path, width=200, height=200):
    try:
        img = Image.open(image_path)
        img_resized = img.resize((width, height))
        return img_resized
    except Exception as e:
        st.error(f"Error al cargar la imagen {image_path}: {e}")
        return None

# Función para mostrar la imagen con su nombre
def display_logo(image_path, name, width=100, height=100):
    img_resized = imagenes_logos(image_path, width, height)
    if img_resized:
        st.image(img_resized)
        st.caption(name)

# Función para mostrar los logos de los equipos con tamaño 300x300
def imagenes_logos_300(image_path, width=300, height=300):
    try:
        img = Image.open(image_path)
        img_resized = img.resize((width, height))  # Tamaño actualizado a 300x300
        return img_resized
    except Exception as e:
        st.error(f"Error al cargar la imagen {image_path}: {e}")
        return None

# Función para mostrar la imagen con su nombre con tamaño 300x300
def display_logo_300(image_path, name, width=300, height=300):  # Tamaño 300x300
    img_resized = imagenes_logos_300(image_path, width, height)
    if img_resized:
        st.image(img_resized)
        st.caption(name)

# Mostrar el contenido de la página principal
if st.session_state.page == "home":
    st.title("Análisis y Estadísticas del VCT Masters Reykjavik 2022: ¡Revive la Emoción del Torneo!")
    
    video_presentación_ = "https://www.youtube.com/watch?v=j2Z4qYJ3Jtc&ab_channel=VALORANTChampionsTour"
    st.video(video_presentación_)
    st.subheader("Presentación de los equipos participantes del torneo")

    # Mostrar logos de los equipos
    col1, col2, col3 = st.columns([1, 1, 1]) 
    with col2:
        display_logo_300(image_LOUD, "1 LOUD")

    col4, col5, col6 = st.columns([1, 1, 1])  
    with col4:
        display_logo_300(image_OPTC, "2 OPTC")
    with col6:
        display_logo_300(image_DRX, "3 DRX")

    col7, col8, col9, col10, col11 = st.columns([1, 1, 1, 1, 1])  
    with col7:
        display_logo(image_FPX, "4 FPX")
    with col8:
        display_logo(image_XSET, "5 XSET")
    with col9:
        display_logo(image_FNC, "6 FNC")
    with col10:
        display_logo(image_TL, "7 TeamLiquid")
    with col11:
        display_logo(image_LEV, "8 Leviatán")

    # Selección de datos adicionales
    page_selection = st.selectbox(
        "Datos que creemos te gustarán saber",
        ["Ház click para desplegar las opciones", 
         "Cuál fue el jugador con mejor rendimiento global del torneo", 
         "Cuál fue el jugador con peor rendimiento global del torneo", 
         "Cuál fue el jugador con más kills?", 
         "Cuáles fueron los jugadores con mejor rendimiento de cada equipo?"]
    )

    # Redirigir a las páginas correspondientes según la selección del `selectbox`
    if page_selection == "Cuál fue el jugador con mejor rendimiento global del torneo":
        st.session_state.page = "mejor_rendimiento"

    elif page_selection == "Cuál fue el jugador con peor rendimiento global del torneo":
        st.session_state.page = "peor_rendimiento"

    elif page_selection == "Cuál fue el jugador con más kills?":
        st.session_state.page = "mas_kills"

    elif page_selection == "Cuáles fueron los jugadores con mejor rendimiento de cada equipo?":
        st.session_state.page = "mejor_rendimiento_por_equipo"

# Mostrar el contenido correspondiente
if st.session_state.page == "mejor_rendimiento":
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
    display_image_with_caption(image_yay, "Presentación yay")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "mejor_rendimiento_por_equipo":
    st.title("Jugadores con el mejor rendimiento por equipo")
    mejor_rendimiento_por_equipo()
    
    # Primera fila de imágenes
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_image_with_caption(image_Less, "Less")
    with col2:
        display_image_with_caption(image_yay, "Yay")
    with col3:
        display_image_with_caption(image_MaKo, "MaKo")
    with col4:
        display_image_with_caption(image_suygetsu, "SUYGETSU")
    
    # Segunda fila de imágenes
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        display_image_with_caption(image_Cryocells, "Cryocells")
    with col6:
        display_image_with_caption(image_Scream, "Scream")
    with col7:
        display_image_with_caption(image_kiNgg, "kiNgg")
    with col8:
        display_image_with_caption(image_ANGE1, "ANGE1")

    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

a_columns, b_columns = st.columns(2)
if a_columns.button("K/D promedio por equipos"):
  fig = plt.figure(figsize=(10, 6))
  kd = df.groupby('Team')['K/D'].mean().sort_values(ascending=False)
  plt.bar(kd.index,kd.values,color="purple")
  plt.xlabel('Team')
  plt.ylabel('Promedio K/D')
  plt.title('K/D promedio por equipo')
  _ = plt.xticks(rotation="horizontal", ha='right')
  st.pyplot(fig)
  
if b_columns.button("Jugador con mas kills"):
  fig = plt.figure(figsize=(12, 6))
  kills = df.groupby('Player')['Kill'].mean().sort_values(ascending=False)
  plt.bar(kills.index, kills.values)
  plt.xlabel('Jugador')
  plt.ylabel('kills')
  plt.title('Jugador con mas kills')
  _ = plt.xticks(rotation=45, ha='right')
  st.pyplot(fig)

c_columns , d_columns , e_columns = st.columns(3)

if c_columns.button("Jugador con más muertes en el torneo"):
  fig = plt.figure(figsize=(15, 6))
  Muertes = df.groupby('Player')['Death'].mean().sort_values(ascending=False)
  plt.bar(Muertes.index, Muertes.values, color="Red")
  plt.xlabel('Jugador')
  plt.ylabel('Muertes')
  plt.title('Jugador con más muertes en el torneo')
  _ = plt.xticks(rotation=45,ha="center", )
  st.pyplot(fig)
if d_columns.button("Equipo con más victorias"):
  fig = plt.figure(figsize=(15, 6))
  Victorias = df.groupby('Team')['Rounds Win'].mean()
  plt.bar(Victorias.index, Victorias.values,color="green")
  plt.xlabel('Equipo')
  plt.ylabel('Victorias')
  plt.title('Equipo con mas victorias')
  _ = plt.xticks(rotation="horizontal",ha="center")
  st.pyplot(fig)
if e_columns.button("Equipo con mas derrotas del torneo"):
  fig = plt.figure(figsize=(15, 6))
  Derrotas = df.groupby('Team')['Rounds Lose'].mean()
  plt.bar(Derrotas.index, Derrotas.values,color="cyan")
  plt.xlabel('Equipo')
  plt.ylabel('Derrotas')
  plt.title('Equipo con mas derrotas del torneo')
  _ = plt.xticks(rotation="horizontal",ha="center")
  st.pyplot(fig)

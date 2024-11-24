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
    filas_seleccionadas = df.iloc[[5]]  # Puedes cambiar el índice según tu CSV
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

def LOUD_page():
    Loud_video = "https://www.youtube.com/watch?v=CSyGWW305M8&ab_channel=LOUDVALORANT"
    st.video(Loud_video)

def OPTC_page():
    OPTC_video = "https://www.youtube.com/watch?v=tCa7ky1qeXw&ab_channel=TeamReyna"
    st.video(OPTC_video)

def FPX_page():
    FPX_video = "https://www.youtube.com/watch?v=W0P7kGERa4o&ab_channel=TeamReyna"
    st.video(FPX_video)

def XSET_page():
    XSET_video = "https://www.youtube.com/watch?v=3jsUSJUhlHg&ab_channel=TeamReyna"
    st.video(XSET_video)

def FNC_page():
    FNC_video = "https://www.youtube.com/watch?v=Yr5X5CoEgKU&ab_channel=TeamReyna"
    st.video(FNC_video)

def TL_page():
    TL_video = "https://www.youtube.com/watch?v=_aJSUUvTDMY&ab_channel=TeamReyna"
    st.video(TL_video)

def LEV_page():
    EV_video = "https://www.youtube.com/watch?v=cYaAr1mr0gY&ab_channel=LEVIATANVALORANT"
    st.video(LEV_video)

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

# Mostrar el contenido de la página principal
if st.session_state.page == "home":
    st.title("Análisis y Estadísticas del VCT Masters Reykjavik 2022: ¡Revive la Emoción del Torneo!")
    
    video_presentación_ = "https://www.youtube.com/watch?v=j2Z4qYJ3Jtc&ab_channel=VALORANTChampionsTour"
    st.video(video_presentación_)

    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        st.subheader("Presentación de los equipos participantes del torneo")

    # Mostrar logos de los equipos
    col1, col2, col3 = st.columns([1, 1, 1]) 
    with col2:
        display_logo(image_LOUD, "1 LOUD")

    col4, col5, col6 = st.columns([1, 1, 1])  
    with col4:
        display_logo(image_OPTC, "2 OPTC")
    with col6:
        display_logo(image_DRX, "3 DRX")

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

    # Selección de página
    paginas_equipos = st.selectbox(
        "Deseas ver los mejores momentos de cada equipo?",
        ["Selecciona el equipo del cual te gustaría saber más", 
         "LOUD", 
         "OPTC", 
         "DRX", 
         "FPX",
         "XSET",
         "FNC",
         "TL",
         "LEV"]
    )

    # Selección de página
    page_selection = st.selectbox(
        "Datos que creemos te gustarán saber",
        ["Ház click para desplegar las opciones", 
         "Cuál fue el jugador con mejor rendimiento global del torneo", 
         "Cuál fue el jugador con peor rendimiento global del torneo", 
         "Cuál fue el jugador con más kills?", 
         "Cuáles fueron los jugadores con mejor rendimiento de cada equipo?"]
    )

    st.subheader("¡Descubre el Poder de los Equipos!")
    st.text("Este gráfico muestra cómo se desempeñan los equipos en cuanto a su ratio de Kills/Deaths (K/D). Los equipos con el mejor desempeño suelen tener una mayor proporción de muertes por baja, lo que refleja una ejecución más eficiente en el juego. ¡Ve quién lidera el torneo en rendimiento!")
    plt.figure(figsize=(10, 6))
    kd = df.groupby('Team')['K/D'].mean().sort_values(ascending=False)
    plt.bar(kd.index, kd.values, color="purple")
    plt.xlabel('Equipo')
    plt.ylabel('Promedio K/D')
    plt.title('K/D promedio por equipo')
    plt.xticks(rotation="horizontal", ha='right')
    st.pyplot()  

    st.subheader("¿Quién es el Rey de las Bajas?")
    st.text("Este gráfico destaca la acumulación de kills de cada jugador a lo largo del torneo. Si estás buscando al jugador con más acción en el campo de batalla, aquí puedes ver quién se lleva la corona de las eliminaciones. ¡El jugador más letal está aquí!")
    plt.figure(figsize=(15, 6))
    kills = df.groupby('Player')['Kill'].mean().sort_values(ascending=False)
    plt.bar(kills.index, kills.values)
    plt.xlabel('Jugador')
    plt.ylabel('Kills')
    plt.title('Jugador con más kills')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()  

    st.subheader("¡Las Muertes también Hablan!")
    st.text("A veces el precio del juego es alto, y este gráfico muestra la cantidad de muertes de cada jugador. Aunque no es lo más positivo, saber quién lidera en esta categoría puede dar pistas sobre el estilo de juego o los desafíos a los que se enfrentan los jugadores. ¡Entérate de quiénes son los más golpeados en el torneo!")
    plt.figure(figsize=(15, 6))
    deaths = df.groupby('Player')['Death'].mean().sort_values(ascending=False)
    plt.bar(deaths.index, deaths.values, color="red")
    plt.xlabel('Jugador')
    plt.ylabel('Muertes')
    plt.title('Jugador con más muertes')
    plt.xticks(rotation=45, ha='right')
    st.pyplot() 

    # Llamada a la página correspondiente
    if paginas_equipos != "Selecciona el equipo del cual te gustaría saber más":
        st.session_state.page = f"{paginas_equipos}_page"

# Páginas de equipos específicos
elif st.session_state.page == "LOUD_page":
    LOUD_page()
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "OPTC_page":
    OPTC_page()
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "FPX_page":
    FPX_page()
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "XSET_page":
    XSET_page()
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "FNC_page":
    FNC_page()
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "TL_page":
    TL_page()
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "LEV_page":
    LEV_page()
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"


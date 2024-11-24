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

def LOUD_page():
    Loud_video = "https://www.youtube.com/watch?v=CSyGWW305M8&ab_channel=LOUDVALORANT"
    st.video(Loud_video)

def OPTC_page():
    OPTC_video = "https://www.youtube.com/watch?v=tCa7ky1qeXw&ab_channel=TeamReyna"
    st.video(OPTC_video)
    st.text(""" 
        LOUD es una organización de deportes electrónicos con sede en Brasil, conocida por su enfoque en varios juegos, 
        pero especialmente por su éxito en Valorant. Fundada en 2018, LOUD rápidamente se posicionó como uno de los 
        equipos más importantes de América Latina, ganando relevancia tanto a nivel nacional como internacional. 
        La organización es famosa por su enfoque en la creación de contenido y la participación activa en las redes 
        sociales, lo que ha ayudado a construir una gran base de seguidores.
        En el VCT Masters Reykjavik 2022, LOUD se convirtió en uno de los equipos más sobresalientes en la historia 
        de los VCT (Valorant Champions Tour) al ganar el torneo. Este evento, que fue el primer Masters presencial 
        del circuito de Valorant, marcó un hito para los equipos de América Latina, ya que LOUD fue el primer equipo 
        de la región en ganar un evento internacional de Valorant.
        VCT Masters Reykjavik 2022 se celebró del 27 de abril al 24 de mayo de 2022 en Reikiavik, Islandia, y reunió 
        a los mejores equipos del mundo. LOUD no solo destacó por su talento, sino también por su impresionante 
        habilidad para adaptarse a los formatos internacionales y superar a equipos de regiones históricamente más 
        fuertes, como Europa y Norteamérica.
        Roster: LOUD llevó a su alineación estelar a Reykjavik, con jugadores como aspas, saadhak, pANcada, saadhak y Less. 
        Estos jugadores fueron fundamentales para el éxito del equipo, especialmente aspas, quien se destacó como una de 
        las estrellas más brillantes del torneo, destacando con su habilidad mecánica excepcional y su capacidad para 
        dominar el campo de juego.
        Campeones: LOUD hizo historia al vencer a KRÜ Esports en la final del torneo, lo que marcó el primer título 
        internacional para un equipo de América Latina en la historia de Valorant. El equipo brasileño demostró una 
        combinación de agresividad, control y estrategias innovadoras que los colocaron por encima de gigantes internacionales 
        como Sentinels y Team Liquid.
    """)

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
    LEV_video = "https://www.youtube.com/watch?v=cYaAr1mr0gY&ab_channel=LEVIATANVALORANT"
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

    # Selección de página de equipo
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

    # Llamada a la página correspondiente del equipo
    if paginas_equipos != "Selecciona el equipo del cual te gustaría saber más":
        st.session_state.page = f"{paginas_equipos}_page"

    if st.session_state.page == "LOUD_page":
        LOUD_page()
    elif st.session_state.page == "OPTC_page":
        OPTC_page()
    elif st.session_state.page == "DRX_page":
        # Aquí puedes agregar la función correspondiente de DRX
        pass
    elif st.session_state.page == "FPX_page":
        FPX_page()
    elif st.session_state.page == "XSET_page":
        XSET_page()
    elif st.session_state.page == "FNC_page":
        FNC_page()
    elif st.session_state.page == "TL_page":
        TL_page()
    elif st.session_state.page == "LEV_page":
        LEV_page()

    # Volver a la página principal
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

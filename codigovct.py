import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

# Cargar datos CSV
df = pd.read_csv("valorant champions istanbul.csv")

# Rutas de las imágenes
image_paths = {
    "yay": "yay.jpeg",
    "Cryocells": "Cryocells.jpg",
    "ANGE1": "ANGE1.jpg",
    "Derke": "Derke.jpg",
    "MaKo": "MaKo.jpg",
    "Scream": "Scream.jpg",
    "kiNgg": "kiNgg.jpg",
    "suygetsu": "suygetsu.jpg",
    "Less": "Less.jpeg",
    "LEV": "LEV.jpg",
    "DRX": "DRX.jpg",
    "XSET": "XSET.jpg",
    "FNC": "FNC.jpg",
    "FPX": "FPX.jpg",
    "OPTC": "OPTC.jpg",
    "TL": "TL.jpg",
    "LOUD": "LOUD.jpg"
}

# Funciones para mostrar datos específicos
def mejor_rendimiento():
    filas_seleccionadas = df.iloc[[5]]
    st.dataframe(filas_seleccionadas)
    st.image(image_paths["yay"], caption="yay - Jugador con mejor rendimiento")
    # Volver a la página principal
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

def peor_rendimiento():
    filas_seleccionadas = df.iloc[[19]]
    st.dataframe(filas_seleccionadas)
    st.image(image_paths["ANGE1"], caption="ANGE1 - Rendimiento más bajo")
    # Volver a la página principal
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

def mas_kills():
    filas_seleccionadas = df.iloc[[5]]
    st.dataframe(filas_seleccionadas)
    st.image(image_paths["yay"], caption="yay - Jugador con más bajas")
    # Volver a la página principal
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

def mejor_rendimiento_por_equipo():
    filas_seleccionadas = df.iloc[[3, 5, 10, 17, 22, 25, 32, 35]]
    st.dataframe(filas_seleccionadas)
    
    # Primera fila de imágenes
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        try:
            image1 = Image.open(image_paths["Less"])
            st.image(image1, caption="Less")
        except Exception as e:
            st.error(f"No se pudo cargar la imagen Less: {e}")
    
    with col2:
        try:
            image2 = Image.open(image_paths["ANGE1"])
            st.image(image2, caption="ANGE1")
        except Exception as e:
            st.error(f"No se pudo cargar la imagen ANGE1: {e}")
    
    with col3:
        try:
            image3 = Image.open(image_paths["MaKo"])
            st.image(image3, caption="MaKo")
        except Exception as e:
            st.error(f"No se pudo cargar la imagen MaKo: {e}")
    
    with col4:
        try:
            image4 = Image.open(image_paths["suygetsu"])
            st.image(image4, caption="suygetsu")
        except Exception as e:
            st.error(f"No se pudo cargar la imagen suygetsu: {e}")

    # Segunda fila de imágenes
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        try:
            image5 = Image.open(image_paths["Cryocells"])
            st.image(image5, caption="Cryocells")
        except Exception as e:
            st.error(f"No se pudo cargar la imagen Cryocells: {e}")
    
    with col6:
        try:
            image6 = Image.open(image_paths["Derke"])
            st.image(image6, caption="Derke")
        except Exception as e:
            st.error(f"No se pudo cargar la imagen Derke: {e}")
    
    with col7:
        try:
            image7 = Image.open(image_paths["Scream"])
            st.image(image7, caption="Scream")
        except Exception as e:
            st.error(f"No se pudo cargar la imagen Scream: {e}")
    
    with col8:
        try:
            image8 = Image.open(image_paths["kiNgg"])
            st.image(image8, caption="kiNgg")
        except Exception as e:
            st.error(f"No se pudo cargar la imagen kiNgg: {e}")

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
    st.title("Jugador con mejor rendimiento global")
    mejor_rendimiento()

# Página 2: Peor rendimiento
elif st.session_state.page == "peor_rendimiento":
    st.title("Jugador con peor rendimiento global")
    peor_rendimiento()

# Página 3: Jugador con más kills
elif st.session_state.page == "mas_kills":
    st.title("Jugador con más kills")
    mas_kills()

# Página 4: Mejor rendimiento por equipo
elif st.session_state.page == "mejor_rendimiento_por_equipo":
    st.title("Jugadores con mejor rendimiento por equipo")
    mejor_rendimiento_por_equipo()

# Después de las páginas de rendimiento, mostramos los gráficos
if st.session_state.page == "home":
    # Visualizaciones de gráficos
    st.subheader("¡Descubre el Poder de los Equipos!")
    st.text("Este gráfico muestra cómo se desempeñan los equipos en cuanto a su ratio de Kills/Deaths (K/D)...")
    plt.figure(figsize=(10, 6))
    kd = df.groupby('Team')['K/D'].mean().sort_values(ascending=False)
    plt.bar(kd.index, kd.values, color="purple")
    plt.xlabel('Equipo')
    plt.ylabel('Promedio K/D')
    plt.title('K/D promedio por equipo')
    plt.xticks(rotation="horizontal", ha='right')
    st.pyplot()

    st.subheader("¿Quién es el Rey de las Bajas?")
    st.text("Este gráfico destaca la acumulación de kills de cada jugador...")
    plt.figure(figsize=(15, 6))
    kills = df.groupby('Player')['Kill'].mean().sort_values(ascending=False)
    plt.bar(kills.index, kills.values)
    plt.xlabel('Jugador')
    plt.ylabel('Kills')
    plt.title('Jugador con más kills')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

    st.subheader("Equipos Triunfadores: ¿Quién Tiene la Mayor Cantidad de Victorias?")
    st.text("El éxito no solo se mide en kills, sino también en victorias. Este gráfico revela a los equipos que más veces han salido victoriosos durante el torneo...")
    plt.figure(figsize=(15, 6))
    victories = df.groupby('Team')['Rounds Win'].mean()
    plt.bar(victories.index, victories.values, color="green")
    plt.xlabel('Equipo')
    plt.ylabel('Victorias')
    plt.title('Equipo con más victorias')
    plt.xticks(rotation="horizontal", ha="center")
    st.pyplot()

    st.subheader("¿Quién Sufrió Más Derrotas?")
    st.text("Este gráfico muestra a los equipos con más derrotas, lo que podría reflejar puntos débiles...")
    plt.figure(figsize=(15, 6))
    defeats = df.groupby('Team')['Rounds Lose'].mean()
    plt.bar(defeats.index, defeats.values, color="cyan")
    plt.xlabel('Equipo')
    plt.ylabel('Derrotas')
    plt.title('Equipo con más derrotas')
    plt.xticks(rotation="horizontal", ha="center")
    st.pyplot()

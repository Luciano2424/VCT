import streamlit as st
import pandas as pd
from PIL import Image  
import matplotlib.pyplot as plt

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
    filas_seleccionadas = df.iloc[[3, 5, 10, 17, 22, 25, 32, 35]]  
    st.dataframe(filas_seleccionadas)

# Ensure "page" exists in session state
if "page" not in st.session_state:
    st.session_state.page = "home"

def resize_image(image_path, width=130, height=152):
    img = Image.open(image_path)  
    img_resized = img.resize((width, height))  
    return img_resized

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

if st.session_state.page == "home":  
    st.title("Datos que creemos te gustarán saber")
    
    # URL del video de YouTube
    video_presentación_ = "https://www.youtube.com/watch?v=j2Z4qYJ3Jtc&ab_channel=VALORANTChampionsTour"
    st.video(video_presentación_)

    col1, col2, col3 = st.columns([1, 3, 1])  

    with col2:
        st.subheader("Presentación de los equipos participantes del toreno")
        page_selection = st.selectbox(
            "Datos que creemos te gustarán saber",
            ["Ház click para desplegar las opciones", "Cuál fue el jugador con mejor rendimiento global del torneo", 
             "Cuál fue el jugador con peor rendimiento global del torneo", 
             "Cuál fue el jugador con más kills?", 
             "Cuáles fueron los jugadores con mejor rendimiento de cada equipo?"]
        )

        if page_selection == "Cuál fue el jugador con mejor rendimiento global del torneo":
            st.session_state.page = "mejor_rendimiento"
        elif page_selection == "Cuál fue el jugador con peor rendimiento global del torneo":
            st.session_state.page = "peor_rendimiento"
        elif page_selection == "Cuál fue el jugador con más kills?":
            st.session_state.page = "mas_kills"
        elif page_selection == "Cuáles fueron los jugadores con mejor rendimiento de cada equipo?":
            st.session_state.page = "mejor_rendimiento_por_equipo"

    st.subheader("Mejores momentos del torneo")

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

    # Gráfico de kills
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
    display_image_with_caption(image_yay, "Presentación yay")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "mejor_rendimiento_por_equipo":
    st.title("Jugadores con el mejor rendimiento por equipo")
    mejor_rendimiento_por_equipo()

    col1, col2, col3, col4 = st.columns(4)  
    with col1:
        display_image_with_caption(image_Less, "Less Top 1")
    with col2:
        display_image_with_caption(image_yay, "yay Top 2")
    with col3:
        display_image_with_caption(image_MaKo, "MaKo Top 3")
    with col4:
        display_image_with_caption(image_suygetsu, "suygetsu Top 4")

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        display_image_with_caption(image_Cryocells, "Cryocells Top 5")
    with col6:
        display_image_with_caption(image_Derke, "Derke Top 6")
    with col7:
        display_image_with_caption(image_Scream, "Scream Top 7")
    with col8:
        display_image_with_caption(image_kiNgg, "kiNgg Top 8")

    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

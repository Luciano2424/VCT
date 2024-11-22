import streamlit as st
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("valorant champions istanbul.csv")

st.title("Buscador de Datos de Jugadores")

keyword = st.text_input("Ingrese la palabra clave:", "")

def mostrar_lineas_excel():
    # Obtener el índice de la fila inicial (comienza desde 0 para la primera fila)
    indice_fila_inicial = 0  # Puedes cambiar esto para seleccionar una fila inicial diferente
    
    # Obtener los datos de dos filas
    # Usando iloc para seleccionar filas por índice
    filas_seleccionadas = df.iloc[1 : 7 + 2] 

    # Mostrar las filas seleccionadas como un DataFrame en Streamlit
    st.dataframe(filas_seleccionadas)

if st.button("Jugador con mejor rendimiento global del torneo"):
    mostrar_lineas_excel()
    
# Mapeo de palabras clave
keywords_mapping = {
    "jugador": "player",
    "equipo": "team",
    "nacionalidad": "nationality",
    "asesinatos": "kill",
    "muertes": "death",
    "K/D": "rendimiento",
    "KAST": "Impacto por ronda",
    "Prize": "ganancias",
    "Role": "rol",
    "HS %": "porcentaje de headshots",
    "Rounds Played": "rondas jugadas",
    "Rounds Win": "rondas ganadas",
    "Rounds Lose": "rondas perdidas",
    "Rank": "posición por equipos"
}

if keyword in keywords_mapping:
    column_name = keywords_mapping[keyword]  # Línea correctamente indentada

    if column_name in df.columns:  # También indentado
        st.write(f"Resultados para: {keyword}")
        st.dataframe(df[column_name])
    else:
        st.write("No se encontró la columna correspondiente.")
else:
    st.write("La palabra clave no es válida.")


import streamlit as st
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("valorant champions istanbul.csv")

st.title("Buscador de Datos de Jugadores")

keyword = st.text_input("Ingrese la palabra clave:", "")

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
    column_name = keywords_mapping[keyword]
    
    # Verificar si la columna existe en el DataFrame
    if column_name in df.columns:
        # Filtrar los datos
        filtered_data = df[df[column_name].astype(str).str.contains(keyword, case=False, na=False)]
        if not filtered_data.empty:
            st.write("Resultados encontrados:")
            st.dataframe(filtered_data)
        else:
            st.write("No se encontraron resultados.")
    else:
        st.write(f"Error: La columna '{column_name}' no existe en los datos.")
else:
    st.write("La palabra clave no es válida.")

import ipywidgets as widgets
from IPython.display import display
import re
import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv("valorant champions istanbul.csv")

# Define keyword-column associations
keyword_associations = {
    "jugador": "player",
    "equipo": "team",
    "nacionalidad": "nationality",
    "asesinatos": "kill",  # Asumiendo que "kill" es la columna para asesinatos
    "muertes": "death",   # Asumiendo que "death" es la columna para muertes
    # Agrega más asociaciones aquí...
}

def advanced_search(change):
    text = change['new']

    # Extract keywords and search term
    keywords_found = []
    for keyword, column in keyword_associations.items():
        if keyword in text.lower():
            keywords_found.append((keyword, column))
            text = text.replace(keyword, "", 1)  # Remove keyword from text

    search_term = text.strip()

    # Autocomplete based on search term and associated columns
    options = []
    if search_term:
        for keyword, column in keywords_found:
            for val in df[column].astype(str).unique():
                if search_term.lower() in val.lower():
                    options.append(val)

    search_widget.options = sorted(list(set(options)))

# Create search widget
search_widget = widgets.Text(
    placeholder='Escribe tu búsqueda...',
    description='Buscar:'
)
search_widget.observe(advanced_search, names='value')
display(search_widget)

# Display the selected keyword and search term (for demonstration)
output_widget = widgets.Output()
display(output_widget)

def on_search_widget_change(change):
    with output_widget:
        output_widget.clear_output()
        text = change['new']
        keyword_match = re.search("|".join(keywords), text, re.IGNORECASE)
        keyword = keyword_match.group(0) if keyword_match else None
        search_term = text.replace(keyword, "").strip() if keyword else text
        print(f"Palabra clave: {keyword}")
        print(f"Término de búsqueda: {search_term}")

search_widget.observe(on_search_widget_change, names='value')

import pandas as pd
import streamlit as st

# cargar los datos
df = pd.read_csv("valorant champions istanbul.csv")

# diccionario de asociaciones de palabras clave con las columnas
keyword_associations = {
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

# interfaz de Streamlit
st.title("Buscador de Datos de Valorant")

# entrada de búsqueda
search_term = st.text_input("Introduce una palabra clave para buscar:")

# si el usuario introduce una palabra clave
if search_term:
    # convertir a minúsculas para hacer la búsqueda insensible a mayúsculas
    search_term = search_term.lower()

    # filtrar las columnas que contienen la palabra clave en los nombres de las columnas
    filtered_columns = [column for keyword, column in keyword_associations.items() if keyword.lower() in search_term]

    if filtered_columns:
        # filtrar el DataFrame por las columnas encontradas
        filtered_df = df[filtered_columns]
        st.write(f"Mostrando resultados para las columnas relacionadas con '{search_term}':")
        st.dataframe(filtered_df)
    else:
        st.write("No se encontraron coincidencias con la palabra clave.")
else:
    st.write("Introduce una palabra clave para buscar.")
    st.write(df)

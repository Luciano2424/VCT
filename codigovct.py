
Para modificar tu aplicación de Streamlit de manera que, al buscar una palabra clave, muestre únicamente la columna correspondiente con los datos asociados, puedes ajustar el código de la siguiente manera:
Código actualizado en Python:
python
import streamlit as st
import pandas as pd
Cargar el DataFrame desde el archivo CSV
df = pd.read_csv("valorant champions istanbul.csv")
Título de la aplicación
st.title("Buscador de Datos de Jugadores")
Entrada de texto para buscar palabras clave
keyword = st.text_input("Ingrese la palabra clave:", "")
Mapa de palabras clave a nombres de columnas
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
# Obtener los datos de la columna correspondiente
if column_name in df.columns:
st.write(f"Resultados para: {keyword}")
st.dataframe(df[column_name])
else:
st.write("No se encontró la columna correspondiente.")
else:
st.write("La palabra clave no es válida.")
Cambios realizados:
Al encontrar una coincidencia con la palabra clave, el código ahora extrae y muestra únicamente la columna correspondiente del DataFrame.Se añade un encabezado para los resultados que muestra la palabra clave para mayor claridad.
Instrucciones:
Asegúrate de que el archivo "valorant champions istanbul.csv" esté en el mismo directorio que el script.Mantén las bibliotecas streamlit y pandas instaladas.Guarda el código en tu archivo app.py.Ejecuta la aplicación de Streamlit desde la terminal:
bash
streamlit run app.py
Opciones para seguir adelante:
Modificar el código para presentar múltiples columnas relacionadasAgregar validaciones adicionales para mejorar la experiencia del usuarioExplorar cómo permitir la búsqueda en múltiples columnas
Si necesitas más ajustes o tienes preguntas adicionales, no dudes en decírmelo. ¡Estoy aquí para ayudar!

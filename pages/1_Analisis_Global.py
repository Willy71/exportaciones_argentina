import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Exportaciones Argentina",
    page_icon="🇦🇷",
    layout="wide"
)

# Check if you've already initialized the data
if 'df' not in st.session_state:
    # Get the data if you haven't
    df = pd.read_csv('datasets/exportaciones_anual_porcentaje.csv')
    # Save the data to session state
    st.session_state.df = df

# Retrieve the data from session state
df = st.session_state.df

def centrar_imagen(imagen, ancho):
    # Aplicar estilo CSS para centrar la imagen con Markdown
    st.markdown(
        f'<div style="display: flex; justify-content: center;">'
        f'<img src="{imagen}" width="{ancho}">'
        f'</div>',
        unsafe_allow_html=True
    )


def centrar_texto(texto, tamanho, color):
    st.markdown(f"<h{tamanho} style='text-align: center; color: {color}'>{texto}</h{tamanho}>",
                unsafe_allow_html=True)

centrar_texto("Participación de las exportaciones año 2023 ",2, "white")

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = df["Pais"]
sizes = df["Año 2023"]
colors = [ 'limegreen', 'yellow','dodgerblue', 'red', 'cyan', 'blueviolet', 'orange', 'magenta']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, shadow={'ox': -0.02, 'edgecolor': 'none', 'shade': 0.9}, colors=colors, autopct='%1.1f%%', startangle=15)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

centrar_texto("Indudablemente nuestro principal socio comercial es Brasil, por cercania lo cual significa menor costo de transporte y porque la produccion principal en el vecino pais es la soja, dejando el trigo para importacion desde nuestro pais, por ser este producto de mejor calidad en nuestras tierras.", 5, "white")


import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Exportaciones Argentina",
    page_icon="🇦🇷",
    layout="wide"
)

#df_data = pd.read_csv("datasets\exportaciones_anual_transpose.csv", index_col=0)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/vB6zKN5n/Bandera-Argentina.png");
background-size: 180%;
background-position: top left;
background-repeat: repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

[data-testid="stSidebar"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


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
    
st.write("#")

centrar_texto("Argentina", 1, "black")
centrar_texto("Exportaciones por país y región", 3, "black")
centrar_texto("Exportaciones FOB. En millones de dólares.", 3, "black")
st.title("")
centrar_texto("Periodo de los datos 1989-2022", 5, "black")
centrar_texto("Información Económica al Día - Sector Externo", 5, "black")
centrar_texto("Licencia - Creative Commons Attribution 4.0", 5, "black")
centrar_texto("Frecuencia - Mensual y Anual", 5, "black")
centrar_texto("Mantenedor - Subsecretaría de Programación Macroeconómica.", 5, "black")
centrar_texto("Fuente primaria - Instituto Nacional de Estadística y Censos (INDEC)", 5, "black")
centrar_texto("https://datos.gob.ar/dataset/sspm-exportaciones-fob-por-pais-region", 5, "black")
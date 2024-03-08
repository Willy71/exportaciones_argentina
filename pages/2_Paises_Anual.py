import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Exportaciones Argentina",
    page_icon="🇦🇷",
    layout="wide"
)

# Check if you've already initialized the data
#if 'df' not in st.session_state:
    # Get the data if you haven't
df1 = pd.read_csv('datasets/exportaciones_anual_Pais.csv')
    # Save the data to session state
#    st.session_state.df = df

# Retrieve the data from session state
#df = st.session_state.df

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/2j4YrXkk/Background-Argentina-3.png");
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

# Filtros por país
countries = st.sidebar.multiselect(
    "Seleccione uno o dos países para comparar:  ",
    options=df1['Pais'].unique(),
    default=[]
)

if len(countries) > 2:
    st.error("Por favor, seleccione como máximo dos países para comparar.")
else:
    # Aplicar filtro
    df_selection = df1[df1["Pais"].isin(countries)]

    # Hacer melt de los datos
    df_melted = pd.melt(df_selection, id_vars=["Pais"], var_name="Año", value_name="Valor")

    # Crear el gráfico
    fig = px.bar(df_melted, 
                 x="Año", 
                 y="Valor", 
                 color="Pais", 
                 title=f"Comparación de Exportaciones Anuales",
                 labels={"Valor": "Valor de Exportación", "Año": "Año"},
                 barmode='group')  # Agrupa las barras una al lado de la otra

    # Ordenar el eje x por año
    fig.update_xaxes(type='category')

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True, theme=None)

    # Mostrar el DataFrame filtrado
    st.dataframe(df_selection, hide_index=True)

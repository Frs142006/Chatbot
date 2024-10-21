import streamlit as st

def configurar_pagina():
# Agregamos un título principal a nuestra página
    st.title("Mi chat de IA")
    st.sidebar.title("Configuración de la IA") # Creamos un sidebar con un título.
    elegirModelo = st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)
    return elegirModelo
    modelo = configurar_pagina()

MODELOS = ['modelo1', 'modelo2', 'modelo3']

st.set_page_config(page_title="Mi chat de IA", page_icon="6️⃣", layout="centered")


st.title("Mi primera aplicación con Streamlit")

nombre = st.text_input("¿Cuál es tu nombre?")

modelo = configurar_pagina()
mensaje = st.chat_input("Escribí tu mensaje:")
if st.button("Saludar"):
    st.write(f"¡Hola, {nombre}! gracias por venir a Talento Tech")
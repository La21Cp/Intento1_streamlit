import streamlit as st

# Título de la app
st.title("🎈 Mi Primera App en Streamlit")

# Entrada de usuario
name = st.text_input("¿Cuál es tu nombre?")

# Botón para generar respuesta
if st.button("Saludar"):
    if name:
        st.success(f"¡Hola, {name}! Bienvenido a tu primera app en Streamlit 🚀")
    else:
        st.warning("Por favor, ingresa tu nombre.")

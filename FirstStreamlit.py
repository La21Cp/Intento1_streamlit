import streamlit as st
import PyPDF2

# 📂 Ruta del PDF dentro del proyecto (debe estar en la misma carpeta o indicar el path correcto)
PDF_PATH = "documentos/mi_archivo.pdf"  # Asegúrate de cambiarlo si está en otra carpeta

st.title("📄 Visor de PDF en Streamlit")

# 📖 Abrir el PDF desde la carpeta del proyecto
try:
    with open(PDF_PATH, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Extraer texto de todas las páginas
        pdf_text = ""
        for page in pdf_reader.pages:
            pdf_text += page.extract_text() + "\n"

    # 📜 Mostrar contenido en Streamlit
    st.subheader("Contenido del PDF:")
    st.text_area("Texto extraído:", pdf_text, height=300)

except FileNotFoundError:
    st.error(f"❌ No se encontró el archivo: {PDF_PATH}. Verifica que está en la carpeta correcta.")
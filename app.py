import os
import base64
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="E-Books Pobreza Energética",
    page_icon="📚",
    layout="wide"
)

# Estructura de los libros
LIBROS = {
    "Living with Energy Poverty (2024)": {
        "directorio": "Living_with_Energy_Poverty_2024_Routledge",
        "capitulos": 22,
        "indice": "indice.pdf"
    },
    "Pobreza Energética: Visiones de América Latina (2022)": {
        "directorio": "Pobreza_Energetica_Visiones_America_Latina_2022_COLEF",
        "capitulos": 10,
        "indice": "indice.pdf"
    }
}

# Función para mostrar PDF
def mostrar_pdf(ruta_pdf):
    with open(ruta_pdf, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_iframe = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_iframe, unsafe_allow_html=True)

# Interfaz principal
st.title("📖 Plataforma de E-Books sobre Pobreza Energética")

# Sidebar para selección de libro
selected_book = st.sidebar.selectbox("Selecciona un libro", list(LIBROS.keys()))

# Obtener información del libro seleccionado
book_info = LIBROS[selected_book]
base_path = os.path.join("libros", book_info["directorio"])

# Generar lista de capítulos
capitulos = [str(i) for i in range(1, book_info["capitulos"] + 1)]
selected_chapter = st.sidebar.selectbox("Selecciona un capítulo", capitulos)

# Botones de acción
col1, col2, col3, col4 = st.columns(4)
with col1:
    btn_indice = st.button("📑 Ver Índice General")
with col2:
    btn_capitulo = st.button("📄 Leer Capítulo Completo")
with col3:
    btn_resumen = st.button("📝 Ver Resumen Textual")
with col4:
    btn_audio = st.button("🔊 Escuchar Resumen")

# Manejo de las acciones
if btn_indice:
    st.header(f"Índice - {selected_book}")
    indice_path = os.path.join(base_path, book_info["indice"])
    mostrar_pdf(indice_path)

if btn_capitulo:
    st.header(f"Capítulo {selected_chapter} - {selected_book}")
    capitulo_path = os.path.join(base_path, "capitulos", f"{selected_chapter}.pdf")
    mostrar_pdf(capitulo_path)

if btn_resumen:
    st.header(f"Resumen Capítulo {selected_chapter}")
    resumen_path = os.path.join(base_path, "resumenes", f"{selected_chapter}.docx")
    
    with open(resumen_path, "rb") as file:
        st.download_button(
            label="Descargar Resumen en Word",
            data=file,
            file_name=f"Resumen_Cap_{selected_chapter}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

if btn_audio:
    st.header(f"Resumen Auditivo Capítulo {selected_chapter}")
    audio_path = os.path.join(base_path, "audios", f"{selected_chapter}.mp3")
    st.audio(audio_path, format='audio/mp3')

# Información adicional
st.sidebar.markdown("""
**Instrucciones de uso:**
1. Selecciona un libro del menú desplegable
2. Elige el número de capítulo que deseas explorar
3. Utiliza los botones superiores para acceder a:
   - Índice completo del libro
   - Contenido completo del capítulo
   - Resumen en formato Word
   - Versión auditiva del resumen

**Datos técnicos:**
- Libro 1: 22 capítulos (2024)
- Libro 2: 10 capítulos (2022)
""")

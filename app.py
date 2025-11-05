import streamlit as st
import hashlib, time, json

# Función para crear un hash del texto
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

st.set_page_config(page_title="Acta Digital", layout="centered")

st.title("Acta Digital")
st.write("Demostración: la tecnología no es neutral.")

with st.form("form_acta"):
    titulo = st.text_input("Título del acta")
    contenido = st.text_area("Contenido del acta")
    autor = st.text_input("Autor")

    enviado = st.form_submit_button("Guardar acta")

    if enviado:
        # Crear un texto base para el hash
        texto_completo = titulo + contenido + autor + str(time.time())
        acta_hash = get_hash(texto_completo)

        st.success("Acta guardada correctamente (ejemplo).")
        st.write("**Título:**", titulo)
        st.write("**Autor:**", autor)
        st.write("**Contenido:**")
        st.write(contenido)
        st.write("**Hash del acta:**", acta_hash)


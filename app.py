import streamlit as st

st.set_page_config(page_title="Acta Digital", layout="centered")

st.title("Acta Digital")
st.write("Demostración: la tecnología no es neutral.")

with st.form("form_acta"):
    titulo = st.text_input("Título del acta")
    contenido = st.text_area("Contenido del acta")
    autor = st.text_input("Autor")

    enviado = st.form_submit_button("Guardar acta")

    if enviado:
        st.success("Acta guardada correctamente (ejemplo).")
        st.write("**Título:**", titulo)
        st.write("**Autor:**", autor)
        st.write("**Contenido:**")
        st.write(contenido)

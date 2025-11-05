import streamlit as st
import hashlib, time, json, os

# --- Función de hash ---
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# --- Configuración de la página ---
st.set_page_config(page_title="Acta Digital", layout="centered")

st.title("📜 Registro de Documentos Digitales")
st.write("Esta aplicación registra documentos con un identificador único (hash) que demuestra su autenticidad.")

# --- Entradas del usuario ---
owner = st.text_input("👤 Propietario del documento")
content = st.text_area("📝 Contenido del documento")

# --- Al presionar el botón Registrar ---
if st.button("Registrar documento"):
    if not owner or not content:
        st.warning("Por favor completa todos los campos antes de registrar.")
    else:
        record = {
            "owner": owner,
            "hash": get_hash(content),
            "time": time.ctime()
        }

        # Crear archivo si no existe
        if not os.path.exists("blockchain.json"):
            with open("blockchain.json", "w") as f:
                f.write("")

        # Guardar el registro
        with open("blockchain.json", "a") as f:
            f.write(json.dumps(record) + "\n")

        st.success("✅ Documento registrado con éxito")
        st.write("**Hash del documento:**", record["hash"])
        st.write("**Fecha y hora:**", record["time"])

# --- Mostrar historial de registros ---
st.subheader("📂 Historial de documentos registrados")
if os.path.exists("blockchain.json") and os.path.getsize("blockchain.json") > 0:
    with open("blockchain.json", "r") as f:
        for line in f:
            data = json.loads(line)
            st.markdown(f"**Propietario:** {data['owner']}")
            st.markdown(f"**Hash:** `{data['hash']}`")
            st.markdown(f"**Registrado el:** {data['time']}")
            st.markdown("---")
else:
    st.info("Aún no hay documentos registrados.")



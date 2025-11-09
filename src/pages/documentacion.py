import streamlit as st
from pathlib import Path

def mostrar_documentacion():
    st.subheader("📘 Documentación del proyecto")

    # Ruta al proyecto raíz y al archivo de documentación
    ruta_md = Path(__file__).resolve().parents[2] / "docs" / "documentacion_tienda_aurelion.md"
    ruta_flujo = Path(__file__).resolve().parents[2] / "assets" / "flujograma_aurelion.jpg"

    if ruta_md.exists():
        contenido_md = ruta_md.read_text(encoding="utf-8")

        # --- Contexto y objetivo ---
        st.markdown("### Contexto y objetivo")
        with st.expander("Ver detalles"):
            inicio = contenido_md.find("### Tema")
            fin = contenido_md.find("### Fuente")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # --- Datasets de referencia ---
        st.markdown("### Datasets de referencia")
        with st.expander("Ver detalles"):
            inicio = contenido_md.find("### Fuente")
            fin = contenido_md.find("### Información")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # --- Metodología ---
        st.markdown("### Metodología e implementación")
        with st.expander("Ver detalles"):
            inicio = contenido_md.find("### Información")
            fin = contenido_md.find("### Pseudocódigo")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # --- Pseudocódigo ---
        st.markdown("### Pseudocódigo")
        with st.expander("Ver detalles"):
            inicio = contenido_md.find("### Pseudocódigo") + len("### Pseudocódigo")
            fin = contenido_md.find("### Diagrama del flujo")
            st.markdown(contenido_md[inicio:fin], unsafe_allow_html=True)

        # --- Diagrama del flujo ---
        st.markdown("### Diagrama del flujo")
        with st.expander("Ver detalles"):
            if ruta_flujo.exists():
                col1, col2, col3 = st.columns([1, 2, 1])  # columnas para centrar la imagen
                with col2:
                    st.image(str(ruta_flujo), width=600)
            else:
                st.warning("No se encontró la imagen del diagrama de flujo.")
    else:
        st.warning("El archivo de documentación no se encontró.")

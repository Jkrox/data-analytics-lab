import streamlit as st

def page_config():
    st.set_page_config(
        page_title="Home",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(
        """
<style> 

[data-testid="stAppViewBlockContainer"] {
    width: 100%;
    padding: 2rem 2rem 1rem 4rem;
    min-width: auto;
    max-width: initial;
}
footer {visibility: hidden;} 
        
</style>
""",
        unsafe_allow_html=True,
    )

def main():
    st.title("Bienvenido a la Aplicación de Análisis de Datos")
    st.header("Introducción")
    st.write("""
    Esta aplicación está diseñada para ayudarte a analizar y visualizar datos de manera interactiva.
    Puedes cargar tus propios conjuntos de datos, realizar análisis exploratorios y generar visualizaciones
    para obtener insights valiosos.
    """)

    st.subheader("Características")
    st.write("""
    - Carga de datos desde archivos CSV
    - Análisis exploratorio de datos
    - Visualización interactiva de datos
    - Generación de informes
    """)

    st.subheader("Cómo empezar")
    st.write("""
    Para comenzar, simplemente navega a las diferentes secciones usando la barra lateral.
    Si tienes alguna pregunta o necesitas ayuda, consulta la documentación o contacta con el soporte técnico.
    """)

if __name__ == "__main__":
    page_config()
    main()
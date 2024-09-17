# Guía para arrancar el aplicativo de Streamlit

Esta guía te ayudará a configurar un entorno virtual de Python y a iniciar la aplicación de Streamlit desde el archivo `Home.py`.

## Requisitos previos

- Python instalado en tu sistema.
- pip (gestor de paquetes de Python) instalado.

## Pasos para configurar el entorno y arrancar Streamlit

1. **Clonar el repositorio (si es necesario):**
    ```bash
    git clone https://github.com/tu-usuario/data-analytics-lab.git
    cd data-analytics-lab
    ```

2. **Crear un entorno virtual:**
    ```bash
    python -m venv venv
    ```

3. **Activar el entorno virtual:**

    - En Windows:
      ```bash
      .\venv\Scripts\activate
      ```

    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Arrancar la aplicación de Streamlit:**
    ```bash
    streamlit run Home.py
    ```

## Notas adicionales

- Asegúrate de que el archivo `requirements.txt` contenga todas las dependencias necesarias para tu proyecto.
- Para desactivar el entorno virtual, simplemente ejecuta `deactivate`.

¡Listo! Ahora deberías poder ver tu aplicación de Streamlit en tu navegador web.

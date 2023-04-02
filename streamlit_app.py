import os
import streamlit as st
import openai
import chardet  # Importa el paquete chardet

# 3. Configurar la API de OpenAI utilizando su clave API:
openai.api_key = "your_openai_api_key"

# 4. Crear una función para evaluar el ensayo utilizando GPT:
def evaluar_ensayo(texto_ensayo):
    prompt = f"Por favor, evalúa el siguiente ensayo:\n\n{texto_ensayo}\n\nCalificación:"
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    calificacion = response.choices[0].text.strip()
    return calificacion

# 5. Utilizar Streamlit para crear la interfaz de usuario:
st.title("Evaluador de Ensayos")
archivo_subido = st.file_uploader("Sube tu ensayo", type=["txt", "docx", "pdf"])

# ...

if archivo_subido is not None:
    # Detectar la codificación del archivo subido
    deteccion = chardet.detect(archivo_subido.read())
    codificacion = deteccion['encoding'] or 'utf-8'  # Usar 'utf-8' como codificación predeterminada
    archivo_subido.seek(0)  # Reinicia la posición del archivo a 0 para volver a leerlo
    
    # Leer el contenido del archivo y convertirlo en texto utilizando la codificación detectada
    texto_ensayo = archivo_subido.read().decode(codificacion)

    # ...

    # Leer el contenido del archivo y convertirlo en texto utilizando la codificación detectada
    texto_ensayo = archivo_subido.read().decode(codificacion)

    # Mostrar el ensayo cargado
    st.write("Contenido del ensayo:")
    st.write(texto_ensayo)

    # Evaluar el ensayo utilizando GPT
    if st.button("Evaluar Ensayo"):
        calificacion = evaluar_ensayo(texto_ensayo)
        st.write("Calificación:", calificacion)

        # Crear un archivo de texto con la evaluación y permitir su descarga
        with open("ensayo_evaluado.txt", "w") as f:
            f.write(f"Ensayo:\n\n{texto_ensayo}\n\nCalificación: {calificacion}")

        st.download_button(
            label="Descargar Ensayo Evaluado",
            data=open("ensayo_evaluado.txt", "rb"),
            file_name="ensayo_evaluado.txt",
            mime="text/plain",
        )

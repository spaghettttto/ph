import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5
)

temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):
    
    # Regla 1: pH fuera del rango [6.0, 7.0]
    if pH < 6.0 or pH > 7.0:
        resultado = "Revisar pH"
    # Regla 2: pH correcto, pero temperatura fuera del rango [20.0, 25.0]
    elif temperatura < 20.0 or temperatura > 25.0:
        resultado = "Revisar temperatura"
    # Regla 3: Ambos parámetros son correctos
    else:
        resultado = "Lote aceptable"

    st.write(f"Resultado: {resultado}")

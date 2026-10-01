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

concentracion = st.number_input(
    "Concentración (%)",
    value=10.0
)

if st.button("Evaluar"):

    if pH < 6.0 or pH > 7.0:
        resultado = "Revisar pH"
    elif temperatura < 20.0 or temperatura > 25.0:
        resultado = "Revisar temperatura"
    elif concentracion < 8.0 or concentracion > 12.0:
        resultado = "Revisar concentración"
    else:
        resultado = "Lote aceptable"

    st.write(f"Resultado: {resultado}")

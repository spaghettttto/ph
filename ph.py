import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5)

temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):

    # Completa aquí la lógica

    st.write(f"Resultado: {resultado}") 

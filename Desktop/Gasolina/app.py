import streamlit as st
from calculo import calcular_litros

# Título de la aplicación
st.title("Calculadora de Litros en Gasolinera")

# Valores fijos
largo_auto = 4.0  # Largo promedio de un auto en metros
litros_por_auto = 50.0  # Litros que carga cada auto

# Entradas del usuario
st.header("Ingresa los datos requeridos")
litros_gasolinera = st.number_input("Cantidad de litros disponibles en la gasolinera (litros):", min_value=0.0, value=1000.0)
distancia = st.number_input("Distancia a la gasolinera (metros):", min_value=0.0, value=100.0)

# Calcular autos y litros
if st.button("Calcular"):
    numero_autos, litros_cargados, litros_disponibles = calcular_litros(distancia, largo_auto, litros_por_auto, litros_gasolinera)
    
    # Mostrar los resultados
    st.header("Resultados")
    st.write(f"**Número de autos en la fila:** {int(numero_autos)} autos")
    st.write(f"**Total de litros cargados antes de tu turno:** {litros_cargados:.2f} litros")
    st.write(f"**Litros disponibles en la gasolinera:** {litros_disponibles:.2f} litros")
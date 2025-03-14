# Función para calcular la cantidad de autos y litros cargados
def calcular_litros(distancia, largo_auto, litros_por_auto, litros_gasolinera):
    # Calcular número de autos en la fila
    numero_autos = distancia / largo_auto
    
    # Calcular los litros cargados por esos autos
    litros_cargados = numero_autos * litros_por_auto
    
    # Calcular los litros disponibles en la gasolinera después de que se cargan los autos
    litros_disponibles = litros_gasolinera - litros_cargados
    return numero_autos, litros_cargados, litros_disponibles


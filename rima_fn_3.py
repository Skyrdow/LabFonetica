import random
import rima_data
from rima_data import Bloque_rima

PROBABILIDAD_MISMA_RIMA = 6

rimada = rima_data

"""Necesito ciertas restricciones que no sé implementar:
    En el nivel básico, las dos palabras tienen que ser de la misma categoría "a", "g" o "e"
    En el nivel medio las dos palabras pueden ser 
        a) de la misma categoría
        b) g + a
    En el nivel avanzado
        a) misma categoría
        b) g + a
        c) e + g
"""

def eleccionNivel():
    nivel = int(input("Escriba el número 1 (básico), 2 (medio), 3 (avanzado) correspondiente a su nivel: "))

    if nivel == 1:
        ene_veces = random.randint(3, 6)
        # palabras de la misma categoría: a-g-e

    elif nivel == 2:
        ene_veces = random.randint(5, 9)
        # palabras de la misma categoría o g + a

    elif nivel == 3:
        ene_veces = random.randint(7, 12)
        # palabras de la misma categoría, / a + g / g + e

    else:
        print("Elija opciones entre 1 y 3, con números")

    return nivel, ene_veces


def seleccion_palabras(nivel):
    """ Selecciona y analiza las palabras
        Entrega las variables que se pueden analizar
        para determinar si hay rima o no
     """

    ## Selecciona dos bloques de la lista
    palabra_1 = Bloque_rima(random.choice(rimada.lista))
    palabra_2 = Bloque_rima(random.choice(rimada.lista))

    # RESTRICCIONES NIVEL 1: palabras de la misma categoría: a-g-e
    if nivel == 1:
        while not (palabra_1.categoria == palabra_2.categoria and
                palabra_1.palabra != palabra_2.palabra and 
                (palabra_1.rima != palabra_2.rima or 1 != random.randint(1, PROBABILIDAD_MISMA_RIMA))):
            palabra_1 = Bloque_rima(random.choice(rimada.lista))
            palabra_2 = Bloque_rima(random.choice(rimada.lista))
        return palabra_1, palabra_2        

    # RESTRICCIONES NIVEL 2: palabras de la misma categoría o g + a
    if nivel == 2:
        while not ((palabra_1.categoria == palabra_2.categoria or 
                compararCategorias(palabra_1, palabra_2, "a", "g"))
                and palabra_1.palabra != palabra_2.palabra and 
                (palabra_1.rima != palabra_2.rima or 1 != random.randint(1, PROBABILIDAD_MISMA_RIMA))):
            palabra_1 = Bloque_rima(random.choice(rimada.lista))
            palabra_2 = Bloque_rima(random.choice(rimada.lista))
        return palabra_1, palabra_2
    # RESTRICCIONES NIVEL 3: palabras de la misma categoría, / a + g / g + e
    if nivel == 3:
        while not ((palabra_1.categoria == palabra_2.categoria
                or compararCategorias(palabra_1, palabra_2, "a", "g") 
                or compararCategorias(palabra_1, palabra_2, "e", "g"))
                and palabra_1.palabra != palabra_2.palabra and 
                (palabra_1.rima != palabra_2.rima or 1 != random.randint(1, PROBABILIDAD_MISMA_RIMA))):
            palabra_1 = Bloque_rima(random.choice(rimada.lista))
            palabra_2 = Bloque_rima(random.choice(rimada.lista))
        return palabra_1, palabra_2

# Compara ambas categorias, para ambos lados
def compararCategorias(palabra1, palabra2, cat1, cat2):
    if (palabra1.categoria == cat2) and (palabra2.categoria == cat1):
        return True
    if (palabra1.categoria == cat1) and (palabra2.categoria == cat2):
        return True
    return False

### 1 = no hay rima
### 2 = hay rima consonante
### 3 = hay rima asonante
def identificador_de_rima(palabra_1, palabra_2):
    if (compararCategorias(palabra_1, palabra_2, "a", "e")):
        return 1

    if (compararCategorias(palabra_1, palabra_2, "a", "g")):
        return 1

    if palabra_1.primera_letra_rima != palabra_2.primera_letra_rima:
        return 1

    if (palabra_1.primera_letra_rima == palabra_2.primera_letra_rima): 
        if (palabra_1.rima == palabra_2.rima):
            return 2

        # Rima 1 y 2 no coinciden
        if (palabra_1.rima != palabra_2.rima):

            # Se identifican las dos ultimas vocales
            if (compararCategorias(palabra_1, palabra_2, "e", "e")):
                if (obtener_ultima_vocal(palabra_1) == obtener_ultima_vocal(palabra_2)):
                    return 3
                else:
                    return 1

            if (compararCategorias(palabra_1, palabra_2, "e", "g")):
                if (obtener_ultima_vocal(palabra_1) == obtener_ultima_vocal(palabra_2)):
                    return 3
                else:
                    return 1
    # Valor 4 = algo malo ocurrió
    return 4

def revisar_base_datos_nr():
    print("## Se omiten los resultados de \"no hay rima\" ##")
    for bloq_rima_1 in rima_data.lista:
        rima_1 = Bloque_rima(bloq_rima_1)
        for bloq_rima_2 in rima_data.lista:
            rima_2 = Bloque_rima(bloq_rima_2)
            respuesta = identificador_de_rima(rima_1, rima_2)
            if respuesta == 1:
                continue
            if respuesta == 2:
                opcion = "rima consonante"
            if respuesta == 3:
                opcion = "rima asonante"
            if respuesta == 4:
                opcion = "error logica"
            print(rima_1.palabra, rima_2.palabra, "|||", end=" ")
            print(opcion)
            
def revisar_base_datos():
    for bloq_rima_1 in rima_data.lista:
        rima_1 = Bloque_rima(bloq_rima_1)
        for bloq_rima_2 in rima_data.lista:
            rima_2 = Bloque_rima(bloq_rima_2)
            respuesta = identificador_de_rima(rima_1, rima_2)
            if respuesta == 1:
                opcion = "no hay rima"
            if respuesta == 2:
                opcion = "rima consonante"
            if respuesta == 3:
                opcion = "rima asonante"
            if respuesta == 4:
                opcion = "error logica"
            print(rima_1.palabra, rima_2.palabra, "|||", end=" ")
            print(opcion)

def debug_base_datos():
    for bloq_rima_1 in rima_data.lista:
        rima_1 = Bloque_rima(bloq_rima_1)
        for bloq_rima_2 in rima_data.lista:
            rima_2 = Bloque_rima(bloq_rima_2)
            respuesta = identificador_de_rima(rima_1, rima_2)
            if respuesta == 4:
                print(rima_1.palabra, rima_2.palabra, "|||", end=" ")
                print("datos: ", rima_1, "///", rima_2)

def obtener_ultima_vocal(palabra):
    if palabra.rima[-1] in ('a', 'e', 'i', 'o', 'u'):
        return palabra.rima[-1]
    # Asumiendo que no existen palabras con dos consonantes al final
    if len(palabra.rima) > 1:
        return palabra.rima[-2]
    return "ERROR"
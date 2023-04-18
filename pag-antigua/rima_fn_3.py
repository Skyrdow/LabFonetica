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
            if (compararCategorias(palabra_1, palabra_2, "a", "a")):
                return 3

            rima_simpl_1 = simpl_diptongos(palabra_1)
            rima_simpl_2 = simpl_diptongos(palabra_2)
            # Se identifican las dos ultimas vocales
            if (compararCategorias(palabra_1, palabra_2, "e", "e")):
                vocales_1 = obtener_ultimas_2_vocales(rima_simpl_1)
                vocales_2 = obtener_ultimas_2_vocales(rima_simpl_2)
                if (vocales_1[0] == "" or vocales_2[0] == "" or 
                    vocales_1[1] == "" or vocales_2[1] == ""):
                    return 1

                if (vocales_1[0] == vocales_2[0] and vocales_1[1] == vocales_2[1]):
                    return 3
                else:
                    return 1

            if (compararCategorias(palabra_1, palabra_2, "e", "g") or compararCategorias(palabra_1, palabra_2, "g", "g")):
                if (obtener_ultima_vocal(rima_simpl_1) == obtener_ultima_vocal(rima_simpl_2)):
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

def obtener_ultima_vocal(string):
    if string[-1] in ('a', 'e', 'i', 'o', 'u'):
        return string[-1]
    # Asumiendo que no existen palabras con dos consonantes al final
    if len(string) > 1:
        return string[-2]
    return "ERROR"

def obtener_ultimas_2_vocales(string):
    vocal_1 = ""
    vocal_2 = ""
    # "ABC" -> "CBA"
    reversed_string = string[::-1]
    primero_encontrado = False
    for char in reversed_string:
        if char in ('a', 'e', 'i', 'o', 'u'):
            if (not primero_encontrado):
                vocal_1 = char
                primero_encontrado = True
            else:
                vocal_2 = char
                return [vocal_1, vocal_2]


def simpl_diptongos(palabra):
    resto_rima = palabra.resto_rima
    for elem in ("ai", "au","ua","ia","ei","eu","ue","ie","oi","ou","io","uo","iu","iu","ui"):
        for elem2 in ("a","a","a","a","e","e","e","e","o","o","o","o","i","u","u"):
            resto_rima = resto_rima.replace(elem, elem2)
            break
    return resto_rima

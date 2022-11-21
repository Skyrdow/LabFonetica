import random
import rima_data
from rima_data import Bloque_rima

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
        while not (palabra_1.categoria == palabra_2.categoria and palabra_1.palabra != palabra_2.palabra):
            palabra_1 = Bloque_rima(random.choice(rimada.lista))
            palabra_2 = Bloque_rima(random.choice(rimada.lista))
        return palabra_1, palabra_2        

    # RESTRICCIONES NIVEL 2: palabras de la misma categoría o g + a
    if nivel == 2:
        while not (palabra_1.categoria == palabra_2.categoria or 
                (palabra_1.categoria == "a" and palabra_2.categoria == "g") 
                or (palabra_1.categoria == "g" and palabra_2.categoria == "a")
                and palabra_1.palabra != palabra_2.palabra):
            palabra_1 = Bloque_rima(random.choice(rimada.lista))
            palabra_2 = Bloque_rima(random.choice(rimada.lista))
        return palabra_1, palabra_2
    # RESTRICCIONES NIVEL 3: palabras de la misma categoría, / a + g / g + e
    if nivel == 3:
        while not (palabra_1.categoria == palabra_2.categoria or 
                (palabra_1.categoria == "a" and palabra_2.categoria == "g") 
                or (palabra_1.categoria == "g" and palabra_2.categoria == "a")
                or (palabra_1.categoria == "g" and palabra_2.categoria == "e") 
                or (palabra_1.categoria == "g" and palabra_2.categoria == "e")
                and palabra_1.palabra != palabra_2.palabra):
            palabra_1 = Bloque_rima(random.choice(rimada.lista))
            palabra_2 = Bloque_rima(random.choice(rimada.lista))
        return palabra_1, palabra_2


def identificador_de_rima(palabra_1, palabra_2):
    # Condición de no rima

    ultimo_elemento_p_1 = palabra_1.resto_rima[-1]
    ultimo_elemento_p_2 = palabra_2.resto_rima[-1]
    if len(palabra_1.resto_rima) > 1:
        penultimo_elemento_p1 = palabra_1.resto_rima[-2]
    if len(palabra_2.resto_rima) > 1:    # NECESARIO PARA QUE NO EXPLOTE
        penultimo_elemento_p2 = palabra_2.resto_rima[-2]

    if palabra_1.primera_letra_rima != palabra_2.primera_letra_rima:
        return 1
        ### 1 = no hay rima
        ### 2 = hay rima consonante
        ### 3 = hay rima asonante
    # Condición consonante
    elif (palabra_1.primera_letra_rima == palabra_2.primera_letra_rima) and (palabra_1.rima == palabra_2.rima):
        return 2

    # Mútiples casos de rima asonante
    # 1. A-A si las palabras son agudas, se establece la condición para la rima asonante
    # es igual la vocal tónica. Si es diferente el resto, es asonante.
    elif (palabra_1.categoria == "a" and palabra_2.categoria == "a") and (
            palabra_1.resto_rima != palabra_2.resto_rima):
        return 3

    # 2. G-G si las palabras son grave
    elif palabra_1.categoria == "g" and palabra_2.categoria == "g":
        # Sustituciones en primera palabra
        rima_sustitucion_1 = palabra_1.resto_rima.replace("ai", "a")
        rima_sustitucion_1 = rima_sustitucion_1.replace("au", "a")
        rima_sustitucion_1 = rima_sustitucion_1.replace("ua", "a")
        rima_sustitucion_1 = rima_sustitucion_1.replace("ia", "a")
        rima_sustitucion_1 = rima_sustitucion_1.replace("ei", "e")
        rima_sustitucion_1 = rima_sustitucion_1.replace("eu", "e")
        rima_sustitucion_1 = rima_sustitucion_1.replace("ue", "e")
        rima_sustitucion_1 = rima_sustitucion_1.replace("ie", "e")
        rima_sustitucion_1 = rima_sustitucion_1.replace("oi", "o")
        rima_sustitucion_1 = rima_sustitucion_1.replace("ou", "o")
        rima_sustitucion_1 = rima_sustitucion_1.replace("io", "o")
        rima_sustitucion_1 = rima_sustitucion_1.replace("uo", "o")
        rima_sustitucion_1 = rima_sustitucion_1.replace("iu", "i")
        rima_sustitucion_1 = rima_sustitucion_1.replace("iu", "u")
        rima_sustitucion_1 = rima_sustitucion_1.replace("ui", "u")
        # sustituciones en segunda palabra
        rima_sustitucion_2 = palabra_2.resto_rima.replace("ai", "a")
        rima_sustitucion_2 = rima_sustitucion_2.replace("au", "a")
        rima_sustitucion_2 = rima_sustitucion_2.replace("ua", "a")
        rima_sustitucion_2 = rima_sustitucion_2.replace("ia", "a")
        rima_sustitucion_2 = rima_sustitucion_2.replace("ei", "e")
        rima_sustitucion_2 = rima_sustitucion_2.replace("eu", "e")
        rima_sustitucion_2 = rima_sustitucion_2.replace("ue", "e")
        rima_sustitucion_2 = rima_sustitucion_2.replace("ie", "e")
        rima_sustitucion_2 = rima_sustitucion_2.replace("oi", "o")
        rima_sustitucion_2 = rima_sustitucion_2.replace("ou", "o")
        rima_sustitucion_2 = rima_sustitucion_2.replace("io", "o")
        rima_sustitucion_2 = rima_sustitucion_2.replace("uo", "o")
        rima_sustitucion_2 = rima_sustitucion_2.replace("iu", "i")
        rima_sustitucion_2 = rima_sustitucion_2.replace("iu", "u")
        rima_sustitucion_2 = rima_sustitucion_2.replace("ui", "u")

        # resultado mie > me; cai > ca; riel > rel

        vocal_a_1 = rima_sustitucion_1.count("a")
        vocal_e_1 = rima_sustitucion_1.count("e")
        vocal_i_1 = rima_sustitucion_1.count("i")
        vocal_o_1 = rima_sustitucion_1.count("o")
        vocal_u_1 = rima_sustitucion_1.count("u")

        vocal_a_2 = rima_sustitucion_2.count("a")
        vocal_e_2 = rima_sustitucion_2.count("e")
        vocal_i_2 = rima_sustitucion_2.count("i")
        vocal_o_2 = rima_sustitucion_2.count("o")
        vocal_u_2 = rima_sustitucion_2.count("u")

        # NO CAMBIAR POR vocal_a_1 == vocal_a_2
        # CUANDO SEAN 0 == 0 DA VERDADERO
        if vocal_a_1 == 1 and vocal_a_2 == 1:
            return 3
        elif vocal_e_1 == 1 and vocal_e_2 == 1:
            return 3
        elif vocal_i_1 == 1 and vocal_i_2 == 1:
            return 3
        elif vocal_o_1 == 1 and vocal_o_2 == 1:
            return 3
        elif vocal_u_1 == 1 and vocal_u_2 == 1:
            return 3
        else:   # AL LLEGAR A ESTE ELSE TERMINA TODA LA EJECUCION, NO DEBERIA SER PROBLEMA PORQUE CAMBIA DE CATEGORIA
            return 1


    elif (palabra_1.categoria == "e" and palabra_2.categoria == "e" and
            (palabra_1.resto_rima[-1]) == (palabra_2.resto_rima[-1])):
        return 2

    elif (palabra_1.categoria == "e" and palabra_2.categoria == "e" and 
            (palabra_1.resto_rima[-1]) != (palabra_2.resto_rima[-1])):
        return 1

    ### AGUDA + GRAVE. Basta con saber si son iguales en el resto

    elif (palabra_1.categoria == "a" and palabra_2.categoria == "g" and 
            palabra_1.resto_rima != palabra_2.resto_rima):
        return 3

    ### GRAVE + AGUDA

    elif palabra_1.categoria == "g" and palabra_2.categoria == "a":
        # ) and (palabra_1.resto_rima != palabra_2.resto_rima):
        return 3
    # c asa - dem ás   asa as Si la primera es igual, es asonante
    #####################################
    ### GRAVE + ESDRÚJULA
    #####################################

    elif palabra_1.categoria == "g" and palabra_2.categoria == "e":
        # La palabra 1
        if ultimo_elemento_p_1 in ("a", "e", "i", "o", "u"):
            caracter_fin_p_1 = "vocal"
        else:
            caracter_fin_p_1 = "conso"

        if ultimo_elemento_p_2 in ("a", "e", "i", "o", "u"):
            caracter_fin_p_2 = "vocal"
        else:
            caracter_fin_p_1 = "conso"

        if caracter_fin_p_1 == "vocal" and caracter_fin_p_2 == "vocal":
            if ultimo_elemento_p_1 == ultimo_elemento_p_2:
                return 3
            else:
                return 1

        if caracter_fin_p_1 == "vocal" and caracter_fin_p_2 == "conso":
            if ultimo_elemento_p_1 == penultimo_elemento_p2:
                return 3
            else:
                return 1
        if caracter_fin_p_1 == "conso" and caracter_fin_p_2 == "vocal":
            if penultimo_elemento_p1 == ultimo_elemento_p_2:
                return 3
            else:
                return 1



    ### ESDRÚJULA + GRAVE

    # brújula - bruja   > uxula uxa sí tiene asonante

    elif palabra_1.categoria == "e" and palabra_2.categoria == "g":

        ###  NO SE TOMA EN CUENTA QUE SI ULTIMO_ELEMENTO ES CONSONANTE VOCAL_FINAL NUNCA TIENE VALOR
        ### PREGUNTAR AL PROFE 
        # La palabra 1
        if ultimo_elemento_p_1 == "a":
            vocal_final_1 = "a"
        if ultimo_elemento_p_1 == "e":
          vocal_final_1 = "e"
        if ultimo_elemento_p_1 == "i":
          vocal_final_1 = "i"
        if ultimo_elemento_p_1 == "o":
          vocal_final_1 = "o"
        if ultimo_elemento_p_2 == "u":
          vocal_final_1 = "u"
        else:
             # NO SE USA NADA DE ESTO
            if penultimo_elemento_p1 == "a":
                vocal_penultima_1 = "a"
            if penultimo_elemento_p1 == "e":
                vocal_penultima1 = "e"
            if penultimo_elemento_p1 == "i":
                vocal_penultima1 = "i"
            if penultimo_elemento_p1 == "o":
                vocal_penultima_1 = "o"
            if penultimo_elemento_p1 == "u":
                vocal_penultima_1 = "u"

        # La palabra 2
        if ultimo_elemento_p_2 == "a":
            vocal_final_2 = "a"
        if ultimo_elemento_p_2 == "e":
            vocal_final_2 = "e"
        if ultimo_elemento_p_2 == "i":
            vocal_final_2 = "i"
        if ultimo_elemento_p_2 == "o":
            vocal_final_2 = "o"
        if ultimo_elemento_p_2 == "u":
            vocal_final_2 = "u"
        else:
            if penultimo_elemento_p2 == "a":
                vocal_penultima_2 = "a"
            if penultimo_elemento_p2 == "e":
                vocal_penultima_2 = "e"
            if penultimo_elemento_p2 == "i":
                vocal_penultima_2 = "i"
            if penultimo_elemento_p2 == "o":
                vocal_penultima_2 = "o"
            if penultimo_elemento_p2 == "u":
                vocal_penultima_2 = "u"
            else:
                problema = 1

        if vocal_final_1 == vocal_final_2:
            return 3

# RESPUESTA LARGA
def revisar_base_datos():
    for bloq_rima_1 in rima_data.lista:
        rima_1 = Bloque_rima(bloq_rima_1)
        for bloq_rima_2 in rima_data.lista:
            rima_2 = Bloque_rima(bloq_rima_2)
            print(rima_1.palabra, rima_2.palabra, "|||", end=" ")
            respuesta = identificador_de_rima(rima_1, rima_2)
            if respuesta == 1:
                opcion = "no hay rima entre ellas"
            if respuesta == 2:
                opcion = "rima consonante"
            if respuesta == 3:
                opcion = "rima asonante"
            print(opcion)
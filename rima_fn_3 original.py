import random
from subprocess import call
import rima_data

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


def seleccion_palabras(nivel, ene_veces):
    """ Selecciona y analiza las palabras
        Entrega las variables que se pueden analizar
        para determinar si hay rima o no
     """

    if nivel == 1:

        for palabra in range(1, (ene_veces)):
            ## Selecciona dos bloques de la lista
            bloque_palabra_1 = random.choice(rimada.lista)
            bloque_palabra_2 = random.choice(rimada.lista)

            ## selecciona el primer elemento del bloque (la palabra misma), la categoría y la rima
            ## Luego selecciona los mismos elementos del segundo bloque
            palabra_1 = (bloque_palabra_1[0])
            categoria_acentual_palabra_1 = (bloque_palabra_1[1])
            rima_palabra_1 = (bloque_palabra_1[2])
            primer_elemento_de_la_rima_1 = rima_palabra_1[0]
            resto_palabra_1 = rima_palabra_1[1:]
            
            palabra_2 = (bloque_palabra_2[0])
            categoria_acentual_palabra_2 = (bloque_palabra_2[1])
            rima_palabra_2 = (bloque_palabra_2[2])
            primer_elemento_de_la_rima_2 = rima_palabra_2[0]
            resto_palabra_2 = rima_palabra_2[1:]

            #if (categoria_acentual_palabra_1 == "a" and categoria_acentual_palabra_2 == "a") and (rima_palabra_1 == rima_palabra_2):

            ##    bloque_palabra_2 = random.choice(rimada.lista)
            #    categoria_acentual_palabra_2 = (bloque_palabra_2[1])
            #    if categoria_acentual_palabra_2 == "a":
            #        palabra_2 = (bloque_palabra_2[0])
            #        rima_palabra_2 = (bloque_palabra_2[2])
            #        primer_elemento_de_la_rima_2 = rima_palabra_2[0]
            #        resto_palabra_2 = rima_palabra_2[1:]
            #    else:
             #       print("hasta aquí llego yo")

    return palabra_1, palabra_2, categoria_acentual_palabra_1, categoria_acentual_palabra_2, rima_palabra_1, \
           rima_palabra_2, primer_elemento_de_la_rima_1, primer_elemento_de_la_rima_2, resto_palabra_1, resto_palabra_2


def identificador_de_rima(rima_palabra_1, rima_palabra_2,
                          categoria_acentual_palabra_1, categoria_acentual_palabra_2,
                          primer_elemento_de_la_rima_1, primer_elemento_de_la_rima_2,
                          resto_palabra_1, resto_palabra_2):
    # Condición de no rima
    if primer_elemento_de_la_rima_1 != primer_elemento_de_la_rima_2:
        respuesta_int = 1
        ### 1 = no hay rima
        ### 2 = hay rima consonante
        ### 3 = hay rima asonante
    # Condición consonante
    elif (primer_elemento_de_la_rima_1 == primer_elemento_de_la_rima_2) and (rima_palabra_1 == rima_palabra_2):
        respuesta_int = 2

    # Mútiples casos de rima asonante
    # 1. A-A si las palabras son agudas, se establece la condición para la rima asonante
    # es igual la vocal tónica. Si es diferente el resto, es asonante.
    elif (categoria_acentual_palabra_1 == "a" and categoria_acentual_palabra_2 == "a") and (
            resto_palabra_1 != resto_palabra_2):
        respuesta_int = 3

    # 2. G-G si las palabras son grave
    elif categoria_acentual_palabra_1 == "g" and categoria_acentual_palabra_2 == "g":
        # Sustituciones en primera palabra
        rim_1_0 = resto_palabra_1.replace("ai", "a")
        rim_1a = rim_1_0.replace("au", "a")
        rim_1b = rim_1a.replace("ua", "a")
        rim_1c = rim_1b.replace("ia", "a")
        rim_1d = rim_1c.replace("ei", "e")
        rim_1e = rim_1d.replace("eu", "e")
        rim_1f = rim_1e.replace("ue", "e")
        rim_1g = rim_1f.replace("ie", "e")
        rim_1h = rim_1g.replace("oi", "o")
        rim_1i = rim_1h.replace("ou", "o")
        rim_1j = rim_1i.replace("io", "o")
        rim_1k = rim_1j.replace("uo", "o")
        rim_1l = rim_1k.replace("Iu", "i")
        rim_1m = rim_1l.replace("iU", "u")
        rim_1n = rim_1m.replace("iU", "u")
        rim_1 = rim_1n.replace("Ui", "u")
        # sustituciones en segunda palabra
        rim_2_0 = resto_palabra_2.replace("ai", "a")
        rim_2a = rim_2_0.replace("au", "a")
        rim_2b = rim_2a.replace("ua", "a")
        rim_2c = rim_2b.replace("ia", "a")
        rim_2d = rim_2c.replace("ei", "e")
        rim_2e = rim_2d.replace("eu", "e")
        rim_2f = rim_2e.replace("ue", "e")
        rim_2g = rim_2f.replace("ie", "e")
        rim_2h = rim_2g.replace("oi", "o")
        rim_2i = rim_2h.replace("ou", "o")
        rim_2j = rim_2i.replace("io", "o")
        rim_2k = rim_2j.replace("uo", "o")
        rim_2l = rim_2k.replace("Iu", "i")
        rim_2m = rim_2l.replace("iU", "u")
        rim_2n = rim_2m.replace("iU", "u")
        rim_2 = rim_2n.replace("Ui", "u")

        # resultado mie > me; cai > ca; riel > rel

        vocal_a_1 = rim_1.count("a")
        vocal_e_1 = rim_1.count("e")
        vocal_i_1 = rim_1.count("i")
        vocal_o_1 = rim_1.count("o")
        vocal_u_1 = rim_1.count("u")

        vocal_a_2 = rim_2.count("a")
        vocal_e_2 = rim_2.count("e")
        vocal_i_2 = rim_2.count("i")
        vocal_o_2 = rim_2.count("o")
        vocal_u_2 = rim_2.count("u")

        if vocal_a_1 == 1 and vocal_a_2 == 1:
            respuesta_int = 3
        elif vocal_e_1 == 1 and vocal_e_2 == 1:
            respuesta_int = 3
        elif vocal_i_1 == 1 and vocal_i_2 == 1:
            respuesta_int = 3
        elif vocal_o_1 == 1 and vocal_o_2 == 1:
            respuesta_int = 3
        elif vocal_u_1 == 1 and vocal_u_2 == 1:
            respuesta_int = 3
        else:
            respuesta_int = 1


    elif (categoria_acentual_palabra_1 == "e" and categoria_acentual_palabra_2 == "e" and (resto_palabra_1[-1]) == (
    resto_palabra_2[-1])):
        respuesta_int = 2

    elif (categoria_acentual_palabra_1 == "e" and categoria_acentual_palabra_2 == "e" and (resto_palabra_1[-1]) != (
    resto_palabra_2[-1])):
        respuesta_int = 1

    ### AGUDA + GRAVE. Basta con saber si son iguales en el resto

    elif (categoria_acentual_palabra_1 == "a" and categoria_acentual_palabra_2 == "g") and (
            resto_palabra_1 != resto_palabra_2):
        respuesta_int = 3

    ### GRAVE + AGUDA

    elif categoria_acentual_palabra_1 == "g" and categoria_acentual_palabra_2 == "a":
        # ) and (resto_palabra_1 != resto_palabra_2):
        respuesta_int = 3
    # c asa - dem ás   asa as Si la primera es igual, es asonante
    #####################################
    ### GRAVE + ESDRÚJULA
    #####################################

    elif categoria_acentual_palabra_1 == "g" and categoria_acentual_palabra_2 == "e":
        ultimo_elemento_p_1 = resto_palabra_1[-1]
        ultimo_elemento_p_2 = resto_palabra_2[-1]
        penultimo_elemento_p1 = resto_palabra_1[-2]
        penultimo_elemento_p2 = resto_palabra_2[-2]
        # La palabra 1
        if ultimo_elemento_p_1 == "a" or ultimo_elemento_p_1 == "e" or ultimo_elemento_p_1 == "i" or ultimo_elemento_p_1 == "o" or ultimo_elemento_p_1 == "u":
            caracter_fin_p_1 = "vocal"
        else:
            caracter_fin_p_1 = "conso"

        if ultimo_elemento_p_2 == "a" or ultimo_elemento_p_2 == "e" or ultimo_elemento_p_2 == "i" or ultimo_elemento_p_2 == "o" or ultimo_elemento_p_2 == "u":
            caracter_fin_p_2 = "vocal"
        else:
            caracter_fin_p_1 = "conso"

        if caracter_fin_p_1 == "vocal" and caracter_fin_p_2 == "vocal":
            if ultimo_elemento_p_1 == ultimo_elemento_p_2:
                respuesta_int = 3
            else:
                respuesta_int = 1

        if caracter_fin_p_1 == "vocal" and caracter_fin_p_2 == "conso":
            if ultimo_elemento_p_1 == penultimo_elemento_p2:
                respuesta_int = 3
            else:
                respuesta_int = 1
        if caracter_fin_p_1 == "conso" and caracter_fin_p_2 == "vocal":
            if penultimo_elemento_p1 == ultimo_elemento_p_2:
                respuesta_int = 3
            else:
                respuesta_int = 1



    ### ESDRÚJULA + GRAVE

    # brújula - bruja   > uxula uxa sí tiene asonante

    elif categoria_acentual_palabra_1 == "e" and categoria_acentual_palabra_2 == "g":

        # La palabra 1
        if ultimo_elemento_p_1 == "a":
            vocal_final_1 = "a"
        elif ultimo_elemento_p_1 == "e":
            vocal_final_1 = "e"
        elif ultimo_elemento_p_1 == "i":
            vocal_final_1 = "i"
        elif ultimo_elemento_p_1 == "o":
            vocal_final_1 = "o"
        elif ultimo_elemento_p_2 == "u":
            vocal_final_1 = "u"
        else:
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
        elif ultimo_elemento_p_2 == "e":
            vocal_final_2 = "e"
        elif ultimo_elemento_p_2 == "i":
            vocal_final_2 = "i"
        elif ultimo_elemento_p_2 == "o":
            vocal_final_2 = "o"
        elif ultimo_elemento_p_2 == "u":
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
            respuesta_int = 3

    return respuesta_int

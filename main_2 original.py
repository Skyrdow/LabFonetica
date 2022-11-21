import random
from subprocess import call
import rima_fn_3
rim = rima_fn_3

def main():
    nivel, ene_veces = rim.eleccionNivel()
    print("Su nivel es...")
    print(nivel)

    for i in range(1, ene_veces):
        palabra_1, palabra_2, categoria_acentual_palabra_1, categoria_acentual_palabra_2, \
        rima_palabra_1, rima_palabra_2, primer_elemento_de_la_rima_1, primer_elemento_de_la_rima_2, \
        resto_palabra_1, resto_palabra_2 = rim.seleccion_palabras(nivel, ene_veces)
        respuesta_int = rim.identificador_de_rima(rima_palabra_1, rima_palabra_2, categoria_acentual_palabra_1,
                                                  categoria_acentual_palabra_2, primer_elemento_de_la_rima_1,
                                                  primer_elemento_de_la_rima_2, resto_palabra_1, resto_palabra_2)

        print("Se le presentarán", ene_veces-1, "veces  2 palabras")
        print("En cada ocasión, responda:")
        print("Escriba '1' si no hay rima entre ellas")
        print("Escriba '2' si tienen rima consonante")
        print("Escriba '3' si presentan rima asonante")
        print(palabra_1, "---", palabra_2)
        respuesta_usuario = int(input("Escriba el número que Ud. cree que es el correcto:   "))
#        print(respuesta_usuario)
        medidor_respuesta = respuesta_int - respuesta_usuario
#        print(medidor_respuesta)
        if medidor_respuesta == 0:
            print("Su respuesta es correcta")
        else:
            print("Te equivocas...")

main()

# Lista de palabras:
# ("palabra", "g", "abra")
# palabra / categoría: grave, aguda o esdrújula / contenido fonológico de la rima
# el primer elemento de la rima se escribe sin acento pues es tónico por defecto

lista = (("casa", "g", "asa"), ("mesa", "g", "esa"), ("canción", "a", "on"), ("lector", "a", "or"),
         ("pasa", "g", "asa"), ("lámpara", "e", "ampara"), ("trágico", "e", "axiko"),
         ("queso", "g", "eso"), ("beso", "g", "eso"), ("pesa", "g", "esa"),
         ("fiesta", "g", "esta"), ("mesa", "g", "esa"), ("finca", "g", "inka"),
         ("prístino", "e", "istino"), ("fin", "a", "in"), ("lindo", "g", "indo"),
         ("horno", "g", "orno"), ("bochorno", "g", "orno"), ("lóbrego", "e", "obrego"),
         ("mosco", "g", "osko"), ("fútbol", "g", "utbol"), ("buque", "g", "uke"),
         ("luma", "g", "uma"), ("bruma", "g", "uma"), ("puma", "g", "uma"),
         ("camélido", "e", "elido"), ("fétido", "e", "etido"), ("lúcido", "e", "usido"),
         ("bote", "g", "ote"), ("pote", "g", "ote"), ("cantar", "a", "ar"), ("espuma", "g", "uma"))


def separador_base_rima(lista):
    lista_a = []
    lista_e = []
    lista_i = []
    lista_o = []
    lista_u = []

    for i in lista:
        base_rima = i[2]
        vocal_tonica = base_rima[0]

        if vocal_tonica == "a":
            print(base_rima)
            lista_a.append(i)
        if vocal_tonica == "e":
            print(base_rima)
            lista_e.append(i)
        if vocal_tonica == "i":
            print(base_rima)
            lista_i.append(i)
        if vocal_tonica == "o":
            print(base_rima)
            lista_o.append(i)
        if vocal_tonica == "u":
            print(base_rima)
            lista_u.append(i)

    return lista_a, lista_e, lista_i, lista_o, lista_u


def crea_listas_AGE(lista):
    lista_ag = []
    lista_gr = []
    lista_es = []

    for i in lista:
        categoria = i[1]
        if categoria == "a":
            lista_ag.append(i)
        if categoria == "e":
            lista_es.append(i)
        if categoria == "g":
            lista_gr.append(i)

    return lista_ag, lista_gr, lista_es

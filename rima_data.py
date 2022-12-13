# Lista de palabras:
# ("palabra", "g", "abra")
# palabra / categoría: grave, aguda o esdrújula / contenido fonológico de la rima
# el primer elemento de la rima se escribe sin acento pues es tónico por defecto

class Bloque_rima:
    palabra = ""
    categoria = ""
    rima = ""
    primera_letra_rima = ""
    resto_rima = ""
    
    def __init__(self, bloque_palabra):
        self.palabra = bloque_palabra[0]
        self.categoria = bloque_palabra[1]
        self.rima = bloque_palabra[2]
        self.primera_letra_rima = bloque_palabra[2][0]
        self.resto_rima = bloque_palabra[2][1:]
        
    def __str__(self):
        return self.palabra + " " + self.categoria + " " + self.rima + " " + self.primera_letra_rima + " " + self.resto_rima


lista = (("casa", "g", "asa"), ("mesa", "g", "esa"), ("canción", "a", "on"), ("lector", "a", "or"),
         ("pasa", "g", "asa"), ("lámpara", "e", "ampara"), ("trágico", "e", "axiko"),
         ("queso", "g", "eso"), ("beso", "g", "eso"), ("pesa", "g", "esa"),
         ("fiesta", "g", "esta"), ("finca", "g", "inka"),
         ("prístino", "e", "istino"), ("fin", "a", "in"), ("lindo", "g", "indo"),
         ("horno", "g", "orno"), ("bochorno", "g", "orno"), ("lóbrego", "e", "obrego"),
         ("mosco", "g", "osko"), ("fútbol", "g", "utbol"), ("buque", "g", "uke"),
         ("luma", "g", "uma"), ("bruma", "g", "uma"), ("puma", "g", "uma"),
         ("camélido", "e", "elido"), ("fétido", "e", "etido"), ("lúcido", "e", "usido"),
         ("bote", "g", "ote"), ("pote", "g", "ote"), ("cantar", "a", "ar"), ("espuma", "g", "uma"))
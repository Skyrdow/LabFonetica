package lab_fonetica;

import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.Scanner;


public class Rima_fn_3 {
    final int PROBABILIDAD_MISMA_RIMA = 6;
    
    final List<List<String>> lista = Arrays.asList(Arrays.asList("casa", "g", "asa"), Arrays.asList("mesa", "g", "esa"), Arrays.asList("canción", "a", "on"), Arrays.asList("lector", "a", "or"),
         Arrays.asList("pasa", "g", "asa"), Arrays.asList("lámpara", "e", "ampara"), Arrays.asList("trágico", "e", "axiko"),
         Arrays.asList("queso", "g", "eso"), Arrays.asList("beso", "g", "eso"), Arrays.asList("pesa", "g", "esa"),
         Arrays.asList("fiesta", "g", "esta"), Arrays.asList("finca", "g", "inka"),
         Arrays.asList("prístino", "e", "istino"), Arrays.asList("fin", "a", "in"), Arrays.asList("lindo", "g", "indo"),
         Arrays.asList("horno", "g", "orno"), Arrays.asList("bochorno", "g", "orno"), Arrays.asList("lóbrego", "e", "obrego"),
         Arrays.asList("mosco", "g", "osko"), Arrays.asList("fútbol", "g", "utbol"), Arrays.asList("buque", "g", "uke"),
         Arrays.asList("luma", "g", "uma"), Arrays.asList("bruma", "g", "uma"), Arrays.asList("puma", "g", "uma"),
         Arrays.asList("camélido", "e", "elido"), Arrays.asList("fétido", "e", "etido"), Arrays.asList("lúcido", "e", "usido"),
         Arrays.asList("bote", "g", "ote"), Arrays.asList("pote", "g", "ote"), Arrays.asList("cantar", "a", "ar"), Arrays.asList("espuma", "g", "uma"));
    
    
    public int[] eleccionNivel() {
        Integer ene_veces;
        int nivel;
        Scanner sc = new Scanner(System.in);
        int[] retorno = new int[2];
        
        System.out.print("Escriba el número 1 (básico), 2 (medio), 3 (avanzado) correspondiente a su nivel: ");
        nivel = sc.nextInt();
        
        retorno[0] = nivel;
        
        switch (nivel) {
            case 1:
                ene_veces = random(3,6);
                retorno[1] = ene_veces;
                break;
            case 2:
                ene_veces = random(5,9);
                retorno[1] = ene_veces;
                break;
            case 3:
                ene_veces = random(7,12);
                retorno[1] = ene_veces;
                break;
            default:
                System.out.println("Elija opciones entre 1 y 3, con números");
                break;
        }
        return retorno;
    }
    
    public List<BloqueRima> seleccionPalabras(int nivel) {
        List<BloqueRima> bloqueRimaLista = (List<BloqueRima>) new BloqueRima();
        java.util.Random random = new java.util.Random();
        BloqueRima palabra1 = new BloqueRima(lista.get(random.nextInt(lista.size())));
        BloqueRima palabra2 = new BloqueRima(lista.get(random.nextInt(lista.size())));
        
        if (nivel == 1) {
            while (!(palabra1.getCategoria().equals(palabra2.getCategoria()) &&
                    !palabra1.getPalabra().equals(palabra2.getPalabra()) &&
                    (!palabra1.getRima().equals(palabra2.getRima()) || 1 != random(1,PROBABILIDAD_MISMA_RIMA)))) {
                palabra1 = new BloqueRima(lista.get(random.nextInt(lista.size())));
                palabra2 = new BloqueRima(lista.get(random.nextInt(lista.size())));
            }
            bloqueRimaLista.add(palabra1);
            bloqueRimaLista.add(palabra2);
            return bloqueRimaLista;
        }
        
        else if (nivel == 2) {
            while (!((palabra1.getCategoria().equals(palabra2.getCategoria()) ||
                    compararCategorias(palabra1, palabra2, "a", "g")) &&
                    !palabra1.getPalabra().equals(palabra2.getPalabra()) &&
                    (!palabra1.getRima().equals(palabra2.getRima()) || 1 != random(1,PROBABILIDAD_MISMA_RIMA)))) {
                palabra1 = new BloqueRima(lista.get(random.nextInt(lista.size())));
                palabra2 = new BloqueRima(lista.get(random.nextInt(lista.size())));
            }
            bloqueRimaLista.add(palabra1);
            bloqueRimaLista.add(palabra2);
            return bloqueRimaLista;
        }
        
        else if (nivel == 3) {
            while (!((palabra1.getCategoria().equals(palabra2.getCategoria()) ||
                    compararCategorias(palabra1, palabra2, "a", "g") ||
                    (compararCategorias(palabra1, palabra2, "e", "g"))) &&
                    !palabra1.getPalabra().equals(palabra2.getPalabra()) &&
                    (!palabra1.getRima().equals(palabra2.getRima()) || 1 != random(1,PROBABILIDAD_MISMA_RIMA)))) {
                palabra1 = new BloqueRima(lista.get(random.nextInt(lista.size())));
                palabra2 = new BloqueRima(lista.get(random.nextInt(lista.size())));
            }
            bloqueRimaLista.add(palabra1);
            bloqueRimaLista.add(palabra2);
            return bloqueRimaLista;
        }  
        return null;
    }
    
    private int random(int min, int max) {
        Random numAleatorio = new Random();
        return numAleatorio.nextInt(max - min + 1) + min;
    }
    
    private boolean compararCategorias(BloqueRima p1, BloqueRima p2, String cat1, String cat2) {
        if (p1.getCategoria().equals(cat2) && p2.getCategoria().equals(cat1)) {
            return true;
        }
        if (p1.getCategoria().equals(cat1) && p2.getCategoria().equals(cat2)) {
            return true;
        }
        return false;
    }
    
    private int identificadorDeRima(BloqueRima palabra1, BloqueRima palabra2) {
        if (compararCategorias(palabra1, palabra2, "a", "e")) {
            return 1;
        }
        
        if (compararCategorias(palabra1, palabra2, "a", "g")) {
            return 1;
        }
        
        if (!palabra1.getPrimeraLetraRima().equals(palabra2.getPrimeraLetraRima())) {
            return 1;
        }
        
        if (palabra1.getPrimeraLetraRima().equals(palabra2.getPrimeraLetraRima())) {
            if (palabra1.getRima().equals(palabra2.getRima())) {
                return 2;
            }
            
            if (!palabra1.getRima().equals(palabra2.getRima())) {
                if (compararCategorias(palabra1, palabra2, "a", "a")) {
                    return 3;
                }
                
                String rimaSimp1 = simplificarDiptongos(palabra1);
                String rimaSimp2 = simplificarDiptongos(palabra2);
                
                if (compararCategorias(palabra1, palabra2, "e", "e")) {
                    String[] vocales1 = obtenerUltimas2Vocales(rimaSimp1);
                    String[] vocales2 = obtenerUltimas2Vocales(rimaSimp2);
                    if (vocales1[0].equals("") || vocales2[0].equals("") ||
                            vocales1[1].equals("") || vocales2[1].equals("")){
                        return 1;
                    }
                    
                    if (vocales1[0].equals(vocales2[0]) && vocales1[1].equals(vocales2[1])) {
                        return 3;
                    }
                    
                    else {
                        return 1;
                    }
                }
                
                if (compararCategorias(palabra1, palabra2, "e", "g") ||
                        compararCategorias(palabra1, palabra2, "g", "g")) {
                    if (obtenerUltimaVocal(rimaSimp1).equals(obtenerUltimaVocal(rimaSimp2))) {
                        return 3;
                    }
                    else {
                        return 1;
                    }
                }
            }
        }
        return 4;
    }
    
    private String obtenerUltimaVocal(String string) {
        List<String> vocales = Arrays.asList("a","e","i","o","u");
        String ultimoCaracter = string.substring(string.length() - 1);
        for (String v: vocales) {
            if (ultimoCaracter.equals(v)) {
                return ultimoCaracter;
            }
        }
        if (string.length() > 1) {
            return string.substring(string.length() - 2);
        }
        return null;
    }
    
    private String[] obtenerUltimas2Vocales(String string) {
        String[] listaVocales = new String[2];
        String vocal1 = "";
        String vocal2 = "";
        List<String> vocales = Arrays.asList("a","e","i","o","u");
        List<String> listaReversedString = stringToList(voltearString(string));
        boolean primeroEncontrado = false;
        for (String s: listaReversedString) {
            for (String v: vocales) {
                if (s.equals(v)) {
                    if (!primeroEncontrado) {
                        vocal1 = s;
                        primeroEncontrado = true;
                    }
                    else {
                        vocal2 = s;
                        listaVocales[0] = vocal1;
                        listaVocales[1] = vocal2;
                        return listaVocales;
                    }
                }
            }
        }
        return null;
    }
    
    private String simplificarDiptongos(BloqueRima palabra) {
        List<String> lista1 = Arrays.asList("ai", "au","ua","ia","ei","eu","ue","ie","oi","ou","io","uo","iu","iu","ui");
        List<String> lista2 = Arrays.asList("a","a","a","a","e","e","e","e","o","o","o","o","i","u","u");
        String restoRima = palabra.getRestoRima();
        for (String p1: lista1) {
            for (String p2: lista2) {
                restoRima = restoRima.replace(p1, p2);
                break;
            }
        }
        return restoRima;
    }
    
    private String voltearString(String string) {
        char ch;
        String newString = "";
        for (int i=0; i < string.length(); i++) {
            ch = string.charAt(i);
            newString = ch + newString;
        }
        return newString;
    }
    
    private List<String> stringToList(String string) {
        String[] stringSplit = string.split("");
        List<String> stringList = Arrays.asList(stringSplit);
        return stringList;
    }
    
}

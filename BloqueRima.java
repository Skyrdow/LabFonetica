package Laboratorio.Fonetica.Laboratorio.Fonetica.service;

import java.util.List;


public class BloqueRima {
    private String palabra;
    private String categoria;
    private String rima;
    private String primeraLetraRima;
    private String restoRima;

    public BloqueRima() {
    }
    
    public BloqueRima(String[] bloquePalabra) {
        this.palabra = bloquePalabra[0];
        this.categoria = bloquePalabra[1];
        this.rima = bloquePalabra[2];
        this.primeraLetraRima = bloquePalabra[0].substring(2, 2);
        this.restoRima = bloquePalabra[2].substring(1);
    }

    public String getPalabra() {
        return palabra;
    }
    public String getCategoria() {
        return categoria;
    }

    public String getRima() {
        return rima;
    }

    public String getPrimeraLetraRima() {
        return primeraLetraRima;
    }


    public String getRestoRima() {
        return restoRima;
    }

}

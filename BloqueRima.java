package lab_fonetica;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class BloqueRima {
    private String palabra;
    private String categoria;
    private String rima;
    private String primeraLetraRima;
    private String restoRima;

    public BloqueRima() {
    }
    
    public BloqueRima(List<String> bloquePalabra) {
        this.palabra = bloquePalabra.get(0);
        this.categoria = bloquePalabra.get(1);
        this.rima = bloquePalabra.get(2);
        this.primeraLetraRima = bloquePalabra.get(0).substring(2, 2);
        this.restoRima = bloquePalabra.get(2).substring(1);
    }

    public String getPalabra() {
        return palabra;
    }

    public void setPalabra(String palabra) {
        this.palabra = palabra;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public String getRima() {
        return rima;
    }

    public void setRima(String rima) {
        this.rima = rima;
    }

    public String getPrimeraLetraRima() {
        return primeraLetraRima;
    }

    public void setPrimeraLetraRima(String primera_letra_rima) {
        this.primeraLetraRima = primera_letra_rima;
    }

    public String getRestoRima() {
        return restoRima;
    }

    public void setRestoRima(String resto_rima) {
        this.restoRima = resto_rima;
    }
    
    @Override
    public String toString(){
        return this.palabra + " " + this.categoria + " " + this.rima + " " + this.primeraLetraRima + " " + this.restoRima; 
    }
    
    
}

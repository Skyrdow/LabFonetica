package Laboratorio.Fonetica.Laboratorio.Fonetica.service;

import Laboratorio.Fonetica.Laboratorio.Fonetica.dao.Sentence2Dao;
import Laboratorio.Fonetica.Laboratorio.Fonetica.dto.Sentence2.Sentence2Dto;
import Laboratorio.Fonetica.Laboratorio.Fonetica.dto.Sentence2.Sentence2OutDto;
import Laboratorio.Fonetica.Laboratorio.Fonetica.mapper.Sentence2Mapper;
import Laboratorio.Fonetica.Laboratorio.Fonetica.model.Sentence2;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class Sentence2Service {

    final int PROBABILIDAD_MISMA_RIMA = 6;

    @Autowired
    private Sentence2Dao sentence2Dao;

    @Autowired
    private Sentence2Mapper sentence2Mapper;

    public ArrayList<Sentence2Dto> getAllSentence2() {return sentence2Mapper.generateSentence2DTOS(sentence2Dao.findAll());
    }

    public Sentence2Dto saveSentence2(Sentence2Dto sentenceDto) {
        Sentence2 sentence2 = sentence2Mapper.Sentence2DtoToSentence2(sentenceDto);
        System.out.println(sentence2);
        sentence2Dao.save(sentence2);
        return sentence2Mapper.Sentence2ToSentence2Dto(sentence2);
    }

    public Sentence2Dto updateSentence2(Long id, Sentence2Dto sentenceDto) {
        Sentence2 sentence2 = sentence2Dao.findById(id).get();
        sentence2 = sentence2Mapper.Sentence2DtoToSentence2(sentenceDto);
        sentence2.setId(id);
        sentence2Dao.save(sentence2);
        return sentence2Mapper.Sentence2ToSentence2Dto(sentence2);
    }

    public void deleteSentence2 (Long id_sentence) {
        sentence2Dao.delete(sentence2Dao.findById(id_sentence).get());
    }

    public ArrayList<Sentence2OutDto> getSentences2(Integer level) {
        List<List<Map<String, Object>>> sentences2 = new ArrayList<>();
        ArrayList<Sentence2OutDto> outputSentences2 = new ArrayList<>();
        int quantity = 0, i, aux;
        if (level == 1)
            quantity = random(3, 5);
        else if (level == 2)
            quantity = random(4, 8);
        else if (level == 3)
            quantity = random(7, 12);
        sentences2.add(sentence2Dao.getAllSentenceType1());
        sentences2.add(sentence2Dao.getAllSentenceType2());
        sentences2.add(sentence2Dao.getAllSentenceType3());
        for (i = 0; i < quantity; i++) {
            if (level == 1){
              aux = random(1,3);
              outputSentences2.add(getQuestion(aux,sentences2));
            } else if (level == 2){
                aux = random(1,4);
                outputSentences2.add(getQuestion(aux,sentences2));
            } else {
                aux = random(1,5);
                outputSentences2.add(getQuestion(aux,sentences2));
            }
        }
        return outputSentences2;
    }

    private int random(int min, int max) {
        Random numAleatorio = new Random();
        return numAleatorio.nextInt(max - min + 1) + min;
    }

    private Sentence2OutDto getQuestion(int type, List<List<Map<String, Object>>> sentences2) {
        Sentence2OutDto sentence2OutDto = new Sentence2OutDto();
        String[] word1 = new String[0], word2 = new String[0];
        if (type == 1 ){
            do {
            word1 = preparateList(sentences2.get(0).get(random(0,sentences2.get(0).size()-1)).get("palabra").toString().split("-"));
            word2 = preparateList(sentences2.get(0).get(random(0,sentences2.get(0).size()-1)).get("palabra").toString().split("-"));
            }while (word1[0].equals(word2[0]));}
        else if (type == 2 ){
            do {
                word1 = preparateList(sentences2.get(1).get(random(0,sentences2.get(1).size()-1)).get("palabra").toString().split("-"));
                word2 = preparateList(sentences2.get(1).get(random(0,sentences2.get(1).size()-1)).get("palabra").toString().split("-"));
            }while (word1[0].equals(word2[0]));
        }
        else if (type == 3 ){
            do {
                word1 = preparateList(sentences2.get(2).get(random(0,sentences2.get(2).size()-1)).get("palabra").toString().split("-"));
                word2 = preparateList(sentences2.get(2).get(random(0,sentences2.get(2).size()-1)).get("palabra").toString().split("-"));
            }while (word1[0].equals(word2[0]));
        }
        else if (type == 4 ){
            do {
                word1 = preparateList(sentences2.get(0).get(random(0,sentences2.get(0).size()-1)).get("palabra").toString().split("-"));
                word2 = preparateList(sentences2.get(1).get(random(0,sentences2.get(1).size()-1)).get("palabra").toString().split("-"));
            }while (word1[0].equals(word2[0]));}
        else if (type == 5 ){
            do {
                word1 = preparateList(sentences2.get(1).get(random(0,sentences2.get(1).size()-1)).get("palabra").toString().split("-"));
                word2 = preparateList(sentences2.get(2).get(random(0,sentences2.get(2).size()-1)).get("palabra").toString().split("-"));
            }while (word1[0].equals(word2[0])); }
        sentence2OutDto.setWord1(word1[0]);
        sentence2OutDto.setWord2(word2[0]);
        sentence2OutDto.setResult(identificadorDeRima(new BloqueRima(word1),new BloqueRima(word2)));

        return sentence2OutDto;
    }

    private String[] preparateList(String[] word){
        word[0] = word[0].replace(" ","");
        word[1] = word[1].replace(" ","");
        word[2] = word[2].replace(" ","");
        return word;
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
        else {
            if (palabra1.getRima().equals(palabra2.getRima())) {
                return 2;
            }

            else {
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

    private boolean compararCategorias(BloqueRima p1, BloqueRima p2, String cat1, String cat2) {
        if (p1.getCategoria().equals(cat2) && p2.getCategoria().equals(cat1)) {
            return true;
        }
        if (p1.getCategoria().equals(cat1) && p2.getCategoria().equals(cat2)) {
            return true;
        }
        return false;
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

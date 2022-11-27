package Laboratorio.Fonetica.Laboratorio.Fonetica.service;

import Laboratorio.Fonetica.Laboratorio.Fonetica.dao.Sentence2Dao;
import Laboratorio.Fonetica.Laboratorio.Fonetica.dto.Sentence2.Sentence2Dto;
import Laboratorio.Fonetica.Laboratorio.Fonetica.dto.Sentence2.Sentence2OutDto;
import Laboratorio.Fonetica.Laboratorio.Fonetica.mapper.Sentence2Mapper;
import Laboratorio.Fonetica.Laboratorio.Fonetica.model.Sentence2;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Random;

@Service
public class Sentence2Service {

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
        String[] word1, word2;
        if (type == 1 ){
            do {
            word1 = preparateList(sentences2.get(0).get(random(0,sentences2.get(0).size()-1)).get("palabra").toString().split("-"));
            word2 = preparateList(sentences2.get(0).get(random(0,sentences2.get(0).size()-1)).get("palabra").toString().split("-"));
            }while (word1[0].equals(word2[0]));
            sentence2OutDto.setWord1(word1[0]);
            sentence2OutDto.setWord2(word2[0]);
            sentence2OutDto.setResult(getResult(word1,word2));
        }
        else if (type == 2 ){
            do {
                word1 = preparateList(sentences2.get(1).get(random(0,sentences2.get(1).size()-1)).get("palabra").toString().split("-"));
                word2 = preparateList(sentences2.get(1).get(random(0,sentences2.get(1).size()-1)).get("palabra").toString().split("-"));
            }while (word1[0].equals(word2[0]));
            sentence2OutDto.setWord1(word1[0]);
            sentence2OutDto.setWord2(word2[0]);
            sentence2OutDto.setResult(getResult(word1,word2));

        }
        else if (type == 3 ){
            do {
                word1 = preparateList(sentences2.get(2).get(random(0,sentences2.get(2).size()-1)).get("palabra").toString().split("-"));
                word2 = preparateList(sentences2.get(2).get(random(0,sentences2.get(2).size()-1)).get("palabra").toString().split("-"));
            }while (word1[0].equals(word2[0]));
            sentence2OutDto.setWord1(word1[0]);
            sentence2OutDto.setWord2(word2[0]);
            sentence2OutDto.setResult(getResult(word1,word2));

        }
        else if (type == 4 ){
            do {
                word1 = preparateList(sentences2.get(0).get(random(0,sentences2.get(0).size()-1)).get("palabra").toString().split("-"));
                word2 = preparateList(sentences2.get(1).get(random(0,sentences2.get(1).size()-1)).get("palabra").toString().split("-"));
            }while (word1[0].equals(word2[0]));
            sentence2OutDto.setWord1(word1[0]);
            sentence2OutDto.setWord2(word2[0]);
            sentence2OutDto.setResult(getResultType1And2(word1,word2));
        }
        else if (type == 5 ){
            do {
                word1 = preparateList(sentences2.get(1).get(random(0,sentences2.get(1).size()-1)).get("palabra").toString().split("-"));
                word2 = preparateList(sentences2.get(2).get(random(0,sentences2.get(2).size()-1)).get("palabra").toString().split("-"));
            }while (word1[0].equals(word2[0]));
            sentence2OutDto.setWord1(word1[0]);
            sentence2OutDto.setWord2(word2[0]);
            sentence2OutDto.setResult(getResultTheSameType3(word1[2],word2[2]));
        }
        return sentence2OutDto;
    }

    private String[] preparateList(String[] word){
        word[0] = word[0].replace(" ","");
        word[1] = word[1].replace(" ","");
        word[2] = word[2].replace(" ","");
        return word;
    }

    private int getResultType1And2(String[] rhyme1, String[] rhyme2){
        if (rhyme1[2].replace(" ", "").substring(0,1).equals(rhyme2[2].replace(" ", "").substring(0,1)))
            return 3;
        return 1;
    }

    private int getResult(String[] rhyme1, String[] rhyme2){
        try{
            if (!rhyme1[2].replace(" ", "").substring(0,1).equals(rhyme2[2].replace(" ", "").substring(0,1)))
                return 1;
            else if (rhyme1[2].replace(" ", "").equals(rhyme2[2].replace(" ","")))
                return 2;
            else {
                if (rhyme1[1].replace(" ","").equals(rhyme2[1].replace(" ",""))){
                    if (rhyme1[1].replace(" ","").equals("1")){
                        rhyme1[2] = replaceRhyme(rhyme1[2]);
                        rhyme2[2] = replaceRhyme(rhyme2[2]);
                        return getResultTheSameType1And2(rhyme1[2], rhyme2[2]);
                    }
                    else if (rhyme1[1].replace(" ","").equals("2")){
                        rhyme1[2] = replaceRhyme(rhyme1[2]);
                        rhyme2[2] = replaceRhyme(rhyme2[2]);
                        return getResultTheSameType1And2(rhyme1[2], rhyme2[2]);
                    }
                    else if (rhyme1[1].replace(" ","").equals("3")){
                        rhyme1[2] = replaceRhyme(rhyme1[2]);
                        rhyme2[2] = replaceRhyme(rhyme2[2]);
                        return getResultTheSameType3(rhyme1[2], rhyme2[2]);
                    }
                }
                return 1;
            }
        }catch (Exception e){
            System.out.println("aca estoy: " + e.toString());
        }
        return 1;
    }

    private String replaceRhyme(String rhyme){
        return rhyme.replace("ai","a").replace("au","a").replace("ei","e").replace("eu","e")
                .replace("oi","o").replace("Iu","i").replace("Ui","u");
    }

    private int getResultTheSameType1And2(String rhyme1, String rhyme2){
        try{
            List<List<String>> vocals = new ArrayList<>();
            vocals.add(countVocals(rhyme1));
            vocals.add(countVocals(rhyme2));
            if ((vocals.get(0).get(0).equals(vocals.get(1).get(0))) || (vocals.get(0).get(1).equals(vocals.get(1).get(1))) || (vocals.get(0).get(2).equals(vocals.get(1).get(2))) ||
                    (vocals.get(0).get(3).equals(vocals.get(1).get(3))) || (vocals.get(0).get(4).equals(vocals.get(1).get(4))) )
                return 3;
            else
                return 1;
        }catch (Exception e){
            System.out.println("aca 1" + e.getMessage() + e.toString());
        }
        return 1;
    }

    private int getResultTheSameType3(String rhyme1, String rhyme2){
        int aux1, aux2;
        List<List<String>> vocals = new ArrayList<>();
        vocals.add(countVocals(rhyme1));
        vocals.add(countVocals(rhyme2));
        aux1 = getTypeVocalOrConso(rhyme1);
        aux2 = getTypeVocalOrConso(rhyme2);
        try{
            if (aux1 == aux2){
                if (aux1 == 1){
                    if (rhyme1.substring(rhyme1.length()-1,rhyme1.length()).equals(rhyme2.substring(rhyme2.length()-1,rhyme2.length())))
                        return 3;
                    return 1;
                }
                else if (aux1 == 2){
                    if (rhyme1.substring(rhyme1.length()-2,rhyme1.length()-1).equals(rhyme2.substring(rhyme2.length()-2,rhyme2.length()-1)))
                        return 3;
                    return 1;
                }
            }
            else if (aux1 != aux2){
                if (aux1 == 1){
                    if (rhyme1.substring(rhyme1.length()-1,rhyme1.length()).equals(rhyme2.substring(rhyme2.length()-2,rhyme2.length()-1)))
                        return 3;
                    return 1;
                }
                else if (aux2 == 1){
                    if (rhyme2.substring(rhyme2.length()-1,rhyme2.length()).equals(rhyme1.substring(rhyme1.length()-2,rhyme1.length()-1)))
                        return 3;
                    return 1;
                }
            }
            return 1;
        }catch (Exception e){

            System.out.println("aca 3" + e.toString() + e.getMessage());
        }
        return 1;
    }

    private int getTypeVocalOrConso(String word){
        if (word.substring(word.length()-1,word.length()).equals("a") || word.substring(word.length()-1,word.length()).equals("e") ||
                word.substring(word.length()-1,word.length()).equals("i") || word.substring(word.length()-1,word.length()).equals("o") ||
                word.substring(word.length()-1,word.length()).equals("u"))
            return 1;
        return 0;
    }

    private List<String> countVocals(String rhyme){
        List<String> vocals = new ArrayList<>();
        vocals.add(String.valueOf(rhyme.chars().filter(vocal -> vocal == 'a').count()));
        vocals.add(String.valueOf(rhyme.chars().filter(vocal -> vocal == 'e').count()));
        vocals.add(String.valueOf(rhyme.chars().filter(vocal -> vocal == 'i').count()));
        vocals.add(String.valueOf(rhyme.chars().filter(vocal -> vocal == 'o').count()));
        vocals.add(String.valueOf(rhyme.chars().filter(vocal -> vocal == 'u').count()));
        return vocals;
    }

}
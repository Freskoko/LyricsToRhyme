from collections import Counter
import pronouncing
import random

def open_lyrics():
    with open("lyrics.txt","r") as lyrics:
        lines = lyrics.read() #.replace('\n', ' ')
        lines = lines.split(" ")

        cleanlines = []
        
        #clean lines
        for word in lines:
            word = word.replace(")","")
            word = word.replace("(","")
            word = word.replace(",","")

            cleanlines.append(word)
            #-test comment

        return cleanlines

def find_common_words(wordlist):

    while "\n" in wordlist:
        wordlist.remove("\n")

    newworldlist = []
    for word in wordlist:
        word = word.replace("\n"," ")
        for subword in word.split(" "):
            newworldlist.append(subword)

    commonwords = Counter(newworldlist)
    commonlist = list(commonwords.items())
    commonlist.sort(key = lambda i:i[1], reverse = True)
 
    return(commonlist[0:30])

def replace_words(words,replace):

    replace = [i[0] for i in replace]
    print(replace)
    
    newwords = []
    perm_rhyme_dict = {}

    for sentence in words:

        if sentence in perm_rhyme_dict.keys():
            newwords.append(  perm_rhyme_dict[sentence]  )
                
        elif sentence in replace:

            rhymes = pronouncing.rhymes(sentence)

            if rhymes != []:
                
                

                rhymesentence = random.choice(rhymes)
                attempt = 0
                while is_rhyme_not_accepted(sentence,rhymesentence,attempt):
                    #check if rhyme is ok or is weird
                    rhymesentence = random.choice(rhymes)
                    attempt+=1
                
                newwords.append(rhymesentence)
                perm_rhyme_dict.setdefault(sentence,rhymesentence)

        else:       
            newwords.append(sentence)
    

    with open(f"data/rhyminglyrics7.txt","w") as f:
        f.writelines(" ".join(newwords))

    return "completed"

from spellchecker import SpellChecker

def is_rhyme_not_accepted(originalword,rhyme,attempt):    

    if attempt == 10:
        return (False)
    
    spell = SpellChecker()
    if rhyme == spell.correction(rhyme):

        ogphones = pronouncing.phones_for_word(originalword)
        syll_in_og = pronouncing.syllable_count(ogphones[0])

        rhymephones = pronouncing.phones_for_word(rhyme)
        syll_in_rhyme = pronouncing.syllable_count(rhymephones[0])

        if syll_in_rhyme <= syll_in_og + 2:
            print(rhyme)
            return False
        

    return True



if __name__ == "__main__":

    lyrics = open_lyrics()
    commonwords = find_common_words(lyrics)

    print(replace_words(lyrics,commonwords))
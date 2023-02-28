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

        return cleanlines

def find_common_words(wordlist):

    commonwords = Counter(wordlist)
    commonlist = list(commonwords.items())
    commonlist.sort(key = lambda i:i[1], reverse = True)
 
    return(commonlist)

def replace_words(words,replace):

    # print(words)
   
    longLyrics = (" ".join(words))

    for word,num in replace:
        
            try:

                rhyme = pronouncing.rhymes(word)
                chosenrhyme = random.choice(rhyme)

                while pronouncing.syllable_count(word) != pronouncing.syllable_count(chosenrhyme) and len(chosenrhyme) != len(word) and word not in chosenrhyme:
                    rhyme = pronouncing.rhymes(word)
                    chosenrhyme = random.choice(rhyme)
                
                print(chosenrhyme,word)

                # while word in longLyrics:
                longLyrics = longLyrics.replace(word,chosenrhyme)

            except Exception as e:
                print(f"error {e}")


    with open("data/rhyminglyricsAll1.txt","w") as f:
        f.writelines(longLyrics)

    return "completed"

commonwords = find_common_words(open_lyrics())
print(replace_words(open_lyrics(),commonwords))
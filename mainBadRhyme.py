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
 
    return(commonlist[0:7])

def replace_words(words,replace):

    # print(words)
   
    longLyrics = (" ".join(words))

    for word,num in replace:
        
        for i in range(longLyrics.count(word)):
            try:

                rhyme = pronouncing.rhymes(word)
                chosenrhyme = random.choice(rhyme)
                print(chosenrhyme)

                # while word in longLyrics:
                longLyrics = longLyrics.replace(word,chosenrhyme,1)

            except Exception as e:
                print(f"error {e}")


    with open("rhyminglyricsNEW8.txt","w") as f:
        f.writelines(longLyrics)

    return "completed"

commonwords = find_common_words(open_lyrics())
print(replace_words(open_lyrics(),commonwords))
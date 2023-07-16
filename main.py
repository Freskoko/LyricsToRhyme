from collections import Counter
import pronouncing
import random
#TODO dictonary

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

    #for line in words
    #if word in replace, find a rhyme
    #replace word with rhyme
    #try 10 times, if fails then go next line

    replace = [i[0] for i in replace]
    newwords = []
    print(replace)

    for sentence in words:
        
        if sentence in replace:

            rhyme = pronouncing.rhymes(sentence)
            if rhyme != []:
                
                attempt = 0

                sentence = random.choice(rhyme)
                while is_rhyme_not_accepted(sentence,attempt):
                    #check if rhyme is ok or is weird
                    sentence = random.choice(rhyme)
                    print(sentence)
                    attempt+=1
        
        newwords.append(sentence)
    

    with open(f"data/rhyminglyrics7.txt","w") as f:
        f.writelines(" ".join(newwords))

    return "completed"

def is_rhyme_not_accepted(rhyme,attempt):

    if attempt == 10:
        return (False)
    
    return True



if __name__ == "__main__":

    lyrics = open_lyrics()
    commonwords = find_common_words(lyrics)

    print(replace_words(lyrics,commonwords))
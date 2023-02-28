import api.get_word as word
import api.getch as keyboard
import os

words = []

nb_mots=10

for i in range(10):
    random_words = word.randomWord()
    for j in range(10):
        words.append(random_words[j])
    print("["+"|"*i+" "*(10-i)+"] "+ str(i)+"0%",end="\r")    

print(words)
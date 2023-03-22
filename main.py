#!/bin/python3

import api.get_word as word
import api.getch as keyboard
import os
import time 

def dactylo(nb_mots,Time,lang):
    """The main fuction of the dactylo who will need dactylo to change the color of the letters

    Args:
        nb_mots (int): number of words /10 (if nb_mots = 10 so there will be 100 words)
        Time (bool): true if it's the time mod
        lang (str): the lang of the game ('f' if french, 'e' if english)

    Returns:
        str: the message it'll be printed
    """
    words = ""
    pos = 0
    timer = None

    ### Taking the words and setup ### 

    for i in range(nb_mots):
        random_words = word.randomWord(lang)
        for j in range(10):
            words += random_words[j].lower() + " "
        print('\033[32m'+"■"*i+'\033[31m'+"□"*(10-i)+'\033[0m'+" "+str(i)+"0%",end="\r")    

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[0m'+words)

    ### The 30 sec mod ###

    if Time == True:
        while True:
            right = False
            while not right:
                inp = keyboard.getch()
                if timer == None:
                    timer = time.perf_counter()
                if inp == words[pos]:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\033[32m'+words[:pos+1]+'\033[33m'+words[pos+1]+'\033[0m'+words[pos+2:])
                    right = True
                    pos +=1
            if time.perf_counter() > timer + 30:
                break

        wpm = round((pos)/2.5)
        if wpm<0:
            wpm = 0
        return str(wpm)+" wpm"

    ### The 10 words mod ###

    for pos in range(len(words)-1):
        right = False
        while not right:
            inp = keyboard.getch()
            if timer == None:
                timer = time.perf_counter()
            if inp == words[pos]:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\033[32m'+words[:pos+1]+'\033[33m'+words[pos+1]+'\033[0m'+words[pos+2:])
                right = True
    temps = round(time.perf_counter()-timer,1)
    wpm = round((pos)*12/temps)
    if wpm<0:
        wpm = 0
    return str(temps)+" s "+str(wpm)+" wpm"



print("(F)rançais / (E)nglish")
while True:
    inp = keyboard.getch()
    if inp == "e":
        lang='en'
        break
    elif inp == "f":
        lang='fr'
        break
print("(T)ime / (W)ords")
while True:
    inp = keyboard.getch()
    if inp == "t":
        print(dactylo(10,True,lang))
        break
    elif inp == "w":
        print(dactylo(1,False,lang))
        break

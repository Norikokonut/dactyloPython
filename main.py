import api.get_word as word
import api.getch as keyboard
import os
import time 

def dactylo(nb_mots,Time):
    words = ""
    pos = 0
    error = 0
    timer = None


    for i in range(nb_mots):
        random_words = word.randomWord()
        for j in range(10):
            words += random_words[j].lower() + " "
        print("■"*i+"□"*(10-i),str(i)+"0%",end="\r")    

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[0m'+words)

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
                else:
                    error += 1
            if time.perf_counter() > timer + 30:
                break

        wpm = round((pos-error)/2.5)
        if wpm<0:
            wpm = 0
        print(str(wpm)+" wpm")

    else:
        for _ in range(len(words)):
            right = False
            while not right:
                inp = keyboard.getch()
                if timer == None:
                    timer = time.perf_counter()
                if inp == words[pos]:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\033[32m'+words[:pos+1]+'\032[0m'+words[pos+1]+'\033[0m'+words[pos+2:])
                    right = True
                    pos +=1
                else:
                    error += 1
        temps = round(time.perf_counter()-timer,1)
        wpm = round((pos-error)*12/temps)
        if wpm<0:
            wpm = 0
        print(str(temps)+"s")
        print(str((wpm))+" wpm")


print("(T)ime / (W)ords")
while True:
    inp = keyboard.getch()
    if inp == "t":
        dactylo(10,True)
        break
    elif inp == "w":
        dactylo(1,False)
        break
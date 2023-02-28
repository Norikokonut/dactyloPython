import api.get_word as word
import api.getch as keyboard
import os
import time 

words = ""
nb10mots=10

for i in range(nb10mots):
    random_words = word.randomWord()
    for j in range(10):
        words += random_words[j].lower() + " "
    print("■"*i+"□"*(10-i),str(i)+"0%",end="\r")    

os.system('cls' if os.name == 'nt' else 'clear')
print('\033[31m'+"|"+'\033[0m'+words)

while keyboard.getch() == words[0]:
    pos = 1
timer = time.perf_counter()

while time.perf_counter() < timer+30:
    right = False
    while not right:
        inp = keyboard.getch()
        if inp == words[pos]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(words[:pos+1]+'\033[31m'+"|"+'\033[0m'+words[pos+1:])
            right = True
            pos +=1

print(str(pos*2)+" letter per minutes")
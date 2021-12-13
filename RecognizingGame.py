import pandas as pd
import random
import sys, getpass
import os

## Check if files exists
if (os.path.exists('words.txt') == False):
    with open('words.txt', 'w') as f:
        f.write("interpretation = tercüme")
        f.close()

if (os.path.exists('sentences.txt') == False):
    with open('sentences.txt', 'w') as f:
        f.write("existentialism, any of various philosophies, most influential in continental Europe from about 1930 to the mid-20th century, that have in common an interpretation of human existence in the world that stresses its concreteness and its problematic character. = varoluşçuluk, yaklaşık 1930'dan 20. yüzyılın ortalarına kadar kıta Avrupası'nda en etkili olan, dünyadaki insan varoluşunun somutluğunu ve sorunlu karakterini vurgulayan ortak bir yorumuna sahip çeşitli felsefelerden herhangi biri. ")
    f.close()

## construct words dictionary
words = {}

f = open("words.txt")
for line in f:
    key, value = line.split('=')
    words[key] = value
f.close()

## construct sentences dictionary
sentences = {}

f = open("sentences.txt")
for line in f:
    key, value = line.split('=')
    sentences[key] = value
f.close()

## adds element to given dictionary
def add_element(dictionary):

        string = input()
        if(string == "exit"):
            return False
        key, value = string.split('=')
        dictionary[key] = value
        return True

## starts the game
def play_game(dictionary):
        
        true_answers = 0
        total = 0
        string = input("Press enter to start the game! \(exit+enter to exit\) ")
        if(string == "exit"):
                return
        
        while True:      

            if(string == "exit"):
                break
            element, meaning = random.choice(list(dictionary.items()))
            string = input(element + "? ")

            if string == meaning.strip():
                true_answers += 1
                total += 1
                print("Correct! Score:" +str(true_answers)+'/'+str(total))

            else:
                total += 1
                print("False! Score:" +str(true_answers)+'/'+str(total))
            
        return score

## at the end, writes updated dictionary to the file
def write_dict_to_file(dictionary, file_name):
    with open(file_name, 'w') as f:
           for key, value in dictionary.items():
                 f.write(str(key)+ '='+ str(value))
            f.close()

print ("""Menu
1. Add a word with =
2. Add a sentences with = 
3. Play words game!
4. Play sentences game!
5. Exit
    """)


while True:
    
    menuchoice = int(input())
    
    if(menuchoice == 1):
        choice = True
        while choice:
            choice = add_element(words)
    elif(menuchoice == 2):
        choice = True
        while choice:
            choice = add_element(sentences)
    elif(menuchoice == 3):
        play_game(words)
    elif(menuchoice == 4):
        play_game(sentences)
    elif(menuchoice == 5):
        break
    else:
        print("Wrong choice")


write_dict_to_file(words,"words.txt")
write_dict_to_file(sentences,"sentences.txt")
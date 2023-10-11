from nltk.corpus import words
import random 
import time


def checkInput(l, w,c) :
    if(l.isalpha()!=True):
        return c
    counter=0
    for i in range(0,len(word)):
        if(l==w[i]):
            blanks[i]=l    
        else:
            counter+=1
    if(counter==len(word)):
        c-=1
    return c

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
chances = 6
notwon=False
wordNum= random.randint(0,len(words.words())-1)
word=words.words()[wordNum]
blanks=[]
for x in range(0,len(word)):
    blanks.append("_")
while(chances>=0):
    if(chances==6):
        print(stages[-1])
    elif(chances==5):
        print(stages[-2])
    elif(chances==4):
        print(stages[-3])
    elif(chances==3):
        print(stages[-4])
    elif(chances==2):
        print(stages[-5])
    elif(chances==1):
        print(stages[-6])
    elif(chances==0):
        print(stages[0])
    for i in range(0,len(blanks)):
        print(blanks[i]+ " ", end=" ")
    print("\n")
   # print(word)
    letter=input("Guess a letter: ").lower()
    if letter in blanks:
        print(f"you allready used {letter}")
    chances=checkInput(letter,word,chances)
    if "_" not in blanks:
        notwon=True
        print("You WON!")
        break
    time.sleep(0.5)
    print("\033[H\033[J", end="")
if(chances==0):
    print("You lost! Better luck next time!")
    
    


   
    

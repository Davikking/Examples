import random
selection=0
# Rock
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
choices=[rock, paper, scissors]
rock_paper_scissors=input("Enter rock, paper, or scissors: ")
rock_paper_scissors=rock_paper_scissors.lower()
if(rock_paper_scissors=="rock"):
    selection=0
elif(rock_paper_scissors=="paper"):
    selection=1
elif(rock_paper_scissors=="scissors"):
    selection=2
else:
    print("inproper input defaulting to rock")
    selection=0
cpu_choice=random.randint(0,2)
print(choices[selection])
print(choices[cpu_choice])
if(selection==cpu_choice):
    print("Tie")
elif(selection==0 and cpu_choice==2):
    print("Player 1 wins!")
elif(selection==0 and cpu_choice==1):
    print("Player 1 loses!")
elif(selection==1 and cpu_choice==0):
    print("Player 1 wins!")
elif(selection==1 and cpu_choice==2):
    print("Player 1 loses!")
elif(selection==2 and cpu_choice==1):
    print("Player 1 wins!")
elif(selection==2 and cpu_choice==0):
    print("Player 1 loses!")


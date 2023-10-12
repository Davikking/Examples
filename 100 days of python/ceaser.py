from art import logo

def caeser(task, txt, shft):
    temptxt=""
    if(task=="encode"):
        for x in txt:
           if(x.isalpha()):
            index=alphabet.index(x)
            temptxt+=alphabet[(index+shft)%len(alphabet)]
           else:
              temptxt+=x
        print(f"the encoded text is {temptxt}")
    if(task=="decode"):
        for x in txt:
            if(x.isalpha()):
                index=alphabet.index(x)
                temptxt+=alphabet[(index-shft)%len(alphabet)]
            else:
                temptxt+=x

        print(f"the decoded text is {temptxt}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
runAgain=True
again=""
while(runAgain):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(task=direction, txt=text, shft=shift)
    again=input("Do you want to run again? yes/no: ").lower()
    if(again=="no"):
        runAgain=False
        print("GoodBye!")




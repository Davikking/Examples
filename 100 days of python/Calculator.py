import math

def add(n1, n2):
    """This function adds the two numbers entered together"""
    return n1+n2
def sub(n1,n2):
    """This function subtracts two numbers entered"""
    return n1-n2
def mult(n1,n2):
    """This function multiplys two numbers sent to it"""
    return n1*n2
def div(n1, n2):
    """This function divides the two numbers given to it """
    return n1/n2
def power(n1,n2):
    """This raises the first number to the power of the second """
    return math.pow(n1,n2)
operations={"+":add,"-":sub,"*":mult,"/":div,"^":power}
done=False
firstRun=True
while done==False:
    if firstRun:
     num1=float(input("enter the first number: "))
     for key in operations:
            print(key)
     opt=input("enter operation to preform: ")
     num2=float(input("enter the second number: "))
     ans=operations[opt](num1,num2)
    else:
     for key in operations:
        print(key)
     opt=input("enter operation to preform: ")
     num2=float(input("enter the second number: "))
     ans=operations[opt](ans,num2)
    print(ans)
    selection = input("Type y to continue clculating, c to clear, and n to stop.").lower()
    if(selection=="y"):
        firstRun=False
    elif(selection=="c"):
        firstRun=True
        print("\033[H\033[J", end="")
    elif(selection=="n"):
        done=True
        print("Good Bye!")
    else:
        print("Your selection wasnt an option! Good Bye!")

    
    



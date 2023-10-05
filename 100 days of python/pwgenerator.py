import random
import string
password=[]
num_letters=int(input("please enter number of letters you want in your password: "))
num_num=int(input("please enter the number of numbers you want in your password: "))
num_symb=int(input("please enter the number of symbols you want in your password: "))

for x in range(num_letters):
    password.append(random.choice(string.ascii_letters))
for x in range(num_num):
    password.append(random.randint(0,9))
for x in range(num_symb):
    password.append(random.choice('!@#$%^&*()_-'))
random.shuffle(password)
listToStr = ' '.join([str(elem) for elem in password])
print(listToStr)
#final=''.join([str(elem) for elem in password])
#print(final)
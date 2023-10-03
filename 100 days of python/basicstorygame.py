import time
air_left=100

print('''   ~;
                  ,/|\,
                ,/' |\ \,
              ,/'   | |  \
            ,/'     | |   |
          ,/'       |/    |
        ,/__________|-----' ,
       ___.....-----''-----/
       \                  /
   ~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^
     ~-^~^-`~^~-^~^`^~^-^~^`^~^-~^ ''')
waiver=input("Welcome travlers! its great to see you here! As a precaution have you signed the waiver?")
waiver=waiver.lower()
if(waiver=="yes"):
    print("ok awesome to hear that! since you've signed the waiver we can get started by getting your suit on and getting you in the water!")
    print("...")
    time.sleep(5)
    print("...")
    time.sleep(5)
    print("...")
    time.sleep(5)
    print("great now that you are all ready we can get you in the water! Just walk of the end of the boat. See you in a bit!")
    time.sleep(2)
    print(''')    O
                           (   o . O
                            )   () .
                           /  O   o
                         _.|._ o .()
              _         / _:_ \
             <_><)     |.(_"_).|
                __     _\. : ./_
             |><_'>   / |..:..| \
                     /_/ `---' \_\       ,
             ,  (.   \_)        \_)  \)-<
             _) \)~    \   T   /    ,(_)
            _/ -(-<    _)__|__(_    \_)-<~
             \)~ )-<  /....|....\  .~(_,_
            >(_ (_/   """"" """""    _\
         `-.__)__\_.----'`-.______.-'  `-.__
                                                ''')
    print("krrrcchhh...")
    time.sleep(2)
    print("Good we made it through to you! You are now free to explore the reef! Keep an eye out for anything cool! Captain out!")
    time.sleep(2)
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         .               `         /
                          .    ,../...       .
          .                .  /       `\  /  .
     \    .        o         < '  )     =<
     /\  .                    \ \      /  \   .  __
   >=)'>                       `'\'"'"'         /o \/
     \/ .    /         o              /,        \__/\    .:/
     /   .  /--\ /         /         <')=<     .      ,,///;,   ,;/
           ::::::::;;\\\
             \            \_/            .            ''\\\\\'' ';\
    (                      \              .   __
     )                                       <'_><          (
    (          (                ,/..          `              )
     )     (    )             <')   `=<                )    (
    (       )  (               ``\```                 (      )
_____)_____(____)______________________________________)____(________''')
    time.sleep(3)
    print("you see lots of fish and lots of corals and seaweed.\n You see in the distace a wrecked ship to your right\n you see to your left you see an undersea cave ")
    input("You can choose to go left or right which place would you like to explore?")
else:
    print("OH NO it looks like you didnt sign the waiver! We can't let you dive today!")
    time.sleep(1)
    print("GAME OVER")
import math
import random 
from Blackjacklogo import logo
game_start=input("Do you want to play a game of Blackjack? Type \'\y \'\ or  \'\ n \'\:").lower()
game_end=False
def draw_cards():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0,len(cards))]
if(game_start=="n"):
    exit()
else:
    while game_end==False:
        print(logo)
        player_hand=[]
        dealer_hand=[]
        bet = float(input("Please enter your bet amount"))
        for i in range(2):
            player_hand.append(draw_cards())
            dealer_hand.append(draw_cards())
        if(sum(player_hand)==21):
            if(sum(dealer_hand)==21):
                print("its a tie")
                play_again=input("Would you like to play again? y/n: ").lower()
                if(play_again=="n"):
                    exit()
                else:
                    game_end==False
        


import math
import random 
from Blackjacklogo import logo

def draw_cards():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def calc_score(hand):
    if sum(hand)==21 and len(hand)==2:
        return 0
    if 11 in hand and sum(hand)>21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
      
def reset(h1, h2):
    play_again=input("Would you like to play again? y/n: ").lower()
    if(play_again=="y"):
        h1.clear()
        h2.clear()
        return h1, h2, False
    else:
        return h1, h2, True
    
game_start=input("Do you want to play a game of Blackjack? Type y or n:").lower()
game_end=False
if(game_start=="n"):
    exit()
print(logo)
bet = float(input("Please enter your bet amount: $"))
player=[]
dealer=[]
if(len(player)<2):
        for i in range(2):
            player.append(draw_cards())
            dealer.append(draw_cards())

while game_end==False:
    print(player)
    print(dealer)
    u_score= calc_score(player)
    d_score = calc_score(dealer)
    if u_score==0 or d_score==0 or u_score>21:
        game_end=True
    hit=input("would you like to hit or stand? h/s: ").lower()
    if(hit=="h"):
        player.append(draw_cards())
    elif hit=="s":
        u_score=calc_score(player)
        if(sum(dealer)<15):
            dealer.append(draw_cards())
            d_score=calc_score(dealer)
        if(u_score>d_score):
            print("You win!")
            player, dealer, game_end= reset(player, dealer)
        else:
            print("You Lost")
            player, dealer, game_end= reset(player, dealer)


    




        


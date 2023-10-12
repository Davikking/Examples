from gavel import logo

print(logo)
moreBidders=True
silent_auction={}
while moreBidders:
    name = input("Please enter your name: ")
    price = int(input("please enter your bid amount:  "))
    silent_auction[name] = price
    bidsOver= input("Are there any more bidders? yes/no: ").lower()
    if(bidsOver=="no"):
        moreBidders=False
    print("\033[H\033[J", end="")
print(f"{max(silent_auction, key=lambda key: silent_auction[key])} is the winner")
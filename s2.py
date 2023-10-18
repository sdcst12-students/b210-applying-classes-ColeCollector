hand = ['AH']

print("The dealer's hand is ",end="")
for i in hand: 
    print(f"{i},",end=" ")



hand = ['AH','2H']

print("The dealer's hand is ",end="")
for i in hand: 
    print(i,end="")
    if len(hand) > 1 and (hand[len(hand)-1] != i):
        print(",",end="")
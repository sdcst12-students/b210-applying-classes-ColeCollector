


class game:

    def createDeck(self):
        import random
        ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        suits = ['C','D','H','S']
        deck = []
        
        for i in ranks:
            for n in range(0,4):
                deck.append(f"{i}{suits[n]}")

        random.shuffle(deck)
        
        return deck
    
    def value(self,hand):
        val = 0
        val1 = 0
        forbidden = ['A', 'K', 'Q', 'J', 'T']

        for i in range(0,len(hand)):
            if hand[i][0] not in forbidden:
                val = val + int(hand[i][0])
                val1 = val1 + int(hand[i][0])

            elif hand[i][0] == 'A':
                val = val + 1
                val1 = val1 + 11

            if hand[i][0] == 'Q' or hand[i][0] == 'K' or hand[i][0] == 'T' or hand[i][0] == 'J':
                val = val + 10
                val1 = val1 + 10

        if val == val1:
            return val
        
        else:
            return [val,val1]
        
    def busts(self,score):
        if score <= 21:
            return False
        else:
            return True
        
    def dealer(self,deck):

        dealer = [deck[0]]
        deck.pop(0)
        score = 0

        print(f"\nDealer's hand is {(dealer)[0]} with a value of {self.value(dealer)}")

        Done = False

        while Done == False:
            dealer.append(deck[0])

            try:
                deck.pop(0)
                if (self.value(dealer)) > 16:
                    score = self.value(dealer)
                    Done = True
            
            except:
                if self.value(dealer)[0] > 16:
                    score = self.value(dealer)[0]
                    Done = True

                elif self.value(dealer)[1] > 16:
                    score = self.value(dealer)[1]
                    Done = True

        return [ dealer , score , deck ]
    
    def decision(self):
        while True:
            choice = input("Would you like to hit or stand? ")
            if choice == "hit" or choice == "Hit":
                return True 
                
            elif choice == "stand" or choice == "Stand":
                return False
            
    def player(self,deck):
        hand = []
        score = 0
        Done = False

        hand.append(deck[0])
        deck.pop(0)
        
        print(f"\nYour hand is {hand[0]} with a value of {self.value(hand)}")
        
        while Done == False:

            if self.decision() == True:
                hand.append(deck[0])
                deck.pop(0)
                
                if self.value(hand) == 21:
                    break

                else:
                    print ("\033[A                                                  \033[A")
                    print ("\033[A                                                  \033[A")
                    print("Your hand is ",end="")

                    for i in hand: 
                        print(i,end="")
                        if len(hand) > 1 and (hand[len(hand)-1] != i):
                            print(", ",end="")

                    print(f" with a value of {self.value(hand)}")

                    try:
                        if (self.value(hand)) > 21:
                            score = self.value(hand)
                            Done = True

                    
                    except:
                        if self.value(hand)[0] > 21:
                            score = self.value(hand)[0]
                            Done = True


                        elif self.value(hand)[1] > 21:
                            score = self.value(hand)[1]
                            Done = True

            else:
                score = self.value(hand)
                Done = True
                

        return [ hand , score , deck ]
    
    def winner(self,dealerh,dealer,player):
        import time
        
        print(f"Dealer's hand is {(str(dealerh)[1:-1])}, with a value of {dealer}")

        #dealing with aces
        try:
            if player[0] < 22 and player[1] < 22:
                if player[0] > player[1]:
                    player = player[0]

                elif player[0] < player[1]:
                    player = player[1]

            elif player[0] < 22:
                player[0] = player

            elif player[1] < 22:
                player[1] = player

        except:
            pass

        if player > 21:
            print(f"\033[1;31;40mYou busted \033[0m")
        
        elif dealer == 21:
            print(f"\033[1;31;40mYou lose, dealer had blackjack \033[0m")
        
        elif player == 21:
            print(f"\033[1;32;40mYou win, you got blackjack! \033[0m")

        elif dealer > player and dealer < 21 :
            print(f"\033[1;31;40mYou lost, dealer had a higher value hand \033[0m")
        
        elif dealer < player and dealer < 21:
            print(f"\033[1;32;40mYou won, you had a higher value hand \033[0m")

        elif dealer > 21:
            print(f"\033[1;32;40mYou won dealer busted \033[0m")
        
        elif dealer == player:
            print(f"\033[1;35;40mIt's a draw \033[0m")
        print("\n\n\n")

        time.sleep(1)

    def __init__(self):
        while True:
            deck = self.createDeck()
            dealer = self.dealer(deck)
            player = self.player(deck)

            self.winner(dealer[0],dealer[1],player[1])
            pass


g = game()
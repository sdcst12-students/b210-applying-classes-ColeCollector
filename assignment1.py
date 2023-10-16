


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

        print(f"Dealer's hand is: {dealer} with a value of {self.value(dealer)}")

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
            choice = input("Would you like to hit or stand?")
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
        
        print(f"\nYour hand is {hand} with a value of {self.value(hand)}")

        while Done == False:

            if self.decision() == True:
                hand.append(deck[0])
                deck.pop(0)
                
                if self.value(hand) == 21:
                    break

                else:
                    print(f"\nYour hand is {hand} with a value of {self.value(hand)}")

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
    
    def winner(self,computerh,computer,playerh,player):
        print(f"Dealer's hand is {computerh}, with a value of {computer}")

        if player > 21:
            print(f"You busted")
        
        elif computer == 21:
            print("You lose, dealer had blackjack ")
        
        elif player == 21:
            print(f"You win, you got blackjack! ")
        
        elif computer > player and computer < 21 :
            print("You lost, dealer had a higher value hand")
        
        elif computer < player and computer < 21:
            print("You won, you had a higher value hand")

        elif computer > 21:
            print("You won dealer busted")
        
        elif computer == player:
            print("It's a draw")

    def __init__(self):
        while True:
            deck = self.createDeck()
            dealer = self.dealer(deck)
            player = self.player(deck)

            self.winner(dealer[0],dealer[1],player[0],player[1])

            pass






g = game()
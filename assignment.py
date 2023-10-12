#! python3

class game:
  
    def playerchoice(self):
        choice = 0
        global choices
        choices = {"rock":1,"papper":2,"scissors":3,"lizard":4,"spock":5}
        
        while choice not in choices:
            choice = input("\nWould you like to choose rock, papper, scissors, lizard or spock?\nYour choice: ")

        choice = choices[choice]
        return choice

    def winner(self):
        global choice
        global win
        global answer

        choice = self.playerchoice()
        answer = self.computerchoice()

        #draw
        if int(choice) == int(answer):
            win = "1"

        #if you choose rock
        elif (choice == 1 and answer == 2) or (choice == 1 and answer == 5):
            win = False

        elif (choice == 1 and answer == 3) or (choice == 1 and answer == 4):
            win = True

        #if you choose papper
        elif (choice == 2 and answer == 1) or (choice == 2 and answer == 4):
            win = True

        elif (choice == 2 and answer == 3) or (choice == 2 and answer == 5):
            win = False

        #if you choose scissors
        elif (choice == 3 and answer == 1) or (choice == 3 and answer == 5):
            win = False

        elif (choice == 3 and answer == 2) or (choice == 3 and answer == 4):
            win = True

        #if you choose lizard
        elif (choice == 4 and answer == 1) or (choice == 4 and answer == 3):
            win = False

        elif (choice == 4 and answer == 2) or (choice == 4 and answer == 5):
            win = True

        #if you choose spock
        elif (choice == 5 and answer == 1) or (choice == 5 and answer == 3):
            win = True

        elif (choice == 5 and answer == 2) or (choice == 5 and answer == 4):
            win = False

    def computerchoice(self):
        import random
        answer = random.randint(1,5)
        return answer

    def printwinner(self):
        global winstreak
        if win == True:
            print(f"\033[1;32;40mYou Won, I chose \033[1;37;40m{(list(choices.keys()))[answer-1]}")
            winstreak +=1
            print(f"\033[1;33;40mWinstreak \033[0m: {winstreak}")

        elif win == False:
            print(f"\033[1;31;40mYou lost, I chose \033[1;37;40m{(list(choices.keys()))[answer-1]}")
            winstreak = 0
            print(f"\033[1;33;40mWinstreak Lost \033[0m")

        elif win == "1":
            print(f"\033[1;35;40mIt's a draw we both chose \033[1;37;40m{(list(choices.keys()))[answer-1]}")
            winstreak = 0
            print(f"\033[1;33;40mWinstreak Lost \033[0m")

    def __init__(self):
        print('If you ever want to leave say "leave"')
        global winstreak
        winstreak = 0
        while True:
            self.winner()
            self.printwinner()  

# This is the only command allowed that is not in the class template. All code must be done there.
g = game()

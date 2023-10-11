#! python3

class game:
  import random
  
  choice = 0
  choices = {"rock":1,"papper":2,"scissors":3,"lizard":4,"spock":5}
  
  while choice not in choices:
    choice = input("\nWould you like to choose rock, papper, scissors, lizard or spock?\nYour choice: ")

  answer = random.randint(1,3)

  choice = choices[choice]

  #draw
  if choice == answer:
    print(f"It's a draw we both chose {(list(choices.keys()))[choice-1]}")

  #if you choose rock
  elif choice == 1 and answer == 2:
      print("You lost, I chose papper")

  elif choice == 1 and answer == 3:
      print("You won, I chose scissors")

  elif choice == 1 and answer == 4:
      print("You won, i chose lizard")

  elif choice == 1 and answer == 5:
      print("You lost, I chose spock")

  #if you choose papper
  elif choice == 2 and answer == 1:
      print("You won, I chose rock")

  elif choice == 2 and answer == 3:
      print("You lost, I chose scissors")

  elif choice == 2 and answer == 4:
      print("You won, I chose lizard")

  elif choice == 2 and answer == 5:
      print("You lost, I chose spock")

  #if you choose scissors
  elif choice == 3 and answer == 1:
      print("You lost i chose rock")

  elif choice == 3 and answer == 2:
      print("You won, i chose papper")

  elif choice == 3 and answer == 4:
      print("You won, I chose lizard")

  elif choice == 3 and answer == 5:
      print("You lost i chose spock")

  #if you choose lizard
  elif choice == 4 and answer == 1:
      print("You lost, I chose rock")

  elif choice == 4 and answer == 2:
      print("You won, I chose papper")

  elif choice == 4 and answer == 3:
      print("You lost, I chose scissors")

  elif choice == 4 and answer == 5:
      print("You won, I chose spock")

  #if you choose spock
  elif choice == 5 and answer == 1:
      print("You won, I chose rock")

  elif choice == 5 and answer == 2:
      print("You lost, I chose papper")

  elif choice == 5 and answer == 3:
      print("You won, I chose scissors")

  elif choice == 5 and answer == 4:
      print("You lost, I chose lizard")

  def __init__(self):
    pass


# This is the only command allowed that is not in the class template. All code must be done there.
g = game()

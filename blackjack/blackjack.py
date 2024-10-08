# main.py
import random
print("Welcome the game black jack. The goal of the game is to get as close to 21 as possible without going over 21(busting). You will be randomly be delt 2 card. You will then get to choose weather to stay or hit which is getting another card in hopes of getting closer to 21. After your turn the dealer will play.")
# start with while true loop and conditional to start playing
# then will use random to add 2 number 2 - 11 to a list called playerCards
# after printing will ask a for an input staying or hitting
# if stay move on to dealers turn if hitt append random card to playerCards
# write a conditional for the player busting by adding numbers in list and seeing if they are lower that 21
# now start doing a similar thiing to the dealers hand but the dealer hits when less then 17 but after they stay

start = input("press enter to start playing!")
if start == "":
  print("")
  
  while True:
    playerCards = []
    amount = 0
    for i in range(2):
      x = random.randint(2,11)
      playerCards.append(x)
      amount += x
    print("Here is your hand:")
    print(playerCards)
    while True:
      choice = input("Typer H to hit and S to stay: ")
      
      if choice == "H":
        increase = random.randint(2,11)
        playerCards.append(increase)
        print("Here is your hand:")
        print(playerCards)
        amount += increase 
        if amount > 21:
          print("you busted :(")
          break
      elif choice == "S":
        break
      else:
        print("please enter H or S")
    
    if amount <= 21:
      dealerCards = []
      dealerAmount = 0
      for i in range(2):
        y = random.randint(2,11)
        dealerCards.append(y)
        dealerAmount += y
      print("Here is the dealer's hand:")
      print(dealerCards)
      while True:
        if dealerAmount > 17:
          print("the dealer has finalized their hand")
          break
        else:
          print("The dealer has Hit")
          increaseDealer = random.randint(2,11)
          dealerCards.append(increaseDealer)
          print(dealerCards)
          dealerAmount += increaseDealer
          if dealerAmount > 21:
            print("The Dealer Busted. You win!")
            break
    if dealerAmount > 21:
      print("")
    elif amount > 21:
      print("")
    elif amount > dealerAmount:
      print("You win :)")
      print("")
    else:
      print("The dealer wins")
      print("")
    
    startAgain = input("press enter to play again!")
    if startAgain == "":
      print("")
    
  

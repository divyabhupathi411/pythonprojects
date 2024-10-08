# main.py
import random 

# make Grid
gridArray = []
for i in range(3):
  row = []
  for x in range(3):
    row.append("   ")
  gridArray.append(row)
  
# print grid function
def printGrid(gridArray):
  print(gridArray[0][0] + "|" + gridArray[0][1] + "|" + gridArray[0][2])
  print("---+---+---")
  print(gridArray[1][0] + "|" + gridArray[1][1] + "|" + gridArray[1][2])
  print("---+---+---")
  print(gridArray[2][0] + "|" + gridArray[2][1] + "|" + gridArray[2][2])

# player move function
def playerMove():
  row = input("pick a row to play: ")
  collum = input("pick a collum to play: ")
  gridArray[int(row)][int(collum)] = " O "
  printGrid(gridArray)

# random move
def randomMove():
  while True:
    row = random.randint(0,2)
    collum = random.randint(0,2)
    if gridArray[row][collum] != " O " and gridArray[row][collum] != " X ":
      gridArray[row][collum] = " X "
      break
  printGrid(gridArray)
  
# check for wins
def checkWins():
 
  if gridArray[0][0] == gridArray[1][1] == gridArray[2][2] and gridArray[0][0] != "   ":
    if gridArray[0][0] == " O ":
      print("O wins!")
      return False
      
    elif gridArray[0][0] == " X ":
      print("X wins!")
      return False
  
  if gridArray[0][2] == gridArray[1][1] == gridArray[2][0] and gridArray[0][2] != "   ":
    if gridArray[0][2] == " O ":
      print("O wins!")
      return False
      
    elif gridArray[0][2] == " X ":
      print("X wins!")
      return False
  
  for row in range(3):
    if gridArray[row][0] == gridArray[row][1] == gridArray[row][2]:
      if gridArray[row][0] == " O ":
        print("O wins!")
        return False
      
      elif gridArray[row][0] == " X ":
        print("X wins!")
        return False
        
  for collum in range(3):
    if gridArray[0][collum] == gridArray[1][collum] == gridArray[2][collum]:
      if gridArray[0][collum] == " O ":
        print("O wins!")
        return False
      
      elif gridArray[0][collum] == " X ":
        print("X wins!")
        return False
  # add row checks + stuff in while look at end
    
    

# loop for game:
printGrid(gridArray)
flip = random.randint(1,2)

if flip == 1:
  print("The coin flip shows that you (X) will go first!")
  input("Press Enter to begin!")
  
  while True:
    randomMove()
    if checkWins() == False:
      break
    playerMove()
    if checkWins() == False:
      break
  
elif flip == 2:
  print("The coin flip shows that you (O) will go first!")
  input("Press Enter to begin!")
  
  while True:
    playerMove()
    if checkWins() == False:
      break
    randomMove()
    if checkWins() == False:
      break





# main.py
import random
SampleList = [4,0,7,1,5,3]

def suffle(ExList,n):
  for i in range(n):
    x = random.randint(0,len(ExList)-1)
    y = random.randint(0,len(ExList)-1)
    temp = ExList[x]
    ExList[x] = ExList[y]
    ExList[y] = temp
  return ExList
  
def partition(ExList, pivot):
  equalList = []
  lessList = []
  greaterList = []
  for i in range(len(ExList)):
    if ExList[i] == pivot:
      equalList.append(ExList[i])
    elif ExList[i] < pivot:
      lessList.append(ExList[i])
    else:
      greaterList.append(ExList[i])
  return equalList, lessList, greaterList



def quicksort(ExList):
  if len(ExList) <= 1:
    return ExList
  equalList, lessList, greaterList = partition(ExList,ExList[random.randint(0,len(ExList)-1)])
  x = quicksort(lessList)
  y = quicksort(greaterList)
    
  return x + equalList + y

print(quicksort(suffle(SampleList,10)))



  

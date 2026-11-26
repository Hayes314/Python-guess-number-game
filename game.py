import random

playerans=0

LowestNo=int(input("The lowest number is "))
HighestNo=int(input("The highest number is "))

while LowestNo==HighestNo:
  print("!"*50)
  print("lowest number cannot be same to highest nuber!")
  LowestNo=int(input("The lowest number is "))
  HighestNo=int(input("The highest number is "))

print("="*50)

FinalAns = random.randint(LowestNo , HighestNo)



while not playerans == FinalAns:

 playerans=int(input("Your answer is "))

 if playerans < FinalAns:

  if LowestNo<playerans:
   LowestNo=playerans


  print("Too low!")
  print("-"*50)
  print(f"The number range is {LowestNo}-{HighestNo}")
  #biger^

 if playerans > FinalAns:

  if HighestNo>playerans:
   HighestNo=playerans


  print("Too high!")
  print("-"*50)
  print(f"The number range is {LowestNo}-{HighestNo}")
  #smaller%



#endgame
print("#"*50)
print(f"Good ! The answer is {FinalAns}")

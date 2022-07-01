import random

num = random.randint(1,100)
guess = int(input("guess the number:"))
attempt = 1
while(True):
  if(guess>num):
    guess=int(input("guess another number.This is too big:"))
    attempt+=1
  elif (guess<num):
     guess = int(input("guess another number.This is too small:"))
     attempt+=1
  else:
    print(f"Yeah thats the number! You guessed it right in {attempt} attempts")
    break



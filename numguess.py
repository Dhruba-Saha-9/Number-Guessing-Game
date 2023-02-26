import random
a=random.randint(1,101)
b = int(input("Guess the number between 1 to 100 : "))
guess=0
while guess>=0:


  if b==a :
       print("Congratulations u got the correct number ",a)
       break
  elif b>a :
       b = int(input("Enter a lower number : "))
  else:
       b = int(input("Enter a higher number : "))

  guess += 1
print("And your number of guesses were ",guess)

import random

random_number = random.randint(1,100)

while True:
                   guess_number = int(input("Guess the number: "))
                   if guess_number >  random_number :
                                   print("A little shorter.")
                   elif guess_number < random_number :
                                   print("A little bigger")
                   else:
                                  print("Correct!")
                                  break
                                
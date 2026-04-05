import random

comp_score = 0
user_score = 0


print("                              Rock, Paper and Scissors")
print("if you want to stop playing, type STOP")
choices = ["Rock", "Paper", "Scissors"]
 


while True:
     comp_guess = random.choice(choices)
     comp_guess = comp_guess.lower()
     
     user_guess = input("What do you want to choose?:    ")
     
     user_guess = user_guess.lower()
     
     print(f"I choose {comp_guess}")
     
     if comp_guess == user_guess:
         print("Its a draw!")
     elif user_guess == "rock" and comp_guess == "paper":
         print("You lose")
         comp_score += 1
     elif user_guess == "paper" and comp_guess == "scissors":
             print("You lose")
             comp_score += 1
     elif user_guess == "scissors" and comp_guess == "rock" :
             print("You lose")
             comp_score += 1
     elif user_guess == "rock" and comp_guess == "scissors":
             print("You win!")
             user_score += 1
     elif user_guess == "paper" and comp_guess == "rock":
             print("You win!")
             user_score += 1
     elif user_guess == "scissors" and comp_guess == "paper":
             print("You win!")
             user_score += 1
     elif user_guess == "stop":
             print(f"Your score: {user_score}")
             print(f" Computer score: {comp_score}")
             if user_score > comp_score:
                 print("You win!")
             elif user_score < comp_score:
                 print("You lose, computer wins.")
             elif user_score == comp_score:
                 print("It's a draw.")
                 break
    
     else:
             print("Please fix your typing mistake.")
             

         
####guess the number betwen 1 to 100. Choose a difficulty. Try: easy or hard###
###according to the difficulty how many times user can guess will be set.
### this is also binary search algorithm
###easy level = 10 attempts||hard level == 5 attempts|| 
#when the guessed number is high print a warning statement || when the number is low print another statement

import random


#set the global variables
n=random.randint(1,100)
easy_attempts = 10
hard_attempts = 5
users_attempt = 0

def guessing(guess_number, n, user_attempt):
  if guess_number > n:
    print("too high!")
    return users_attempt - 1
  elif guess_number < n:
    print("too low!")
    return users_attempt - 1
  elif guess_number == n:
    print("correct")

#setting difficulty level
def set_difficulty():
  level = input("type easy or hard: ")
  if level == "easy":
    return easy_attempts
  else:
    return hard_attempts

#function to compare between guessed number and the actual number

n=random.randint(1,100)

#track the number of attempts remaining
def game(n, users_attempt, guess_number):
  print("Welcome to the number guessing game")
  print("think a number between 1 to 100")
  users_attempt = set_difficulty()

  print(f"you have {users_attempt} attempts left")

  #repeat the process if the number is wrong
  guess_number = 0
  while guess_number != n:
    guess_number= int(input("Make a guess: "))
    guessing(guess_number, n)

game(n, users_attempt, guess_number)

        
           
        
    

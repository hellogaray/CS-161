# Author: Leonel Garay
# Date: 10/11/2019
# Description: User inputs number to be guessed, 4 attempts are allowed at guessing the number.
print("Enter the number for the player to guess.")
user_choice = int(input())  # Ask user for the number to be guessed.
print("Enter your guess.")
attempts = 0  # User has 4 attempts before program ends.
user_guess = user_choice - 1
while user_guess != user_choice:
    user_guess = int(input())
    attempts = attempts + 1
    if (user_guess > user_choice):  # if guess is higher then user_choice
        print("Too high - try again:")
    if (user_guess < user_choice):  # if guess is lower then user_choice
        print("Too low - try again:")
    if (user_guess == user_choice):  # if guess is correct
        if (attempts == 1):  # if correct in first attempt then congratulate
            print("You guessed it in 1 try.")
        else: # if guess is correct after first try, then congratulate with number of attempts
            print("You guessed it in", attempts, "tries.")
    if (attempts == 4):
        break

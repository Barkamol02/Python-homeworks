# Number Guessing Game Create a simple number guessing game.

# The computer randomly selects a number between 1 and 100.
# If the guess is high, print "Too high!".
# If the guess is low, print "Too low!".
# If they guess correctly, print "You guessed it right!" and exit the loop.
# The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.
# Hint: Use Python’s random.randint() to generate the number.

import random

while True:
    number = random.randint(1, 100)
    attempts = 10
    while attempts>0:
        guess = int(input("enter your guess "))
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print("You guessed it right!")
            break  
        attempts -=1 
    if attempts == 0:
        print("You lost. Want to play again?")
    play_again = input("Type 'Y', 'YES', 'y', 'yes', or 'ok' to restart: ").strip().lower()
    if play_again not in ['y', 'yes', 'ok']:
        break
    else:
        print("Starting a new game!")         

 

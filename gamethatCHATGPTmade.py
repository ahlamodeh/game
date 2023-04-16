# -*- coding: utf-8 -*-
"""
this is a game that ChatGPT made
"""
import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

# Set initial values for guesses and game status
guesses = 0
is_game_over = False

print("Welcome to the Guessing Game!")
print("Guess the number between 1 and 100.")

# Loop until the game is over
while not is_game_over:
    # Ask the player for their guess
    guess = int(input("Enter your guess: "))
    guesses += 1
    
    # Compare the guess with the target number
    if guess < target_number:
        print("Higher!")
    elif guess > target_number:
        print("Lower!")
    else:
        print("Congratulations! You guessed the correct number in", guesses, "guesses!")
        is_game_over = True
        
        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            # Generate a new target number and reset guesses
            target_number = random.randint(1, 100)
            guesses = 0
            is_game_over = False
        else:
            print("Thank you for playing. Goodbye!")

# Guess a number game where computer will select a random number and we have to guess it.

import random

def guess_number(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {10}: "))
        if guess < random_number:
            print("Guess again. Too low.")
        elif guess > random_number:
            print("Guess again. Too high.")
    print(f"You guessed the number {random_number} successfuly!!")

guess_number(10)

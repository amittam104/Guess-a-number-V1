# Guess a number where user will select a random number and program (computer) will guess it.
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low <= high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is the {guess} too high(H) or too low (L) or correct (C): ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Congrats! The computer guessed the {guess} correctly.")


computer_guess(10)
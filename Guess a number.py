# Guess a number game where computer will select a random number and we have to guess it.

import random

# def guess_number(x):
#     random_number = random.randint(1, x)
#     guess1 = 0
#     while guess1 != random_number:
#         guess1 = int(input(f"Guess a number between 1 and {10}: "))
#         if guess1 < random_number:
#             print("Guess again. Too low.")
#         elif guess1 > random_number:
#             print("Guess again. Too high.")
#     print(f"You guessed the number {random_number} successfuly!!")

# guess_number(10)



# Guess a number where user will select a random number and program (computer) will guess it.
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

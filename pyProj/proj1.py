# guess a random number

import random

def guessUnder(x):
    guessUnder = random.randint(1, x)
    guess = 0

    while guess != guessUnder :
        guess = int(input(f"guess a number between the 0 and {x} : "))
        if guess < guessUnder:
            print("You have chosen a smaller number!")

        elif guess > guessUnder:
            print("You have chosen a larger number")
    
    print("You have hit the jackpot!!!")

guessUnder(100)
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

# now let the computer guess the number in your mind

def guessBelow(x):
    start = 1
    end = x
    instructions = ''

    while instructions != 'c':
        if start != end:
            guess = random.randint(start, end)
        else:
            guess = start

        instructions = input(f"The number {guess} is too high(H), too low(L) and correct(C) : ")
        if instructions == 'h':
            end = guess - 1
        elif instructions == 'l':
            low = guess + 1

    print("Computer has guessed the correct number")

guessBelow(1000)

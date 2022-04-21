# Rock Paper Scissors

import random


def game():
    user = input("'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "Game tied !!!"

    if is_win(user, computer):
        return "You Won!"

    return 'You Lost !!!'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(game())

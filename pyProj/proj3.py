import random
from allWords import words
import string


def validWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = validWord(words)
    wordAlpha = set(word)
    alphabet = set(string.ascii_uppercase)
    usedAlpha = set()

    while len(wordAlpha) > 0:
        print("You have used these letters : ", ' '.join(usedAlpha))
        wordList = [letter if letter in usedAlpha else '-' for letter in word]
        print('Current Word: ', ' '.join(wordList))
        userLetter = input("Guess a letter: ").upper()

        if userLetter in alphabet - usedAlpha:
            usedAlpha.add(userLetter)
            if userLetter in wordAlpha:
                wordAlpha.remove(userLetter)

        elif userLetter in usedAlpha:
            print('Already used, please try again.')

        else:
            print('Invalid character, Please try again.')


hangman()

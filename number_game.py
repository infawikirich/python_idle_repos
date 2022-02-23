"""
script file: number_game.py

purpose: This program create a guess game by asking the
user to enter a number.

author: Mr. Asiamah

date: 03/09/21

"""

import random


def numberGame():
    # choose a random number between 1 and 100
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100")

    guess = int(input("What's your guess? "))

    while guess:

        if number == guess:
            print("That's correct! The number was ", number)
            break
        elif number < guess:
            print("Nope. Higher")
        else:
            print("Nope.Lower")

        guess = int(input("What's your guess? "))


numberGame()

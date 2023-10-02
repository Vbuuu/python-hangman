import sys
from getpass import getpass

from helper.inputHelper import getBoolInput

bot = getBoolInput("Playing against a friend?", True)
guesses = ""
wrongGuesses = []

if bot:
    print("[Player One] Please enter in the guess word \n")
    guessWord = getpass()

else:
    guessWord = "Cheesecake"

while True:
    failed = 0
    for char in guessWord:
        if char.lower() in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1

    wrongGuesses = set(guesses) - set(guessWord)
    guessChar = input(f" {'Wrong chars: '+''.join(map(str, wrongGuesses))if len(wrongGuesses) > 0 else ''}  Next char?")
    guesses += guessChar.lower()

    if failed <= 0:
        print("You won!")
        break

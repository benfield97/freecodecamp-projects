import pyinputplus as pyip
import random

number = 5  # andom.randint(1, 50)

attempts = 0

while True:

    guess = pyip.inputNum(prompt="Guess a number between 1 and 50 ", min=1, max=50)

    attempts += 1

    if number != guess:
        print('Wrong!')
        choice = None
        while choice != "N":
            choice = input("Keep Playing? (Y/N) ").upper()
            if choice == "Y":
                break

        if choice == "N":
            print("Bye")
            break

    else:
        print(f'Nice! You guessed it in {attempts} attempts')
        break

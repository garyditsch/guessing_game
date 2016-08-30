# Game mechanics:
# 1. Ask player how many guesses they will need
    ## Ask player for the range that they want the number to be
    ### Ask player how much they are willing to wager that they will win
# 2. Ask player for their first guess
# 3. Generate random number
# 4. Evaluate if player won or lost
# 5. Determine if player has more attempts available
# 6. Tell player if they were higher or lower than the answer
# 7. End game or go to next round

## Game Setup ##

import random

name = input("Enter your name: ")
needed_guesses = int(input("How many guesses do you need? "))
difficulty = int(input("How high are you willing to try? "))
answer = random.randrange(0, difficulty)

## Game Play ##

for chance in range(needed_guesses):
    guess = input("\nWhat is your guess? ")
    if guess == " " or not guess.isdigit():
        print("\nis an invalid option, please try again")
    elif int(guess) == answer:
        print("\nCongrats " + name + " You win!")
        break
    elif chance < needed_guesses - 1:
        if int(guess) < answer:
            print("\nToo Low, Try Again")
        else:
            print("\nToo High, Try Again")
    else:
        print("\nSorry " + name + " You lose!!")

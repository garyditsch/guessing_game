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

# Create a game class:
# a. name of player
# b. difficulty of game
# c. number of guesses they want to take
# d. generate random number to get answer to game

# Create a play class:
# a. ask player for their guess
# b. evaluate if player won, lost or has another turn
# c. tell player if they were higher or lower than the answer
# d. end game 

import random

class Game():
    """ Has attributes: name, difficulty, guesses, answer """
     
    def __init__(self):
        """Return a game object whose name is *name*, default
        difficulty is 10, default guesses is 5 and answer is *answer* """
        self.get_name()
        self.get_difficulty()
        self.get_guesses()
        self.get_answer()
        self.get_wager()
        self.chance = 0

    def get_name(self):
        self.name = input("Enter your name: ")
        return self.name

    def get_difficulty(self):
        self.difficulty = int(input("How high are you willing to try? "))
        return self.difficulty

    def get_guesses(self):
        self.guesses = int(input("How many guesses do you need? "))
        return self.guesses

    def get_wager(self):
        self.wager = int(input("How much money are you willing to bet? "))
        return self.guesses

    def get_answer(self):
        self.answer = random.randrange(0, self.difficulty)
        return self.answer

x = Game()
# print(x.guesses)
# print(x.answer)
# print(x.difficulty)
# print(x.name)
# print(x.chance)
# print(x.wager)

while x.chance < x.guesses:
    guess = input("\nWhat is your guess? ")
    x.chance += 1
    if guess == " " or not guess.isdigit():
        x.chance -= 1
        print("\nis an invalid option, please try again")
    elif int(guess) == x.answer:
        print("\nCongrats " + x.name + " You win!")
        print("\nLooks like we owe you {} dollars".format(x.wager))
        break
    elif x.chance < x.guesses:
        if int(guess) < x.answer:
            print("\nToo Low, Try Again")
            print("\nThat was guess: {} . You have {} guesses left.".format(x.chance, x.guesses - x.chance))
        else:
            print("\nToo High, Try Again")
            print("\nThat was guess: {} . You have {} guesses left.".format(x.chance, x.guesses - x.chance))
    else:
        print("\nSorry " + x.name + " You lose!!")
        print("\nLooks like you own us {} dollars".format(x.wager))

# Hangman Game
""" 
- begin the game with options - start , exit
- words list
- get a guess
- try few guess
-check guess
-if wrong continue loop until no of try
-if all correct - break
"""
import random

#words list for the game

words = ['happy', 'winter','dublin','buzz','ring','python','quartz','jogging','jiujitsu','queue','galaxy','fancy',
    'frazzled','syndrome','awkward']
game_words = random.choice(words)

"""begin the game with option to start and exit with wecome message"""
def welcome_message():
    while True:
        name = input('Please enter your Name:\n')
        print(f'Hello {name}, Welcome to Hangman Game! \n')
        break
    return name
welcome_message()


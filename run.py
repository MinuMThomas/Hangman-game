
import random
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
welcome_message()

"""game instructions and option to enter the game
 the options will give user to start or exit the game
 """
def game_instructions():
    while True:
        options = input('please select option: \n * Y - start \n * N - exit \n').upper()
        try:
            if not options.upper():
                print('must enter uppercase letter')
        except:
            print('you must enter Y or N please try again')                
        if options.upper() == "Y":
                print('- The computer will generate random word and \n'
                'you have to guess the letters in the word and have 6 chances. \n'
                '- type the letter and hit enter button. \n'
                '- if it is wrong guess you will loose a chance.\n'
                '- Good Luck!')
                yes_input = input('press enter to begin the game')
                if yes_input == '':
                    game()
                else:
                    print('sorry you pressed wrong key')
        else:
            options.upper() == 'N'
            print('thanks for trying, please come back later')          
            break       
game_instructions()

"""game function, enter letter check it is correct or not
   count the wrong entry , show the result"""

def game():
    





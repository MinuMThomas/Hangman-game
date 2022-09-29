
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
                print('option must be alphabet')
        except:
            print('you must enter Y or N please try again')
                         
        if options.upper() == "Y":
                print('- The computer will generate random word and \n'
                'you have to guess the letters in the word and have 6 chances. \n'
                '- type the letter and hit enter button. \n'
                '- if it is wrong guess you will loose a chance.\n'
                '- Good Luck!')
                yes_input = input('press enter go back to main menu')
                if yes_input == '':
                    pass
                else:
                    print('sorry you pressed wrong key')
        else:
            options.upper() == 'N'
            print('thanks for trying, please come back later')          
            break 
        
game_instructions()




"""def game_instruction():
    while True:
print = ('welcome to play HANGMAN GAME \n *')
print = ('please select option: \n *')
print =  ('y - start \n *')
print = ('n - exit \n')
def start_game():  
    options = None
    options = input('enter your option: ')
    if options == y:
        print("Exiting the game")
    elif options == n:
            
        print('start the game')
    else:
        print('invalid entry, please try again')    
        
start_game()"""

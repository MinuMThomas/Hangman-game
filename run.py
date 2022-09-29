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
#hangman graghic with different stages for number of guess 
def hangman_image():
    graphics = ['''
     +---+
        |
        |
        |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
       |
      ===''', '''
   +---+
    O   |
   /|\  |
        |
      ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
   +---+
    O   |
   /|\  |
   / \  |
       ==='''
    ]

#words list for the game

"""game function, enter letter check it is correct or not
   count the wrong entry , show the result"""

def hangman_game():
    word = None
    guess = None

    words_list = ['happy', 'winter','dublin','buzz','ring','python','quartz','jogging','jiujitsu','queue','galaxy','fancy',
    'frazzled','syndrome','awkward']
    word = random.choice(words_list)


guessed_letters = []
wrong_guess = []
chances = 6
counting_hangman = -1
print("Let's play the game")
print(hangman_image())
while chances > 0:
        output = ''
for alphabet in word:
    if alphabet in guessed_letters:
        output += alphabet
    else:
        output += '_'    
if output == word:
    break
      
guess = input('please guess a letter or word: ').lower()

if guess in wrong_guess:
        print('you already guessed letter',guess)
            
elif guess in word and guess.lower():
            guessed_letters.append(guess)
       
else:
        counting_hangman = counting_hangman + 1
        chances = chances - 1
        wrong_guess.append(guess)
        print(hangman_image[counting_hangman])
if chances > 0:
        print('correct word')
else:
        print('sorry wrong word, try again')                


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
                    hangman_game()
                else:
                    print('sorry you pressed wrong key')
        else:
            options.upper() == 'N'
            print('thanks for trying, please come back later')          
            break       
game_instructions()







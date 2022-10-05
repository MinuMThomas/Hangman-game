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


def hangman_image():

    """
    hangman graghic with different stages for number of guess
    """

    global graphic_man
    graphic_man = ['''
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
       ===''']


def welcome_message():

    """welcome message along with entering user name input"""

    print('██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██')
    print('██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██')
    print('███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██') 
    print('███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██')
    print('██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██')
    print('██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████\n')

    name = input('\n Please enter your Name:\n')    
    print(f'Hello {name}, Welcome to Hangman Game! \n')


welcome_message()


def list_of_words():

    """
    list of words included with four types easy,  medium and hard
    user can choose level to play
    """
    global word

    word_easy = ['baby', 'back', 'bad', 'bag', 'ball''call', 'can', 
                 'candle', 'cap', 'car', 'card', 'care', 'ear', 'early',
                 'earn', 'earth', 'east', 'easy', 'jelly', 'job', 'join']
    word_medium = ['force', 'foreign', 'forest', 'forget', 'forgive', 'example'
                   'except', 'excited', 'exercise', 'expect', 'develop', 'die',
                   'different', 'difficult', 'dinner', 'direction']
    word_hard = ['chronological', 'lacrosse', 'copyright', 'glamorous', 
                 'unforeseen', 'glamorous', 'vengeance', 'optimistic', 
                 'noticeable', 'vengeance', 'consensus', 'recollection']
    
    print(' Please choose a level and enter it to begin the game !!\n'
          '\n* EASY\n \n* MEDIUM\n \n* HARD \n')
    level_of_difficulty = input('\n')
    
    if level_of_difficulty == 'EASY':
        print("\n you choose 'EASY' level")
        word = random.choice(word_easy).upper()
        
    elif level_of_difficulty == 'MEDIYUM':
        print("\n you choose 'MEDIUM' level")
        word = random.choice(word_medium).upper()
    elif level_of_difficulty == 'HARD':
        print("\n you choose 'HARD' level")
        word = random.choice(word_hard).upper()
    else:
        print('\n Enter the level in BIG letters!!\n')
        print('==================================')
        list_of_words()


def hangman_game():

    """
    game function, enter letter check it is correct or not
    count the wrong entry , show the result
    begin the game with option to start and exit with welcome message
    """

    global graphic_man
    hangman_image()
    guessed_letters = []
    wrong_guess = []
    chances = 7
    counting_hangman = -1
    alphabet = input
    
    while chances > 0:
        output = ''
        for alphabet in word:
            if alphabet in guessed_letters:
                output += alphabet
            else:
                output += '_ '
        if output == word:
            break
        print('===================================')
        print('===================================')
        print('Guess the word: ', output)
        print(chances, " lives left")
        
        guess = input().upper()
        
        if len(guess) != 1:
            print(' Please enter only one letter.')
        elif guess in guessed_letters or guess in wrong_guess:
            print(' Already guessed', guess)
        elif guess in word:
            print(' Awesome Job! You guessed the correct letter!\n')
            guessed_letters.append(guess)
        else:
            print(' Sorry! You have guessed a wrong letter!')
            counting_hangman = counting_hangman + 1
            chances = chances-1
            wrong_guess.append(guess)
            print(graphic_man[counting_hangman])

    if chances > 0:
        print(f" You guessed it right, the word is {word} !!!")
        print('======================================')
    else:
        print(' Sorry run out of chances. Try again.')
        print('======================================')              


def game_instructions():

    """
    game instructions and option to enter the game
    the options will give user to start or exit the game until 
    user's input is y or n.
    """

    while True:
        options = input(' please select option:\n\n' 
                        '* YES - start \n\n * NO - exit\n\n')               
        if options == "YES":
            print(' - The computer will generate random word \n\n'
                  ' - you have to guess the letters in the word\n\n'
                  ' - type the alphabet in the word and hit enter button\n\n'
                  ' - you have 6 chances\n\n'
                  ' - if it is wrong guess you will loose a chance\n\n'
                  ' - Good Luck!\n')
            list_of_words()
            hangman_game()
        elif options == 'NO':
            print('\n Thanks for trying, please come back later\n')          
            break
        else:
            print('\n Sorry please enter YES or NO in big letters')
            continue      


game_instructions()


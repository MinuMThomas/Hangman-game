import random
import os
import time
import sys


def hangman_image():

    """
    hangman graghic with different stages
    grapic image will show when input is wrong
    """
    global graphic_man

    graphic_man = ["""
    +---+
        |
        |
        |
      ===== """, """
    +---+
     O  |
        |
        |
      ===== """, """
    +---+
    O   |
    |   |
        |
      ===== """, """
    +---+
    O   |
   /|   |
        |
      ===== """, """
    +---+
    O   |
   /|\  |
        |
      ===== """, """
    +---+
    O   |
   /|\  |
   /    |
      ===== """, """
    +---+
    O   |
   /|\  |
   / \  |
      ===== """]


def clear_window():
    """
    Clears the game window
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome_message():

    """welcome message along with entering user name input"""

    print(' ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██')
    print(' ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██')
    print(' ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██')
    print(' ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██')
    print(' ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██')
    print(' ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████\n')

    while True:
        name = input('\n Please enter your Name:\n')
        clear_window()
        if not name.isalpha():
            print(' Please enter a name')
        else:
            print(f'Hello {name}, Welcome to Hangman Game! \n')
            break


welcome_message()


def list_of_words():

    """
    list of words included with four types easy,  medium and hard
    user can choose level to play
    """
    global word
    word_easy = ['baby', 'back', 'bad', 'bag', 'ball', 'call', 'can',
                 'candle', 'cap', 'car', 'card', 'care', 'ear', 'early',
                 'earn', 'earth', 'east', 'easy', 'jelly', 'job', 'join']
    word_medium = ['force', 'foreign', 'forest', 'forget', 'forgive', 'example'
                   'except', 'excited', 'exercise', 'expect', 'develop', 'die',
                   'different', 'difficult', 'dinner', 'direction']
    word_hard = ['chronological', 'lacrosse', 'copyright', 'glamorous',
                 'unforeseen', 'glamorous', 'vengeance', 'optimistic',
                 'noticeable', 'vengeance', 'consensus', 'recollection']
    print(' \nPlease choose a level and enter it to begin the game !!\n'
          '\n* EASY\n \n* MEDIUM\n \n* HARD \n')
    level_of_difficulty = input('\n').lower()
    if level_of_difficulty == 'easy':
        print("\n you choose 'EASY' level")
        word = random.choice(word_easy).upper()
        clear_window()
    elif level_of_difficulty == 'medium':
        print("\n you choose 'MEDIUM' level")
        word = random.choice(word_medium).upper()
        clear_window()
    elif level_of_difficulty == 'hard':
        print("\n you choose 'HARD' level")
        word = random.choice(word_hard).upper()
        clear_window()
    else:
        print('\n Enter the level you wish to play!!\n')
        print('==================================')
        clear_window()
        list_of_words()


def restart_game():

    """
    function for restart the game
    if user wants to play game then enter yes or
    any other key to exit and game will exit
    """

    print("\n Would you like to play again?\n")
    play_again = input(
        " Please enter YES to play, any other key to exit the game \n\n")
    if play_again.lower() == "yes":
        clear_window()
        game_instructions()
    else:
        print("Thank you for playing the game\n\n")
        sys.exit()


def hangman_game():

    """
    game function, enter letter check it is correct or not
    count the wrong entry , show the result
    begin the game with option to start and exit with welcome message
    """
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
        print(' Guess the word: ', output)
        print(chances, 'lives left')
        guess = input(" ").upper()
        if len(guess) != 1:
            clear_window()
            print(' \nPlease enter only one letter.\n')
            print(graphic_man[counting_hangman])
        elif not guess.isalpha():
            clear_window()
            print(' \nPlease enter only alphabet\n')
            print(graphic_man[counting_hangman])
        elif guess in guessed_letters or guess in wrong_guess:
            clear_window()
            print(' \nAlready guessed\n', guess)
            print(graphic_man[counting_hangman])
        elif guess in word:
            clear_window()
            print(' \nAwesome Job! You guessed the correct letter!\n')
            guessed_letters.append(guess)
            print(graphic_man[counting_hangman])
        else:
            clear_window()
            print(' \nSorry! You have guessed a wrong letter!\n')
            counting_hangman = counting_hangman + 1
            chances = chances-1
            wrong_guess.append(guess)
            print(graphic_man[counting_hangman])

    if chances > 0:
        print(f" You guessed it right, the word is {word} !!!")
        print('======================================')
        time.sleep(0.5)
        restart_game()
        clear_window()
    else:
        print(' Sorry! run out of chances. Try again.')
        print('======================================\n')
        time.sleep(0.5)
        restart_game()
        clear_window()


def game_instructions():

    """
    game instructions and option to enter the game
    the options will give user to start or exit the game until
    user's input is YES or NO.
    """

    while True:
        options = input(' please select an option:\n\n'
                        '* 1 - Start \n* 2 - Instructions\n'
                        '* 0 - Exit \n\n')
        if options == '1':
            clear_window()
            list_of_words()
            hangman_game()
        elif options == '2':
            clear_window()
            print('\n Game Instructions\n')
            time.sleep(0.5)
            print(' - The computer will generate random word \n\n'
                  ' - you have to guess the letters in the word\n\n'
                  ' - type the alphabet in the word and hit enter button\n\n'
                  ' - you have 7 chances\n\n'
                  ' - if it is wrong guess you will loose a chance\n\n'
                  ' - Good Luck!\n')
            time.sleep(6)
            clear_window()
            list_of_words()
            hangman_game()
            clear_window()
        elif options == '0':
            clear_window()
            print('\n Thanks for trying, please come back later\n')
            sys.exit()
        else:
            clear_window()
            print('\n Sorry please enter 1, 2 or 0\n')


game_instructions()

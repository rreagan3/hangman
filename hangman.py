#!/usr/bin/env python3

import os
import random
from termcolor import colored
import time

stages = ["""






""",
          """






_________""",
              """
|
|
|
|
|
|
_________""",
              """
______
|    |
|
|
|
|
_________""",
              """
______
|    |
|    O
|
|
|
_________""",
              """
______
|    |
|    O
|    |
|
|
_________""",
              """
______
|    |
|    O
|   /|
|
|
_________""",
              """
______
|    |
|    O
|   /|\\
|
|
_________""",
             """
______
|    |
|    O
|   /|\\
|   /
|
_________""",
             """
______
|    |
|    O
|   /|\\
|   / \\
|
_________"""]

def hangman():

    # initialize some stuff...
    word = ''
    num_lines = 0
    wrong_letters = []

    # this uses the posix list of words stored at /usr/share/dict/words
    with open('/usr/share/dict/words','r') as f:
        # count the number of words
        num_lines = sum(1 for line in f if line.rstrip())

    # select a random line in the file of words
    word_line = random.randrange(num_lines)

    # get the word from that line
    with open('/usr/share/dict/words', 'r') as f:
        for i, line in enumerate(f):
            if i==word_line:
                word = line.strip().lower()
                break

    # make a board as long as the word
    board = list('_'*len(word))

    # be polite
    print("Welcome to Hangman")

    # play the game until you've accumulated enough wrong guesses
    # that you get hung
    while len(wrong_letters) < len(stages)-1:
        # clear the garbage out of the way
        cls()
        # print the hangman board
        print(stages[len(wrong_letters)])

        # print the list of wrong letters guessed so far
        print("Wrong letters: "+', '.join(wrong_letters))
        # print the board
        print('\nWord: '+' '.join(board))

        # get user input
        char = input('Guess a letter: ').lower()

        # this is for... uh, debugging... yeah...
        if char == "cheat":
            print(word)
            time.sleep(1)
            continue

        # only let the user input 1 letter at a time
        elif len(char) != 1:
            print("only one letter, please!")
            continue

        # check if that one character is in the the word
        elif char in word:
            # replace the underscore with the letter
            for i, x in enumerate(word):
                if x==char: board[i] = char

            # if the board is the same as the word, the user wins
            if ''.join(board) == word:
                print("You Win! The word was %s!" % word)
                # winning returns True
                return True
        else:
            # if the char isn't in the word, then put that char in the wrong
            # letters list and continue
            if char not in wrong_letters:
                wrong_letters.append(char)

    # if we exit that while-loop, then we've been hung. print the hangman in
    # red, then reveal the word and return False.
    cls()
    print(colored(stages[len(stages)-1], 'red'))
    print("You lose. The word was: %s\n" % word)
    return False


def cls():
    if os.name == 'posix': os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'): os.system('CLS')
    else: print('\n'*15)

if __name__ == '__main__':
    wins = 0
    games = 0
    play_again = True
    while play_again:
        wins += (0,1)[hangman()]
        games += 1
        print('Record: %i and %i' % (wins, games - wins))
        msg = input("Want to play another game? ")

        play_again = msg.lower() in ('yes', 'y')



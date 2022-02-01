import random
import re
import nltk
from nltk.corpus import brown
from termcolor import colored

ALLOWED_ATTEMPTS = 6
WORD_LENGTH = 5
try:
    WORD_BANK = [word.upper() for word in brown.words() if len(word) == WORD_LENGTH and word.isalpha()]
except RuntimeError: # Data is not yet downloaded
    nltk.download(brown)
    word_bank = [word.upper() for word in brown.words() if len(word) == WORD_LENGTH and word.isalpha()]

def validate(attempt, answer, current_alpha):
    result = ''
    for pos, char in enumerate(attempt):
        if char == list(answer)[pos]: # Letter is correct and in right position
            color = 'green'
        elif char in answer: # Letter is correct but in wrong position
            color = 'yellow'
        else: # Letter is incorrect
            color = 'red'
        current_alpha = current_alpha.replace(char, colored(char, color))
        result += (' ' + colored(char, color) + ' ')
    print('\n' + result + '\n')
    return current_alpha

def guess(answer):
    alphabet = ('\n\n   Q  W  E  R  T  Y  U  I  O  P   \n    A  S  D  F  G  H  J  K  L    \n      Z  X  C  V  B  N  M     \n\n')
    print('\nEnter your ' + str(ALLOWED_ATTEMPTS) + ' guesses. \n')
    for i in range(ALLOWED_ATTEMPTS):
        while True:
            print(alphabet)
            attempt = input('Attempt #' + str(i + 1) + ': ').upper()
            if len(attempt) == WORD_LENGTH and attempt in WORD_BANK: # Ensures user input is valid
                break
            else:
                print(colored('\nNot in word bank.', 'red'))
        if attempt == answer: # Checks if user won
            return True
        else:
            alphabet = validate(attempt, answer, alphabet)
    return False
    
def main():
    print('\n\n\nI am thinking of a ' + str(WORD_LENGTH) + '-letter word. Can you guess in ' + str(ALLOWED_ATTEMPTS) + ' tries? \n')
    print('If a letter is in the right place, it will be ' + colored('green', 'green') + '.\n' +
    'If it is in the word but in the wrong place, it will be ' + colored('yellow', 'yellow') + '.\n' +
    'If it is not in the word, it will be ' + colored('red', 'red') + '.\n')
    while True:
        answer = random.choice(WORD_BANK) # Picks a word for this turn
        if guess(answer):
            print(colored('\nCongratulations! You won!\n', 'green', attrs=['bold']))
        else:
            print('\nYou lost! The word was ' + colored(answer, 'green') + '\n')
        if input('\nWant to play again with a new word? Type anything to keep playing, or type [q]uit to quit. ').upper().startswith('Q'):
            print('\nThanks for playing.\n')
            exit()

main()

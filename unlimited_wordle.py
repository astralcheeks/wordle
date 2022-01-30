import random
import re
from nltk.corpus import brown
from termcolor import colored

allowed_attempts = 6
word_length = 5
word_bank = [word.upper() for word in brown.words() if len(word) ==word_length and word.isalpha()]

def validate(attempt, answer, current_dict):
    result = ''
    for pos, char in enumerate(attempt): # Iterates over entry to check if letter is correct
        if char == list(answer)[pos]: # Letter is correct and in right position
            result += (' ' + colored(char, 'green') + ' ')
            current_dict = current_dict.replace(char, (colored(char, 'green')))
        elif char in answer: # Letter is correct but in wrong position
            result += (' ' + colored(char, 'yellow') + ' ')
            current_dict = current_dict.replace(char, (colored(char, 'yellow')))
        else: # Letter is incorrect
            result += (' ' + char + ' ')
            current_dict = current_dict.replace(char, (colored(char, 'red')))  
    print('\n' + result + '\n')
    return current_dict

def guess(answer):
    dict_words = ('\n\n   Q  W  E  R  T  Y  U  I  O  P   \n    A  S  D  F  G  H  J  K  L    \n      Z  X  C  V  B  N  M     \n\n')
    print('\nEnter your 6 guesses. \n')
    for i in range(allowed_attempts): # Iterates over 6 attempts
        while True:
            print(dict_words)
            attempt = input('Attempt #' + str(i + 1) + ': ').upper() # Takes user input
            if len(attempt) == word_length and attempt in word_bank: # Ensures user input is valid
                break
            else:
                print(colored('\nNot in word bank.', 'red'))
        if attempt == answer: # Checks if user won
            return True
        else:
            dict_words = validate(attempt, answer, dict_words) # Calls validation function
    return False
    
def main():
    print('\n\n\nI am thinking of a 5-letter word. Can you guess in 6 tries? \n')
    print('If a letter is in the right place, it will be ' + colored('green', 'green') + '.\n' +
    'If it is in the word but in the wrong place, it will be ' + colored('yellow', 'yellow') + '.\n' +
    'If it is not in the word, it will be ' + colored('red', 'red') + '.\n')
    while True:
        answer = random.choice(word_bank) # Picks a 5-letter word for this turn
        if guess(answer):
            print(colored('\nCongratulations! You won!\n', 'green', attrs=['bold']))
        else:
            print('\nYou lost! The word was ' + colored(answer, 'green') + '\n')
        if input('\nWant to play again with a new word? Type anything to keep playing, or type Q to quit. ').upper() == 'Q':
            print('\nThanks for playing.\n')
            exit()

main()

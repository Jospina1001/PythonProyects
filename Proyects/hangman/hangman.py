import random
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choise(words)
    return word.upper()

def hangman():
    

import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word: #tomamos las palabras sin espacios o guiones
        word=random.choise(words)
    return word.upper()

def hangman():
    word=get_valid_word(words)
    word_letters=set(word) #letters in the word
    alphabet = set(string.ascii_uppercase) #alphabet}
    used_letters = set()

    while len(word_letters) > 0:
        print('You have used these letters: ',' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('invalid character. Please try again.')
    print(f'You won, the word is: {word}')


hangman()

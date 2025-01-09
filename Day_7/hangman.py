import random

from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

choosen_word = random.choice(word_list).lower()

display = []

# print(f"The choosen word: {choosen_word}")÷

for char in range(0, len(choosen_word)):
    display.append('_')

end_of_game = False
lives = 6

while not end_of_game:
    letter = input('Guess a letter: ').lower()

    if letter in display:
        print(f"You've already guessed '{letter}'")
    # choosen_word = random.choice(word_list)

    for position in range(0, len(choosen_word)):
        if choosen_word[position] == letter:
            display[position] = letter

    if letter not in choosen_word:
        print(f"You guessed the letter {letter}, that is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose')
    print(f"{''.join(display)}")
    if '_' not in display:
        end_of_game = True
        print('You won')
    print(stages[lives])
    


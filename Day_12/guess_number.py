import random
EASY_TURNS = 10
HARD_TURNS = 5
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100')
difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()

def set_difficulty(difficulty):
    if difficulty == 'easy':
        return EASY_TURNS
    else:
        return HARD_TURNS

number = random.randint(1, 100)
# print(number, number_of_attempts)
guessed = False
number_of_attempts = set_difficulty(difficulty)
while not guessed:
    print(f'You have {number_of_attempts} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))
    if number_of_attempts == 1:
        guessed = True
        print('You\'ve run out of guesses, you lose')
    elif guess > number:
        number_of_attempts -= 1
        print('Too high.')
        print('Guess again.')
    elif guess < number:
        number_of_attempts -= 1
        print('Too low.')
        print('Guess again.')
    else:
        print(f'You got it! The answer was {number}.')
        guessed = True

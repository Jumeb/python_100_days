from art import logo, vs
from game_data import data
from random import choice

print(logo)


def randStat(statistics):
    return choice(statistics)

def compare(type, datumA, datumB):
    if type == 'a' and datumA['follower_count'] > datumB['follower_count']:
        return True
    elif type == 'b' and datumA['follower_count'] < datumB['follower_count']:
        return True
    else:
        return False

score_count = 0
continue_game = True
statB = randStat(data)

while continue_game:
    statA = statB
    statB = randStat(data)
    while statA == statB:
        statB = randStat(data)
    print(f"Compare A: {statA["name"]}, {statA["description"]}, from {statA["country"]}")

    print(vs)

    print(f"Against B: {statB["name"]}, {statB["description"]}, from {statB["country"]}")
    user_choice = input("Who has more followers? Type 'A' or 'B' ").lower()

    if compare(user_choice, statA, statB):
        score_count += 1
        print(f'You\'re right: Current Score: {score_count} ')
    else:
        print(f"Sorry, that's wrong. Final score: {score_count}")
        continue_game = False
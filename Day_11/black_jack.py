import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from art import logo

def compare(u_score, c_score):
    if c_score == u_score:
        return'It is a draw'
    if u_score == 0:
        return 'You win, You have a Blackjack'
    elif c_score == 0:
        return'You lose, opponent has a Blackjack'
    elif u_score > 21:
        return "You lose. You went over"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return 'You win'
    else:
        return'You lose'

def score(current_hand):
    """Takes a list of cards and returns the calculated score from the cards"""
    if sum(current_hand) == 21 and len(current_hand) == 2:
        return 0
    if sum(current_hand) > 21 and 11 in current_hand:
        current_hand.remove(11)
        current_hand.append(1)
        return sum(current_hand)
    return sum(current_hand)



def continue_game():
    option = input("Do you want to play a game of Blackjack? Type 'y' of 'n': ")
    if option == 'y':
        black_jack();
    else:
        return


def black_jack():
    print(logo)
    user_cards = []
    computer_cards = []
    should_continue = True

    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]   
    while should_continue:
        user_score = score(user_cards)
        computer_score = score(computer_cards)
        print(f'    Your cards: {user_cards}, total = {score(user_cards)}')
        print(f'    Computer\'s first card: {computer_cards[0]}')
        if user_score > 21 or user_score == 0 or computer_score == 0:
            should_continue = False
        else:
            continue_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if continue_deal == 'y':
                user_cards.append(random.choice(cards))
            if continue_deal == 'n':
                should_continue = False
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = score(computer_cards)
    print(f'    Your final hand: {user_cards}, total = {user_score}')
    print(f'    Computer\'s final hand: {computer_cards},  total = {computer_score}')
    print(compare(user_score, computer_score))
    continue_game()

black_jack()





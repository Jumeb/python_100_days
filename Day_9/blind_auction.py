bidding_record = {}
biding = True

def find_highest_bid(bidding_record):
    winning = 0
    win_key = ''
    for bidder in bidding_record:
        if bidding_record[bidder] > winning:
            winning = bidding_record[bidder]
            win_key = bidder
    print(f'The winner is {win_key} with a bid of ${winning}')

while biding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid? $"))
    bidding_record[name] = bid
    con_biding = input('Are there any other bidders? Type \'yes\' or \'no\'. \n')
    if con_biding == 'no':
        find_highest_bid(bidding_record)
        biding = False


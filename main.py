from art import logo


print(logo)

bids = {}
bidding_finised = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount


while not bidding_finised:
    name = input("What's your name? ")
    price = input("What's your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == 'no':
        bidding_finised = True
    



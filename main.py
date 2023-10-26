from art import logo


print(logo)

bids = {}
bidding_finised = False

while not bidding_finised:
    name = input("What's your name? ")
    price = input("What's your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == 'no':
        bidding_finised = True




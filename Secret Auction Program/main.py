import art
print(art.logo)

auction_dict = {}
condition = True

# fnc
def find_highest_bidders(auction_dict):
    winner = ""
    max_bid = 0
    for bidder in auction_dict:
        bid_amount = auction_dict[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")

# TODO-1: Ask the user for input
while condition:
    name = input("What is you name?: ")
    bid = int(input("What is your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    auction_dict[name] = bid

    # TODO-3: Whether if new bids need to be added
    any_bidders_left = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    # TODO-4: Compare bids in dictionary
    if any_bidders_left == 'no':
        print("\n" * 20)

        ## using max function
        #max_name = max(auction_dict, key=auction_dict.get)  # return max value key name
        #max_bid = auction_dict[max_name]
        #print(f"The winner is {max_name} with a bid of ${max_bid}")

        # using user defined fnc
        find_highest_bidders(auction_dict)
        condition = False
    else:
        print("\n" * 20)




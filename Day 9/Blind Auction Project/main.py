import art
print(art.logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def find_highest_bid(bidding_record):
    winner = ""
    highest_bid = 0

    # bids_list = list(bids.values())
    # highest_bid = max(bids_list)
    #
    # for key, value in bids.items():
    #     if value == highest_bid:
    #         winner = key

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


stop_auction = False
bids = {}

while not stop_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

    bids[name] = bid

    if other_bidders == "no":
        stop_auction = True
    else:
        print("\n"*20)

find_highest_bid(bids)

# print(bids)









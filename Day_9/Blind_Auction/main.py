"""Game that runs a blind auction"""

def find_highest_bidder(bidding_dict):
    """Finds and prints the highest bidder"""
    if not bidding_dict:
        print("No bids were placed")
        return
    highest_bid = 0
    winner = None
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is: {winner} with a bid of €{highest_bid}")

def clear_screen():
    """Clears the screen"""
    print("\n" * 20)

bids = {}
continue_bidding = True

while continue_bidding:
    user_name = input("Enter your name: ").strip().lower()

    try:
        user_bid = int(input("Enter your bid: €").strip())
    except ValueError:
        print("Incorrect format.")
        continue

    bids[user_name] = user_bid

    should_continue = input("Are there any more bidders? (y/n): \n").lower().strip()
    if should_continue != "y":
        continue_bidding = False
        find_highest_bidder(bids)
    else:
        clear_screen()



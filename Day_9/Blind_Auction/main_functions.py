def clear_screen():
    """Clears Screen"""
    print("\n" * 100)

def name_and_bid(bids):
    """Asks for name and bid """
    user_name = input("Please enter name: ").strip().lower()

    try:
        user_bid = int(input("Please enter bid: ").strip())
    except ValueError:
        print("Please enter a valid number")
        return

    bids[user_name] = user_bid
    print("Bid recorded")
    clear_screen()

def more_bids():
    """Asks for more bids"""
    bid_input = input("More bids? (y/n): ").strip().lower()
    return bid_input == 'y'

def highest_bid(bids):
    """Fins and prints the highest bidder"""
    winner = max(bids, key=bids.get)
    print(f"The winner is {winner} with a bid of {bids[winner]}!")

# --- HUVUDPROGRAM ---
bids = {}

while True:
    name_and_bid(bids)
    if not more_bids():
        break

highest_bid(bids)
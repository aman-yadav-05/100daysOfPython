from console_util import clear_console
#HINT: You can call clear() to clear the output in the console.

import art

print(art.logo)

bids = {}


def bid_entry(name, bid):
  bids[name] = bid


def highest_bidder(bids):
  # for key in bids:
  #   bids[key]
  Key_max = max(zip(bids.values(), bids.keys()))[1]  
  print(f'the max bid is from {Key_max} with bid: {bids[Key_max]}$')  


end_of_bid = False

while not end_of_bid:
  bidder_name = input("Enter your name:\n")
  bid_price = int(input("Enter your bidding price ($):\n"))
  bid_entry(name=bidder_name, bid=bid_price)

  #asking if there are other bidders
  other_bidders = input("Are there other bidders? Type 'yes' or 'no':\n")
  #if there are other bidders, clear the screen and ask for the next bidder's name and bid price
  if other_bidders=='yes':
    clear_console()
  else:
    clear_console()
    highest_bidder(bids=bids)
    end_of_bid=True

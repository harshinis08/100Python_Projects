print("Welcome to the Secret Auction program..")

more_bidders = True

bidders = {}

while more_bidders:
    name = input("What is your name? ")

    price = input("What's your bid?: $")

    bidders[name] = price

    choice = input("Are there any other bidders? Type 'yes' or 'no': ")

    if choice == "no":
        more_bidders = False

print(bidders)

max_bid = 0
bidder_name = ""

for i in bidders:
    val = int(bidders[i])
    if val > max_bid:
        max_bid = val
        bidder_name = i

print(f"The winner is {bidder_name} with a bid of  ${max_bid}")
import random

print("Tossing a coin....")
value = random.randint(0, 1)

if value == 0:
    print("It's Heads")
else:
    print("It's Tails")
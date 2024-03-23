from trasureLogo import logo

print(logo)

print("Welcome to Treasure Island!")
print("Your mission is to find treasure.")

direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()

if direction == 'left':
    option = input(
        "You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type "
        "\"swim\" to swim across\n").lower()

    if option == 'wait':
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. "
            "Which color do you choose?\n")

        if door == 'blue':
            print("Eaten by beasts. Game Over!!!")
        elif door == 'red':
            print("It's a room full of fire. Game Over!!!")
        elif door == 'yellow':
            print("You Win!!!")
        else:
            print("Game Over!!!")
    else:
        print("Attacked by trout. Game Over!")
else:
    print("Fall into a hole. Game Over.")

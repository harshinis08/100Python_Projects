
import random

rock = ''' rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


logo = [rock, paper, scissors]

computer = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(logo[user_choice])

print("Computer chose: ")
print(logo[computer])

if computer == user_choice:
    print("It's a draw!")
elif user_choice == 0:
    if computer == 1:
        print("Computer Wins!!!")
    else:
        print("User Win!!!")
elif user_choice == 1:
    if computer == 0:
        print("User Wins!!!")
    else:
        print("Computer Win!!!")
else:
    if computer == 0:
        print("Computer Wins!!!")
    else:
        print("User Win!!!")



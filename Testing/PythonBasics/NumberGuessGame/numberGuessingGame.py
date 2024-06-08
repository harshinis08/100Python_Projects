import random

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100 ")

user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

number = random.choice(range(1, 101))
print(number)

attempts = 0

if user_choice == "easy":
    attempts = 10
elif user_choice == "hard":
    attempts = 5
else:
    print("Invalid input!!")

while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.. ")
    guess = int(input("Make a guess: "))

    if guess == number:
        print("Correct.. You Win!")
    elif guess < number:
        print("Too Low!")
        print("Try again")
    elif guess > number:
        print("Too High!")
        print("Try again")
    elif attempts == 0:
        print("You've run out of guesses.. You  Lose!")

    attempts -= 1
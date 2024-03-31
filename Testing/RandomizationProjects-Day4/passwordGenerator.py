import random

print("Welcome to the PyPassword Generator!!")

count = 0

letters_count = int(input("How many letters you would like in your password? "))
symbols_count = int(input("How many symbols would you like? "))

numbers_count = int(input("How many numbers would you like? "))

user_choice = [letters_count, symbols_count, numbers_count]

count += letters_count + symbols_count + numbers_count
print(f"Password length {count}")

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '<', '>', '?', ']', '[', '{', '}',
           '+', '|']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

options = [letters, symbols, numbers]

password_1 = ""

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

while letters_count > 0:
    val = random.randint(0, len(letters) - 1)
    password_1 += letters[val]
    letters_count -= 1

while symbols_count > 0:
    val = random.randint(0, len(symbols) - 1)
    password_1 += symbols[val]
    symbols_count -= 1

while numbers_count > 0:
    val = random.randint(0, len(numbers) - 1)
    password_1 += numbers[val]
    numbers_count -= 1

print(password_1)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_2 = ""

count = letters_count + numbers_count + symbols_count
element_list = [letters, numbers, symbols]

while len(password_2) != count:
    current = random.choice(element_list)

    if current == letters and letters_count > 0:
        password_2 += random.choice(letters)
        letters_count -= 1
    elif current == symbols and symbols_count > 0:
        password_2 += random.choice(symbols)
        symbols_count -= 1
    elif current == numbers and numbers_count > 0:
        password_2 += random.choice(numbers)
        numbers_count -= 1

print(password_2)

print(f"Here is your password {password_2}")


#Hard Level Method 2:

password_list = []
password_created = ""

for i in range(1, letters_count+1):
    password_list.append(random.choice(letters))

for i in range(1, numbers_count+1):
    password_list.append(random.choice(numbers))

for i in range(1, symbols_count+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

for i in password_list:
    password_created += i

print(f"Here is your password {password_created}")

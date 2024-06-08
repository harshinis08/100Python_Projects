
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z']

flag = True


def caesar(user_choice, text, shift):
    shift_count = 0

    new_text = ""

    if user_choice == "decode":
        shift = shift * (-1)

    for i in text:
        if i in letters:
            current = letters.index(i) + shift
            shift_count = current % 26

            new_text += letters[shift_count]
        else:
            new_text += i

    print(f"Your {user_choice}d text is {new_text}")


while flag:
    user_option = input("Type 'encode' to encrypt, type 'decode' to decrypt. \n").lower()

    if user_option == "encode" or user_option == "decode":
        message = input("Type your message.. :  ")
        shift_number = int(input("Type the shift number : "))

        caesar(user_option, message, shift_number)
    else:
        print("Unknown Input!!!")

    answer = input("Type 'yes' if you want to go again? Otherwise type 'no'.")

    if answer == 'no':
        flag = False




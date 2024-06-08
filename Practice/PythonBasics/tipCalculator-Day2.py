print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

total = bill * (1 + tip/100)

# Can you also "%.2f" % round(total/people, 2) to have trailing zeroes
per_person = "{:.2f}".format(round(total/people, 2))

print(f"Each person should pay: ${per_person}")
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of the bill would you like to tip? "))
people = int(input("How many people are splitting the bill? "))
final = (bill + tip) / people
print("Each person should pay: $" + str(round(final, 2)))
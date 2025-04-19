print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

total_amount = (bill + ((tip_percent / 100) * bill)) / no_of_people
print(f"Each person should pay: ${total_amount:.2f}")
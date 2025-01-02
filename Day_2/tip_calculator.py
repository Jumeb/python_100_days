print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"));
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_splitting = int(input("How many people to split the bill? "))

total_bill += total_bill * (tip_percentage/100)

each_person_bill = "{:.2f}".format(total_bill / people_splitting)

print(f"Each person should pay: ${each_person_bill}")


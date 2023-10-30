print("Welcome to the tip calculator!")
total_bill = float(input("What's the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
each_person_bill = (total_bill + (total_bill*(tip/100)))/people
# new_each_person_bill = round(each_person_bill, 2)
new_each_person_bill = ("{:.2f}".format(each_person_bill))
print(f"Each person should pay: ${new_each_person_bill}")
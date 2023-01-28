print("Welcome to tips calculator:")
total = float(input("What was the total bill?"))
percent = int(input("What percentage tip would you like to give?"))
people = int(input("How many people should split the bill?"))

bill = percent/100*total + total
each = bill/people
each_person = round(each, 2)
print(f"Each person should pay {each}")

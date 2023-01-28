import random

names_string = input("Enter everybody's name separated by a comma. ")
names = names_string.split(",")

people = len(names)

random_choice = random.randint(0, people-1)

person_to_pay = names[random_choice]

print(f"{person_to_pay} is to pay the bill")
  
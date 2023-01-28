print("Welcome to Python Pizza Deliveries!")
size = input("What size of Pizza do you want? S,M,L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n ")
extra_cheese = input("Do you want extra cheese? Y or N \n")
bill = 0
S = 15
M = 20
L = 25
Ps = 2
Pl = 3
Extra = 1


if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill = S+Ps+Extra
    print(f"Your final bill is $ {bill}")
elif size == "S" and add_pepperoni == "Y" and extra_cheese == "N":
    bill = S+Ps
    print(f"Your final bill is $ {bill}")
elif size == "S" and add_pepperoni == "N" and extra_cheese == "Y":
    bill = S+Extra
    print(f"Your final bill is $ {bill}")
elif size == "S" and add_pepperoni == "N" and extra_cheese == "N":
    bill = S
    print(f"Your final bill is $ {bill}")
elif size == "M" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill = M+Pl+Extra
    print(f"Your final bill is $ {bill}")
elif size == "M" and add_pepperoni == "Y" and extra_cheese == "N":
    bill = M+Pl
    print(f"Your final bill is $ {bill}")
elif size == "M" and add_pepperoni == "N" and extra_cheese == "Y":
    bill = M+Extra
    print(f"Your final bill is $ {bill}")
elif size == "M" and add_pepperoni == "N" and extra_cheese == "N":
    bill = M
    print(f"Your final bill is $ {bill}")
elif size == "L" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill = L+Pl+Extra
    print(f"Your final bill is $ {bill}")
elif size == "L" and add_pepperoni == "Y" and extra_cheese == "N":
    bill = L+Pl
    print(f"Your final bill is $ {bill}")
elif size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
    bill = L+Extra
    print(f"Your final bill is $ {bill}")
elif size == "L" and add_pepperoni == "N" and extra_cheese == "N":
    bill = L
    print(f"Your final bill is $ {bill}")
else:
    print("Invalid Input")

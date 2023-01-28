print("Welcome to the Love calculator: ")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

names = name1.lower()+name2.lower()
T = names.count("t")
R = names.count("r")
U = names.count("u")
E = names.count("e")

true = str(T+R+U+E)


L = names.count("l")
O = names.count("o")
V = names.count("v")
E = names.count("e")

love = str(L+O+V+E)
score = int(true+love)

if score < 10 or score > 90:
    print(f"Your score is {score}, You go together like coke and mentos ")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, You are alright together.")
else:
    print("Your score is {score}.")

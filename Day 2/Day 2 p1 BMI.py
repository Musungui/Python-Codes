height=input("Enter your height in m:\n")
weight=input("Enter your weight in kg:\n")

height_sq = float(height**height)
BMI=float(weight)/float(height_sq) 
print("Your BMI is:" +BMI)
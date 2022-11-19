# Program to calculate BMI mobin mohammadi
name = str(input("whats your name? "))
height = float(input("please type your Hight(cm): "))
weight = float(input("please type your Weight(kg): "))

bmi = weight / (height/100)**2

print("your bmi is: ",bmi)

if bmi <= 18.4:
    print("You are underweight " + name)
elif bmi <= 24.9:
    print("you are healthy " + name)
elif bmi <= 29.9:
    print("You are overweight " + name)
elif bmi <= 34.9:
    print("You are severely overweight " + name)
elif bmi <= 39.9:
    print("you're fat " + name)
else:
    print("You are extremely fat " + name)
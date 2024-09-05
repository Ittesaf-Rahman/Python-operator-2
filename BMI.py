weight = float(input("Enter your weight(Kg) = "))
height = float(input("Enter your height(Meter) = "))
BMI = weight/height**2
if BMI < 18.5:
    print("You are under weight")
elif BMI>= 18.5 and BMI < 25:
    print("You are Normal")
elif BMI>= 25 and BMI < 30:
    print("You are Over weight")
elif BMI>= 30 and BMI < 35:
    print("You are Obese")
elif BMI>=35 and BMI < 40:
    print("You are Obese class2")
else:
    print("Obese class3")
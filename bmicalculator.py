def bodymassindex(height, weight) :
    return round((weight / height ** 2),2)

print("Welcome to Body Mass Index Calculator")

height = float(input("Enter your height in meters:"))
weight = float(input("Enter your weight in kilograms:"))


bmi = bodymassindex(height,weight)
print("Your BMI is:", bmi)

if bmi <= 18.5:
    print("You are Underweight")
elif 18.5 < bmi <= 24.9:
    print("Your weight is Normal")
elif 25 < bmi <= 29.9:
    print("You are overweight")
else:
    print("You Are Obese")

print("Thank You !!")
def inches_to_meters(inches):
    return inches * 0.3048 

def bodymassindex(height, weight) :
    return round((weight / height ** 2),2)


print("Body Mass Index (BMI) Calculator")

choice = input("Do you want to enter height in inches? (yes/no): ").strip().lower()

if choice == "yes":
    inches = float(input("Enter height in inches:"))
    height = inches_to_meters(inches)
    print(f"Converted Height: {height:.2f} meters")
else:
    height = float(input("Enter height in meters: "))    

weight = float(input("Enter weight in kilograms:"))

bmi = bodymassindex(height, weight)

print("Your Body Mass Index is:",bmi)

if bmi <= 18.5:
    print("Underweight")
elif 18.5 < bmi <= 24.9:
    print("Normal")
elif 25 < bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")
    
print("Thank You !!!")
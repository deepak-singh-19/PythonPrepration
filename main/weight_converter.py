#-- kilograms to pounds
#---pounds to kilograms

weight = float(input("Please enter the weight of the object: "))
unit = input("Please enter the unit of the object Kilograms or Pounds (K or P): ")

if unit == "k":
    weight = weight * 2.205
    unit = "pounds"
elif unit == "p":
    weight = weight / 2.205
    unit = "kilograms"
else:
    print(f"{unit} is not a valid")

print(f"Your weight is: {round(weight, 1)} {unit}")
# a = input("Enter a first number: ")
# b = input("Enter a second number: ")
#
# print(int(a) + int(b))

# c = input("Enter a first number: ")
# d = input("Enter a second number: ")
#
# print(int(c) + int(d))
# print(int(c) - int(d))
# print(int(c) * int(d))
# print(int(c) / int(d))

units = int(input("Enter total consumed electricity unit: "))
per_unit_charge = 5

if units <= 100:
    bill = units * per_unit_charge

    print(f"Total Consumed Electricity : {bill}")
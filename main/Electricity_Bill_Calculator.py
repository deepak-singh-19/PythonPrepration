# Electricity Bill Calculator

# Take input from user
units = int(input("Enter the number of units consumed: "))

# Per unit charge
rate_per_unit = 10

# If units are less than 100 -> Free
if units <= 100:
    bill = 0

# If units are greater than 100 but less than or equal to 200 -> 5% charge
elif units <= 200:
    bill = units * rate_per_unit
    bill = bill + (bill * 0.05)   # adding 5% extra charge

# If units are greater than 200 -> 10% charge
else:
    bill = units * rate_per_unit
    bill = bill + (bill * 0.10)   # adding 10% extra charge

# Print the result
print(f"Total Units Consumed : {units}")
print(f"Total Bill Amount    : ₹{bill:.2f}")

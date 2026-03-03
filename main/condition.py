# (-) conditional operators
# (<) less than
# (>) greater than
# (<=) less than equal
# (>=) greater than equal
# (==) equal equal
# (!=) not equal

# a = int(input("Enter your age: "))
# print("Your age is:", a)

#
# print(a!=18)


#-- Check the positive, negative & zero --------
# num = int(input("Enter a number: "))
# if num<0:
#     print("Negative Number")
# elif num==0:
#     print("Zero")
# else:
#     print("Positive Number")

#--- odd & even number ---------------------------
# num = int(input("Enter a number: "))
#
# if num % 2 == 0: print(a<18)
# print(a>18)
# print(a<=18)
# print(a>=18)# if a < 18:
#     print("You are not eligible for the voting:", a)
# else:
#     print("You are eligible for the voting:", a)
# print(a==18)
#     print("Even")
# else:
#     print("Odd")

# --- vehicle speed -------------------------------

# speed = int(input("Enter a vehicle speed Km/Hr:"))
# print("Enter a vehicle speed Km/Hr: ", speed)
#
# if speed < 80:
#     print("The vehicle speed is low")
# elif speed == 80:
#     print("The vehicle speed is medium")
# else:
#     print("The vehicle speed is high")

# --Bill units
# unit = int(input("Enter the units :"))
# # print("Enter the units: ", unit)
# rate_per_unit = 10
#
# if unit <= 100:
#     print("Your light bill is free")
# elif unit <= 200:
#     bill = unit*rate_per_unit
#     print("Your system Generated Bill is: ", bill)
# else:
#     bill = unit*15
#     print("Your system Generated Bill is: ", bill)

#-- Mark grading system
# mark = int(input("Enter the marks :"))
# if mark <= 50:
#     print("Grade C")
# elif mark <= 75:
#     print("Grade B")
# else:
#     print("Grade A")

#-- Greatest of two numbers

# a = int(input('Enter a first number: '))
# b = int(input('Enter a second number: '))
#
# if a > b:
#     print("First number is greater than second number")
# elif b > a:
#     print("Second numer is greater than first number")
# else:
#     print("Both numbers are equal")

# ------ Even or Odd number program

# number = int(input("Enter the number: "))
#
# if number % 2 == 0:
#     print("Even number :", number)
# else:
#     print("Odd number :", number)

#----internet Access
# age = float(input("Enter you Age: "))
#
# if age >= 18:
#     print("Welcome to High-speed internet")
# else:
#     print("Sorry! You can't access the internet")

#---office entry access
# name = input("Enter your name: ")
# password = int(input("Enter your password: "))
#
# if password == 1123:
#     print("Welcome!")
# else:
#     print("Sorry!")

#---task recharge
# days  = int(input("Enter the days: "))
# if days <= 28:
#     print("Your recharge is not expire")
# else:
#     print("Your recharge has been expired")

#--------------bill charge
# units = float(input("Enter the units: "))
# unit_charge = 5
# bills = units * unit_charge
# if units >= 50:
#     print(f"Your current month electricity bill is: {bills}rs")
# else:
#     print("Your current month electricity bill is Zero!")

#----Positive, Negative & Zero
# number = int(input("Enter a number: "))
# if number > 0:
#     print("Positive number")
# elif number < 0:
#     print("Negative number")
# else:
#     print("Zero")

#------ Larget number
# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter a number: "))
# num3 = float(input("Enter a number: "))

#---------Using with condition (if, else)
# if num1 > num2:
#     print(f"{num1} is greater")
# else:
#     print(f"{num2} is greater")

#--------without applying condition
# print(f"The greater number is : {max(num1, num2, num3)}")

#----------Age Eligibility (Voting)
# age = float(input("What is your age? "))
# if age >= 18:
#     print("You are eligible for voting")
# else:
#     print("You are not eligible for voting")

#-----------Divisible by 5
# number = int(input("Enter a number: "))
# if number % 5 == 0:
#     print(f"{number} is divisible by 5")
# else:
#     print(f"{number} is not divisible by 5")

#--------Number Divisible by Both 3 and 5
# number = int(input("Enter a number: "))
# if number % 3 == 0 and number % 5 == 0:
#     print("Number divisible by 3 and 5")
# elif number % 3 == 0:
#     print("Number divisible by 3")
# elif number % 5 == 0:
#     print("Number divisible by 5")
# else:
#     print("Number not divisible by 3 and 5")

#------Salary Bonus Calculation
# salary = int(input("Enter your salary: "))
# bonus = salary * 0.20
# if salary >= 50000:
#     print(f"Your salary bonus is: {bonus}")
# elif salary >= 30000:
#     bonus = salary * 0.10
#     print(f"Your salary bonus is: {bonus}")
# else:
#     bonus = salary * 0.05
#     print(f"Your salary bonus is: {bonus}")

#----------student mark
# mark = int(input("Enter your mark: "))
#
# if mark >=90:
#     print(f"According to your mark the grade is A")
# elif mark >= 60:
#     print(f"According to your mark the grade is B")
# else:
#     print(f"According to your mark the grade is C")

#---------Login System Basic Logic
# username = input("Please enter your username: ")
# password = int(input("Please enter your password: "))
#
# if username == "admin":
#     if password == 1234:
#         print("Welcome To Admin")
#     else:
#         print("Incorrect Password")
# else:
#     print("Incorrect Username")

#------Number Divisible by 2 and 5
# number = int(input("Enter a number: "))
# if number % 2 == 0 and number % 5 == 0:
#     print("The number is divisible by 2 and 5")
# elif number % 2 == 0:
#     print("The number is divisible by 2")
# elif number % 5 == 0:
#     print("The number is divisible by 5")
# else:
#     print("The number is not divisible by 2 and 5")
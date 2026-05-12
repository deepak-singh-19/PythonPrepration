#- practice python program

#--Store marks of 5 subjects in list and calculate total marks
# subject = ["Hindi", "English", "Math", "Science", "Computer"]
# subject_marks = [50, 60, 80, 40, 50]
# total = sum(subject_marks)
# print(f"Total marks: {total}")

#-2--Create dictionary for automation tool
# automation_tool = {"Tool 1" : "Selenium",
#                    "Tool 2" : "Playwright",
#                    "Tool 3" : "Cypress",
#                    "Tool 4" : "TestNG"
#                    }
# print(automation_tool)

#-3- Store week days
# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# print(days)

#-4- check the even or odd number
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("it is even number")
# else:
#     print("it is odd number")

#-5- Age eligibility
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible for vote")
# else:
#     print("You are not eligible for vote")

#-6- check the positive, negative and zero number
# number = float(input("Enter a number: "))
# if number > 0:
#     print("It is a positive number")
# elif number < 0:
#     print("It is a negative number")
# else:
#     print("It is a zero number")

#-7- check credentials
# username = input("Enter your username: ")
# password = int(input("Enter your password: "))
# if username == "admin" and password == 123:
#     print("Welcome Admin")
# else:
#     print("Wrong username or password")

#-8- Check largest digit between two numbers
# first_num = int(input("Enter first number: "))
# second_num = int(input("Enter second number: "))
#
# if first_num > second_num:
#     print("The first number is greater than the second number")
# else:
#     print("The second number is greater than the first number")

#--Even or odd
# number =float(input("Enter the digits: "))
# if number % 2 == 0:
#     print("It is even number")
# else:
#     print("It is odd number")

#--positive, negative and zero
# number = int(input("Enter the number: "))
# if number > 0:
#     print("This number is positive number")
# elif number < 0:
#     print("This number is negative number")
# else:
#     print("This number is zero")

#-vote criteria
# age = int(input("Enter your age: "))
# if age >=18:
#     print("You are eligible for the vote")
# else:
#     print("Your are not eligible for the vote")

#--weekday and weekend first program
# days = input("Enter the days: ")
# if days == "Monday":
#     print("It's weekday")
# elif days == "Tuesday":
#     print("It's weekday")
# elif days == "Wednesday":
#     print("It's weekday")
# elif days == "Thursday":
#     print("It's weekday")
# elif days == "Friday":
#     print("It's weekday")
# else:
#     print("It's weekend")

#--weekday or weekend second program
# day = input("Enter a day: ").strip() #--.strip() method is used for removing the all whitespace from strat and ending the string
# if day == "Saturday" or day == "Sunday":
#     print("it's weekend")
# else:
#     print("it's weekday")

#-check the fail pass criteria
# marks = float(input("Enter your marks: "))
# if marks <= 40:
#     print("Sorry!, Yor are failed")
# elif marks > 100:
#     print("Please enter the correct marks")
# else:
#     print("Congrats!, You are passed")

#--Temperature Check
# Temperature = float(input("Enter Temperature in Celcius: "))
# if Temperature >= 35:
#     print("It's a hot day")
# else:
#     print("Good Temperature")

#- ATM withdrawal---take account balance and withdrawal amount.
# account_balance = 10000
# withdrawal_amount = float(input("Enter withdrawal amount: "))
# if withdrawal_amount > account_balance:
#     print("Withdrawal amount exceeded")
# else:
#     print("Insufficient balance")

#---hotel bill
# tea = int(input("Enter the quantity the cup of tea: "))
# coffee = int(input("Enter the quantity the cup of coffee: "))
# water = int(input("Enter the quantity the botel of water: "))
# tea_price = 1000
# coffee_price = 20
# water_cost = 40
# total_cost = tea_price*tea + coffee_price*coffee + water_cost*water
# print(float(total_cost))
# if total_cost >=10000:
#     gst = total_cost * 2/100
#     print(gst + total_cost)
# else:
#     print(total_cost)

#--Login OTP Verification
# mobile_number = int(input("Enter mobile number: "))
# otp = int(input("Enter OTP: "))
# if otp == 5442:
#     print("OTP match successfully")
# else:
#     print("Invalid OTP")

#--number range
# number = int(input("Enter the number: "))
# if number >=1 and number <=100:
#     print("The number is between 1 and 100")
# else:
#     print("The number is not between 1 and 100")

#--electricity bill charge program first
# unit = int(input('Enter the electricity used unit: '))
# bill = unit*10
# # print(bill)
# if unit >= 100:
#     bill = unit*20
#     print(bill)
# else:
#     print(bill)

#---electricity bill charge program second
# unit = int(input('Enter the electricity used unit: '))
# bill = unit*10
# if bill > 2000:
#     discount_amount = bill * 5/100
#     print(f"After discount your bill is {bill-discount_amount:.2f} rupees")
# else:
#     print("No discount, your bill is", bill)

#--Largest number-- using with the max method
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# num3 = int(input('Enter the third number: '))
# largest = max(num1, num2, num3)
# print(f"The largest number is {largest}")

#--largest number between three numbers using the condition (if-else)
# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))
# c = int(input('Enter the third number: '))
# if a>=b and a>=c:
#     largest = a
# elif b>=a and b>=c:
#     largest = b
# else:
#     largest = c
# print(f'The largest number is {largest}')

#--email verification-- using with the .endswith() method
# email = input("Enter your email: ").strip().lower()
# if email.endswith("@gmail.com"):
#     print("valid email")
# else:
#     print("invalid email")

#--email verification-- using with the condition method
# email = input("Enter your email: ").strip().lower()
# if "@gmail.com" in email:
#     print("Email address is valid")
# else:
#     print("Email address is not valid")

#---check the mobile number length
# mobile_num = int(input("Enter the mobile number: "))
# length = len(str(mobile_num))
# if length == 10:
#     print(f"the mobile number length is {length}")
# else:
#     print(f"the mobile number length is {length}, Please enter the correct mobile number")

#---divisible by 3 and 5
# number = int(input("Enter a number: "))
# if number % 3 == 0:
#     print("The given number is divisible by 3")
# elif number % 5 == 0:
#     print("The given number is divisible by 5")
# else:
#     print("invalid number")

#---website login attempt
# login_attempt = int(input("Enter your login attempt here: "))
# if login_attempt >3:
#     print("Account Blocked")
# else:
#     print("try again")

#--Movie ticket Eligibility
#Age below 12 - Child ticket
#Age between 12-59 = Adult ticket
#Age 60+ = Senior citizen ticket
# movie = input("Enter movie name: ")
# age = int(input("Enter your age: "))
# if age <=12:
#     print("You are child")
# elif age <=59:
#     print("You are a Adult")
# else:
#     print("You are a senior")
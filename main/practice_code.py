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
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

if first_num > second_num:
    print("The first number is greater than the second number")
else:
    print("The second number is greater than the first number")
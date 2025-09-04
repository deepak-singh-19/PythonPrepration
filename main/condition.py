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
# # print(a>18)
# # print(a<=18)
# # print(a>=18)# if a < 18:
# # #     print("You are not eligible for the voting:", a)
# # # else:
# # #     print("You are eligible for the voting:", a)
# # print(a==18)
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

number = int(input("Enter the number: "))

if number % 2 == 0:
    print("Even number :", number)
else:
    print("Odd number :", number)

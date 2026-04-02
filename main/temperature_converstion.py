#--- temperature convertion celsius to fahrenheit & fahrenheit to celsius
#----- (c*9/5)+32 = f
#----- (f-32)* 5/9 = °C

# unit = input("Is this temperature in celsius or fahrenheit? (C/F): ")
# temp = float(input("Enter the temperature: "))
#
# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     print(f"The temperature in fahrenheit is {temp}°F")
# elif unit == "F":
#     temp = round((temp - 32) * 5 / 9, 1)
#     print(f"The temperature in celsius is {temp}°C")
# else:
#     print(f"{unit} is not a valid")

# ---------Test

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def print_student_details(self):
#         print(self.name, end= "")
#         print(self.age)
#
#     @staticmethod
#     def isTeen(age):
#         return age > 16
#
# #Driver's code
# a = Student.isTeen(18)
# print(a)

a = input('Enter your name: ')
print(type(a))
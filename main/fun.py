# import time
# import webbrowser


#---create a function that prints "Welcome to the python"
# def welcome_message():
#     print("Welcome to the Automation testing using with python language")
# welcome_message()

#--create a function that accept username and prints it
# def username(firstname, lastname):
#     print(f"Your username is: {firstname} {lastname}")
# username("Deepak", "Singh")
# username("Amit", "Singh")
# username("Rahul", "Kumar")

#--Create function to add two numbers
# def add(a, b):
#     print(a+b)
# add(1, 2)
# add(12,19)

#--function t0 add two numbers
# def calculation():
#     a=10
#     b=20
#     print(a+b)
# calculation()

#----Create a function to check add and even number
# def check_even_odd(number):
#     if number % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")
# check_even_odd(3)
# check_even_odd(4)
# check_even_odd(2)

#--Create a function to find Largest number between two numbers using with print
# def largest_num(a, b):
#     if a>b:
#         print(f"{a} is grater")
#     else:
#         print(f"{b} is grater")
# largest_num(10, 20)

#---find Largest number with return function
# def largest_number(num1, num2):
#     if num1>num2:
#         return num1
#     else:
#         return num2
# result = largest_number(29, 21)
# print(f"The largest number is: {result}")

#-Create a login function with username and password parameter.
# def login(username, password):
#     print(f"Username: {username}, Password: {password}")
# login('Deepak', 'ds123')

#-Create a login function with username and password parameter using return
# def login(username, password):
#     correct_username = "Deepak19"
#     correct_password = "DD123@"
#
#     if username == correct_username and password == correct_password:
#         return "Welcome to the Panel"
#     else:
#         return "Access Denied! Your username & password is incorrect"
# print(login("Deepak", "123@dd"))
# print(login("Singh@","877h"))
# print(login("Deepak19", "DD123@"))

#---Create function that returns square of number.
# def square(a):
#     return a * a
# print(square(4))

#---Create function that returns square of number.(using with user input)
# num = int(input("Enter your number: "))
# def square(num):
#     return num * num
# print(square(num))

#-Create function that returns total characters in string.
# def count_chr(a):
#     # return len(a)
#     print(f"Your Character count is : {len(a)}")
# # print(count_chr("Deepak"))
# count_chr("Deepak")
# count_chr("Selenium")
# count_chr("Python")
# count_chr("Automation")

#-Create function that prints numbers from 1 to n using loop.
# def number(num):
#     for num in range(1, num +1):
#         print(num)
#         # return num
# # print(number(1))
# number(101)

#--Create function to print multiplication table.
# num = 3
# for x in range(1, 11):
#     result = num * x
#     # print(result)
#     print(f"{num} * {x} : {result}")

#--Create function to print multiplication table.
# def multiplication(num):
#     for i in range(1, 11):
#         result = num * i
#         print(f"{num} * {i} : {result}")
# multiplication(2)
# multiplication(3)
# multiplication(4)

#-Create function to check password length.
# def length(password):
#     return len(password)
#     # return (f"The password length is {length(password)}")
# print(f"The length of the password is : {length('ds@2323')}")
# print(f"The length of the password is : {length('JKJ@132J')}")
# print(f"The length of the password is : {length('HJH@894793')}")

#-Create function to reverse string.
# def text(a):
#     print("".join(reversed(a)))
# text("Hello World")
# text("Python")

# current_text = input('Enter your text: ')
# reverse_string = ''
# for char in current_text:
#     reverse_string = char + reverse_string
# print(current_text)
# print(reverse_string)

# def text(current_text):
#     reversed_text = ""
#     for char in current_text:
#         reverse_string = char + reversed_text
#         return reverse_string
# user_text = input("Enter your text : ")
# print(text(user_text))

#-Create function to reverse string.
# def text(current_text):
#     # 1. Move this inside the function so it resets every time
#     reverse_string = ''
#
#     for char in current_text:
#         # 2. Use 'reverse_string' here, not 'current_text'
#         reverse_string = char + reverse_string
#
#         # 3. Move the return OUTSIDE the loop so it finishes counting
#     return reverse_string
#
# # 4. Get input and print the result
# user_text = input('Enter your text: ')
# print(text(user_text))

#-Create function to count vowels in string.
# name = input("What is your name?")
# vowels = "aeiouAEIOU"
# count = 0
# for char in name:
#     if char in vowels:
#         count += 1
# print(f"The number of vowels in '{name}' is: {count}")

# def count_vowels(name):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for chr in name:
#         if chr in vowels:
#             count +=1
#     return count
# user_name = input("Enter your name : ")
# # print(count_vowels(user_name))
# print(f"Number of vowels: {count_vowels(user_name)}")

#--browser launch function (Simple program)
# def browser_launch():
#     browser = "google.com"
#     return browser
# print(browser_launch())

#--browser launch function (real browser)
# def browser_launch(url):
#     print(f"Your browser launching url is : {url}")
#     webbrowser.open(url)
# browser_launch("https://www.google.com")

#--browser launch function (Third simple program)
# def browser_launch(a):
#     print(f"Your launching browser is: {a}")
# browser_launch("Chrome Browser")

# def count(start, end):
#     for x in reversed(range(start, end+1)):
#         print(x)
#         time.sleep(1)
#     print("Happy Birthday Buddy!")
# count(0,10)
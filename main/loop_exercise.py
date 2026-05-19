# i = 0
# while (i <= 50):
#     print(i)
#     i = i+1
from turtledemo.clock import display_date_time

# name = 'Deepak'
# for i in name:
#     print(i)

# for i in range(1, 100):
#     print(i)

#---Types of range
#-- start from 0
# for i in range(10):
#     print(i + 1)

#---range(0,10)-- start from 1 and end before 6
# for i in range(0, 10):
#     print(i)

#---range(1, 20, 2)-- start, stop, end
# for i in range(1, 20, 4):
#     print(i)

#print number 1 to 10
# for i in range(10):
#     print(i+1)

# print even number 1 to 20 using for loop
# for d in range(2, 20, 2):
#     print(d)

#print even number 1 to 20 using while loop
# num = 2
# while num <= 20:
#     print(num)
#     num +=2 #-This increases num by 2 in every step

#-print even number using for loop logic check
# for i in range(50):
#     if i %2 ==0:
#         print(i)

#--print odd number using for loop
# for i in range(1,21,2):
#     print(i)

#--- print odd number using while loop
# num = 1
# while num <=20:
#     print(num)
#     num +=2

#print odd number using for loop logic
# for i in range(1, 21):
#     if i %2 != 0:
#         print(i)

#---table multiplication
# number = 8
# for i in range(1, 11):
#     result = number * i
#     print(f"{number} * {i} = {result}")

#---multiplication table
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     result = num * i
#     print(f"{num} * {i} = {result}")

#--star program
# a= ''
# for i in range(1, 11):
#     star = ' *'
#     a += star
#     print(a)

#---print all item in list
# laptop_company = ['Dell', 'HP', 'Lenovo', 'Asus', 'Soni']
# for company in laptop_company:
#     print(company)

#--Print the sum of the 1 to 10
# count = 0
# for i in range(1,101):
#     count += i
#     print(f'The sum of the 1 to 100 is : {count}')
#     # print(f'The sum of the 1 to 100 is : {sum(range(1, i+1))}')

#--Count vowels in string
# name = input("What is your name?")
# vowels = "aeiouAEIOU"
# count = 0
# for char in name:
#     if char in vowels:
#         count += 1
# print(f"The number of vowels in '{name}' is: {count}")

#--reversed string
# current_text = input('Enter your text: ')
# reverse_string = ''
# for char in current_text:
#     reverse_string = char + reverse_string
# print(current_text)
# print(reverse_string)

#Find largest number in list
# number = [10, 0, .1, 4, 96, 101,5]
# largest = number[0]
# for num in number:
#     if num > largest:
#         largest = num
# print(f'The largest number is: {largest}')

#Find smallest number in list
# number = [10, 0, .1, 4, 96, 101,5, -1]
# smallest = number[0]
# for num in number:
#     if num < smallest:
#         smallest = num
# print(f'The smallest number is: {smallest}')

#--print 1 to 10 using while loop
# num = 0
# while num < 10:
#     num += 1
#     print(num)

#--print countdown 10 to 1
# for i in range(10, 0, -1):
#     print(i)
 #--even number between 1 to 10
# number = 0
# while number < 100:
#     number = number + 1
#     if number % 2 == 0:
#         print(f"The even number is: {number}")

#-print odd number 1 to 10
# number = 0
# while number < 100:
#     number = number + 1
#     if number % 2 != 0:
#         print(f"The odd number is: {number}")

#---Multiplication table
# digit = int(input("Enter a number: "))
# i = 1
# while i < 10:
#     i = i +1
#     result = digit * i
#     print(f"{digit} x {i} = {result}")

#---password match
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "admin" and password == "123":
#     print("Welcome Admin")
# else:
#     print("incorrect username or password")


#--Password match using while loop
# username = input("Enter your username: ")
# password = input("Enter your password: ")
#
# while username != "Deepak" and password != 123:
#     print("Wrong username or password\n")
#
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#
# print("Welcome " + username)

#--break program
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

#--continue program
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

#Age calculater
# birth_year = int(input("Enter birth year: "))
# current_year = int(input("Enter current year: "))
# print(current_year - birth_year)
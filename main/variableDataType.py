# a= 1
# b= 10.1
# c = "Deepak"
# d = None
# print("Type of a is", type(a))
# print("Type of a is", type(b))
# print("Type of a is", type(c))
# print("Type of a is", type(d))

# --list
# -touple
# --Map (dictionary)
# dictionarydict ={"name":"deepak", "Age":25, "Mobile Number":5555555555,}
# print(dict)

#-- Variable exercise
#---1 store personal information
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# current_city = input("Enter your city: ")
# native_place = input("Enter your native place: ")
# company_name = input("Enter your company name: ")
# job_role = input("Enter your job role: ")
# print(name, age, current_city, native_place, company_name, job_role)

#----Swap two number
# a = 10
# b = 20
# a,b = b,a
# print(a)
# print(b)

#---Calculate basic salary
# basic_salary = int(input("Enter a basic salary: "))
# bonus = int(input("Enter a bonus: "))
# deduction = int(input("Enter a deduction: "))
# total_salary = basic_salary + bonus - deduction
# print("Your total salary is", total_salary)

#--Product price calculater
# product_name = input("Enter Your product name: ")
# product_quantity = int(input("Enter Your product quantity: "))
# product_price = int(input("Enter Your product price per item: "))
# total_bill = product_quantity * product_price
# print(total_bill)

#-Login Credentials
# name = input("Please enter your username: ")
# password = int(input("Please enter your password: "))
# print("Your username is " + name, "and password is ",password)

#--Data type identification
# a = 10
# b = "Deepak"
# c = 10.3
# d = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

#---List practice
# #print second car company
# #print last company namr
# #print length of the suzuki
# car_company = ["Tata", "Mahindra", "Suzuki", "Nexa"]
# print("car company:", car_company[1])
# print("car company:", car_company[3])
# print("car company:", car_company[-1])
# print("car company:", len(car_company))

#--Tuple practice
# a= ("apple", "banana", "cherry", "orange", "grape", "mango")
# #print banana
# print("Fruit name : ", a[1])
# print("length of a : ",len(a))

#--Remove duplicate entry
#name = ("Yogesh", "Deepak", "Deepak", "Rahul","Aman", "Rahul")
# name_ex = {"Yogesh", "Deepak", "Deepak", "Rahul","Aman", "Rahul"} #--when we store the value in the curly brackets, the python is remove the duplicate entry automatic
# print(name)
# print(tuple(set(name)))

#-take a user input for name and age
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Your name is {name} and your age is {age}")
# print(f"Hello {name} your age is {age}")

#--store website url in variable and print the length of the url and convert to upper case
# url = ("https://www.amazon.in")
# url = input("Please enter your favourite url: ")
# print(type(url))
# print(len(url))
# print(url.upper())
# print(url.replace("https://www.amazon.in","https://www.flipcart.in/"))
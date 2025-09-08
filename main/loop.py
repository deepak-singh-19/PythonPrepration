# --- first program

# name = "Deepak"
# for i in name:
#     print(i)

#---- Second program

# colour = ["Red", "Green", "Black", "Yellow"]
# for i in colour:
#     print(i)
#     for raj in i:
#         print(raj)

#---- Third Program using with range

#for number in range(10):
    # print(number)     # ----- number is start o
    #print(number +1)    # ------ number is start 1

# for number in range(5, 10):
#     print(number + 1)


# ----- even or odd number list
# for number in range(1, 100):
#     print(number)
#     if number % 2 == 0:
#         print("Even number :", number)
#     else:
#         print("Odd number :", number)

# name = 'Deepak Singh'
# for i in name:
#     print(i)

# ---- Print a to z using loop (Small abc)
# for i in range(97, 123):  #- ASCII values for 'a' = 97, 'z' = 122
#     print(chr(i))
#     # print(chr(i), end="")

#----- Print A to Z using for loop (Capital ABC)
# for i in range(64, 91):  #-- ASCII values for 'A' = 65, 'Z' = 90
#     print(chr(i))

#--- Print each character in string
# text = "This is a python"
# for i in text:
#     print(i)

#----- Print Sum of first 10 Natural numbers
# total = 0
# for i in range(0, 10):
#     total += i
#     print("Sum of first 10 numbers :", total)

# ---- Print Multiplication table
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(num, "*", i, "=", num * i)

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even number :", num)
# else:
#     print("Odd number :", num)

# for i in range(0, 50):
#     if i % 2 == 0:
#         print("Even number :", i)
#     else:
#         print("Odd number :", i)

# num  = int(input("Enter a number: "))
# for i in range(0, num):
#     if i % 2 == 0:
#         print("Even number :", i)
#     else:
#         print("Odd number :", i)

# ---- Factorial number
# num = int(input("Enter a number: "))
# fact = 1
#
# for i in range(1, num + 1):
#     fact *= i
#     print("The factorial of", num, "is", fact)

# -----Factorial number program two
# num = int(input("Enter a number: "))
# fact = 1
#
# for i in range(1, num + 1):
#     fact *= i
#
# print(f"Factorial of {num} is {fact}")

#---- star Pattern (Pyramid)
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2*i - 1))
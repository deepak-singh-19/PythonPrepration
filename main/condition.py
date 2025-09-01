# (-) conditional operators
# (<) less than
# (>) greater than
# (<=) less than equal
# (>=) greater than equal
# (==) equal equal
# (!=) not equal

# a = int(input("Enter your age: "))
# print("Your age is:", a)

# print(a<18)
# print(a>18)
# print(a<=18)
# print(a>=18)
# print(a==18)
# print(a!=18)

# if a < 18:
#     print("You are not eligible for the voting:", a)
# else:
#     print("You are eligible for the voting:", a)

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
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#--- vehicle speed -------------------------------

speed = int(input("Enter a vehicle speed Km/Hr: "))
print("Enter a vehicle speed Km/Hr: ", speed)

if speed < 80:
    print("The vehicle speed is low")
elif speed == 80:
    print("The vehicle speed is medium")
else:
    print("The vehicle speed is high")
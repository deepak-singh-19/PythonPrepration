# i = 0
# while (i <= 50):
#     print(i)
#     i = i+1

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
number = 8
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
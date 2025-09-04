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
for number in range(2, 100):
    print(number)
    if number % 2 == 0:
        print("Even number :", number)
    else:
        print("Odd number :", number)
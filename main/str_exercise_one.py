# Validate user input exercise
# 1. username is no more than 12 character
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) >12:
    print(f"{username} is an invalid username")
elif not username.find(" ") == -1:
    print("spaces are not allowed in the username")
elif not username.isalpha():
    print("Digit is not allow in the username")
else:
    print(f"{username} is a valid username")
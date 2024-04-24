#!/usr/bin/python3
#Basic if else structure

a = 100

if a == 100:
    print("a is 100")
else:
    print("a is not 100")


# check if port is secure or not
user_input = input("Enter port number: ")
port = int(user_input)

if port == 443:
    print("Port is secure")
elif port == 22:
    print("Port is secure")
elif port == 8443:
    print("Port is secure")
else:
    print("Port might not secure")


# create simple login system
username = "admin"
password = "12345"

while True:
    user_input = input("Enter username: ")
    pass_input = input("Enter password: ")

    if user_input == username and pass_input == password:
        print("Login successful")
        break
    else:
        print("Login failed")
        continue

# nested if else

user_pw = input("Enter password for checking: ")
pwupper = user_pw.isupper()
pwlower = user_pw.islower()

if len(user_pw) < 15:
    print("Password must be at least 15 characters")

else:
    print("Good password length")

    if pwupper == True:
        print("Password needs lowercase")
    else:
        print("check if there is any lowercase")

        if pwlower == True:
            print("Password needs uppercase")

        else:
            print("Stronger password")

# check if the file contains the word 'break'
with open('story.txt', 'r') as file:
    data = file.readlines()

    for eachline in data:
        if 'break' in eachline:
            print(eachline)

# count the number of 'SUPPORT' in the file
counter = 0
with open('100west.txt', 'r') as file:
    data = file.readlines()

    for eachline in data:
        if 'SUPPORT' in eachline:
            counter += 1

print("Total number of SUPPORT in the file: ", counter)

'''
use this command to cross check the result on terminal
cat 100west.txt | grep -i "SUPPORT" | wc -l
'''


#!/usr/bin/python3
# Getting an input from user

username = input("Enter your name: ")
print(username)

# by default the input function returns a string
age = input("Enter your age: ")
print(type(age))

print("Your age in the next 3 years is: ", int(age) + 3)

# append user input into a list
favorite_movies = []


for each_round in range(3):
    movie = input("Enter your favorite movie: ")
    favorite_movies.append(movie)

print("your favorite movies are: ", favorite_movies)

# add ask user to register service and display the service as key pair
serivces = {}

input("Enter service information for service registration")

for each_round in range(3):
    service_name = input("Enter the service name you want to register: ")
    service_port = input("Enter the service port: ")
    serivces[service_name] = service_port

print("The services you registered are: ", serivces)


# increment number using for loop
count = 0

for each_num in range(3):
    count += 1
    # count = count + 1

print(count)

# sum number from user input
total = 0

for each_round in range(3):
    number = int(input("Enter a number: "))
    total += number

print("The total of the numbers you entered is: ", total)




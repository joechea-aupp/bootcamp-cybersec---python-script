#!/usr/bin/python3
#Basic for loop structure

# define specific range of numbers to iterate through
for number in range(5):
    print(number)

# definee specific start range of numbers to iterate through
# the end range is n - 1
for number in range(5, 10):
    print(number)


names = ['John', 'Paul', 'George', 'Ringo']

# iterate through a list of names
for name in names:
    print('Hi ' + name + ', how are you?')


# string can also be iterated through
apple = 'apple'
for letter in apple:
    print(letter)

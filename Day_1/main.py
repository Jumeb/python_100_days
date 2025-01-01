print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

print('Hello World!\nHello World!\nHello World!')

# This a cool method for printing and getting input from the user

print('Hello' + input('What is your name?') + '!')

# Using the len() function to get the length of the input

print(len(input('What is your name? ')))

# Using variables to store the input and then print it

name = input('What is your name? ')

# Coding exercise 1.3

a = input('a: ')
b = input('b: ')

temp = a
a = b
b = temp

print('a: ' + a)
print('b: ' + b)
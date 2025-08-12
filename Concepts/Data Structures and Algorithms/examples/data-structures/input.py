"""
How to get input, how to typecast, and how to print ints with strs
"""

print("Hello, What is your name")
name = input()
print('Hello ' + name)
print('What is your age?')
age = input()
print('You will be ' + str(int(age) + 1) + ' in a year')
print('Are you excited to be', age, 'in a year?')
"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""


def ask():
    name = input('Please enter your name:')
    age = input('Please enter your age:')
    if int(age) < 1:
        print('Invaild input')
    elif int(age) <= 100:
        rest_yrs = 100 - int(age)
        year = 2019 + rest_yrs
        print("Name:", name, "\nIn", year, "you will turn 100 years old.")
    else:
        print('You already over 100 years! Your current age is:', age)


ask()


"""

Samle Solution:

name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)

"""


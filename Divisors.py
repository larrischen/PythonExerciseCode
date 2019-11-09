"""
Create a program that asks the user for a number and
then prints out a list of all the divisors of that number.
"""

num = int(input('Please enter a number'))
final = list()
for a in range(num):
    if a == 0:
        pass
    elif num % a == 0:
        final.append(a)
print(final)



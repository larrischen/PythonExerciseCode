"""
Ask the user for a number.
Depending on whether the number is even or odd,
print out an appropriate message to the user.
"""


def odd_or_even():
    while True:
        num = int(input('Please enter a number:'))
        if num < 0:
            print('Invaild input, please enter again!')
            continue
        elif num % 2 == 0:
            print(num, 'is a even number')
        else:
            print(num, "is odd number")


odd_or_even()


"""
Sample Code:

num = input("Enter a number: ")
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")
"""

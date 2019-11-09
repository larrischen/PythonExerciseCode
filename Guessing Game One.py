"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random


def guess_num():
    ran = random.randint(1, 9)
    print('A random number has been generated!')
    count = 0
    while True:
        num = int(input('Please enter your number:'))
        if num == ran:
            print('The random number is', ran)
            print('You are right!')
            break
        elif num > ran:
            print("Your guess is bigger than the number!")
            count += 1
            print('You have tried', count, ' times!')
            continue
        elif num < ran:
            print("Your guess is smaller than the number!")
            count += 1
            print('You have tried', count, 'times!')
            continue


guess_num()



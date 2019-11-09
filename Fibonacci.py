"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the
next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


def gen_a():
    count = int(input('How many numbers do you want to generate?'))
    n = 1
    if count == 0:
        a = []
    elif count == 1:
        a = [1]
    elif count == 2:
        a = [1, 1]
    elif count > 2:
        a = [1, 1]
        while n < count-1:
            a.append(a[n] + a[n-1])
            n += 1
    print(a)

gen_a()








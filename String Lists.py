"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""
target = str(input('Please enter a word:'))

rev_tar = target[::-1]
if target == rev_tar:
    print(True)
else:
    print(False)




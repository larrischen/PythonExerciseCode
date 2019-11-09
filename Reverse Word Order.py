"""
asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""


def reverse_string():
    org = str(input('Please enter a sentence:'))
    print('Original sentence:', org)
    spt = org.split()[::-1]
    after = ' '.join(spt)
    print('After is:', after)


reverse_string()
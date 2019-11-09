"""
Write a program (function!) that takes a list and returns a new list
that contains all the elements of the first list minus all the duplicates.
Write two different functions to do this - one using a loop and constructing a list,
and another using sets.
"""
import random

lst_a = [random.randrange(1, 15) for _ in range(0, 20)]
print(lst_a)

# way 1
lst_b = list(set(lst_a))
print(lst_b)

# way 2
lst_c = list()
for a in lst_a:
    if a not in lst_c:
        lst_c.append(a)
lst_c.sort()
print(lst_c)


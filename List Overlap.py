"""
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
write a program that returns list contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
final = list()
for num1 in a:
    for num2 in b:
        if num1 == num2:
            final.append(num1)
# use set() to distinct duplicated numbers
print(list(set(final)))



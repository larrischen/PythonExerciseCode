"""
Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest)
and another number. The function decides whether or not the
given number is inside the list and returns (then prints) an appropriate boolean.
Use binary search.
"""

import random


def guess_num():
    a = random.sample(range(10), 5)
    a.sort()
    print(a)
    while True:
        g = input("please enter a number, or enter 'q' to quit")
        if g == 'q':
            break
        elif int(g) in a:
            print('True')
            continue
        elif int(g) not in a:
            print("False")
            continue


guess_num()

# binary search
"""
def find(ordered_list, element_to_find):
  start_index = 1
  end_index = len(ordered_list) - 1
  
  while True:
    middle_index = (end_index - start_index) / 2
    
    if middle_index < start_index or middle_index > end_index or middle_index < 0:
      return False
    
    middle_element = ordered_list[middle_index]
    if middle_element == element_to_find:
      return True
    elif middle_element < element_to_find:
      end_index = middle_index
    else:
      start_index = middle_index
  
if __name__=="__main__":
  l = [2, 4, 6, 8, 10]
  print(find(l, 5)) # prints False
  print(find(l, 10)) # prints True
  print(find(l, -1)) # prints False
  print(find(l, 2)) # prints True
"""
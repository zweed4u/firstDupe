#!/usr/bin/python3
import time
from typing import List

"""
Given an array that contains only numbers in range from
1 to the length of the array, find the first duplicate
number for which the second occurrence has the minimal
index. Returns the number NOT the index of the first duplicate.
If no duplicates return -1
"""

test_array = [2, 1, 3, 4, 5, 6, 3, 5, 9]
# make sure the array abides by the problem statement rules 1-N,
# where N is the length of the array
assert max(test_array) <= len(test_array)


def first_duplicate(array: List[int]) -> int:
    # use set datastructure to use uniqueness property for checking
    occurred_numbers = set()
    for number in array:
        if number in occurred_numbers:
            return number
        occurred_numbers.add(number)
    return -1


print(first_duplicate(test_array))

#!/usr/bin/python3
import time
import random
from typing import List

"""
Given an array that contains only numbers in range from
1 to the length of the array, find the first duplicate
number for which the second occurrence has the minimal
index. Returns the number NOT the index of the first duplicate.
If no duplicates return -1
"""


def first_duplicate(array: List[int]) -> int:
    # use set datastructure to use uniqueness property for checking
    occurred_numbers = set()
    for number in array:
        if number in occurred_numbers:
            return number
        occurred_numbers.add(number)
    return -1


def main():
    number_of_elements = 10
    test_array = [
        random.randint(1, number_of_elements) for i in range(number_of_elements)
    ]
    # make sure the array abides by the problem statement rules 1-N,
    # where N is the length of the array
    assert max(test_array) <= len(test_array)  # redundant as randint() considers max

    print(test_array)
    start = time.time()
    print(first_duplicate(test_array))
    print(
        f"Finding first duplicate in array took: {(time.time()-start)*1000} milliseconds"
    )


if __name__ == "__main__":
    main()

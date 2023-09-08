"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    inp_set = set(inp)
    least_common = inp[0]
    most_common = inp[0]
    result_dict = {}
    for el in inp_set:
        result_dict[el] = inp.count(el)
        if inp.count(el) < inp.count(least_common):
            least_common = el
        if inp.count(el) > inp.count(most_common):
            most_common = el
    return most_common, least_common

"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List
from itertools import product


def combinations(*args: List[Any]) -> List[List]:
     # result = []
    # temp_list = []

    # def generate_combinations(list_index):
    #     if list_index == len(args):
    #         result.append(temp_list.copy())
    #         return result
    #     for el in args[list_index]:
    #         temp_list.append(el)
    #         generate_combinations(list_index + 1)
    #         temp_list.pop()
    #
    # generate_combinations(0)
    # return result
    result = list(product(*args))
    return [list(combination) for combination in result]


for results in combinations([[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
    print(results)


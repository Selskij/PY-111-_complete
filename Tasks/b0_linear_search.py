"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    print(arr)
    lst_num = list(enumerate(arr,0))

    min_ = min(lst_num, key = lambda i: i[1])

    return min_[0]

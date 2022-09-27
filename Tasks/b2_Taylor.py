"""
Taylor series
"""
from typing import Union
import math
from itertools import count

EPSILON = 0.0001

def get_item_n(x,n):
    return x ** n / math.factorial(n)

def get_si(x,n):
    return ((-1)**n) * (x ** (2*n + 1)) / math.factorial((2*n)+1)

# def get_sin_x(x):
#     sum_ = 0
#     for i in count(1,1):
#         current_item = get_item_n(x,i)
#         sum_+= current_item
#         if abs(current_item) <= EPSILON:
#             return sum_

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    sum_ = 1
    for n in count(1, 1):
        current_item = get_item_n(x,n)
        sum_ += current_item
        if current_item <= EPSILON:
            break
    return sum_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sum_ = 0
    for n in count(0, 1):
        current_item = get_si(x, n)
        print(current_item)
        sum_ += current_item

        if abs(current_item) <= EPSILON:
            break
    return sum_


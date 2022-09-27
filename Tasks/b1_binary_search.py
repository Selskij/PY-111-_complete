from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    left_border = 0
    right_border = len(arr) - 1

    # №2# Добавить уже после прописания всех if и  elif
    while left_border <= right_border: # пока левая граница меньше чем правая

        middle_index = left_border + (right_border - left_border) // 2  # // - деление без остатка
        middle_value = arr[middle_index]
    # №2# Добавить уже после прописания всех if и  elif

    # №1
        if middle_value == elem:
            return middle_index  # случай когда средняя граница чудом попала в нужный элемент

        elif middle_value < elem:  # если искомый элемент больше чем средняя граница (отсортированно по возрастанию)
                                   # то левая граница смещается на место среднего эелемента
            left_border = middle_index + 1
        elif middle_value > elem:
            right_border = middle_index - 1
    # №1

        #print(elem, arr)
    return None

from typing import Sequence, Optional


from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    right_border = len(arr) - 1
    left_border = 0
    if right_border < left_border:
        return None
    else:
        middle_index = left_border + (right_border - left_border) // 2
        middle_value = arr[middle_index]
        if middle_value > elem:
            return binary_search(elem, arr[:middle_index])
        elif middle_value < elem:
            return binary_search(elem, arr[middle_index::])
        else:
            return middle_index

from typing import List
from random import choice, randint



# def sort(container: List[int]) -> List[int]:
#     """
#     Sort input container with quick sort
#
#     :param container: container of elements to be sorted
#     :return: container sorted in ascending order
#     """
#     if not container:
#         return container
#
#     pivot = choice(container) # Неким образом определяем опорный элемент
#


# Три слогаемых : Первое - рекурсия сортировки для элементов меньше начального,
# второе - для элементов равных начальному, третье - рекурсия для элементов больше начального
#
#
#     return sort([v for v in container if v < pivot]) \
#            + [v for v in container if v == pivot] \
#            + sort([v for v in container if v > pivot])


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    def _sort (left_border, right_border) -> None:
        if left_border >= right_border:
            return

        random_index = randint(left_border, right_border)
        pivot = container[random_index] # Неким образом определяем опорный элемент

        i, j = left_border, right_border # Идем по массиву двумя счетчиками – слева направо и справа налево


# Всё что больше pivot после первого прохода займёт позиции справа, после чего сам pivot
# перемещается направо и становится на позицию меньшего из новой последовательности
# После этого операция повторяется заново

        while i <= j:
            while container[i] < pivot:
                i += 1 # Увеличиваем левый счетчик, пока он не встретит элемент больше или равный опорному

            while container[j] > pivot:
                j -= 1 # Уменьшаем правый счетчик, пока он не встретит элемент меньше или равный опорному

            if i <= j: # если i и j пересеклись - производим обмен
                container[i], container[j] = container[j], container[i] # Меняем элементы местами
                i += 1
                j -= 1
# Продолжаем уменьшать счетчики и менять элементы аналогичным образом, пока счетчики не встретятся\
# – получаем индекс элемента, левее которого все элементы меньше или равны опорному, а правее – больше опорного
        _sort(left_border, j) # Запускаем рекурсивно алгоритм от части левее опорного элемента
        _sort(i, right_border) # и правее опорного элемента
    _sort(0, len(container) - 1)
    return container









    _sort(0, len(container) - 1)
        #choice(container[left_border: right_border])

"""
My little Queue
"""
from typing import Any

#append -> O(1)
#pop(-1) -> O(1)
#insert() -> O(N)
#del() -> O(N)

'''enqueue - O(N)
    dequeue - O(1)'''

queue = []
#queue_priority = []

def enqueue(elem: Any) -> None: # Как append а значит O(1)
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """


    #reversed_index = -ind - 1
    queue.insert(0, elem)
    #queue.append(elem)
    #reversed_queue = reversed(queue)
    print(queue)
    return None


def dequeue() -> Any: # O(N) т.к извлекаем из конца и двигаем все элементы
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    if not queue:
        return None
    return queue.pop()
    #return None


def peek(ind: int = 0) -> Any: #O(1)
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    try:
        queue[ind]
    except IndexError:
        return None
    #print(ind)
    reversed_index = -ind - 1
    return queue[reversed_index]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    queue.clear()
    return None

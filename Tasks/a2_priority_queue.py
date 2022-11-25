"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

#append -> O(1)
#pop(-1) -> O(1)
#insert() -> O(N)
#del() -> O(N)

'''enqueue - O(N)
    dequeue - O(1)'''
# Одна очередь
queue = []
queue_priority = []

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    enqueue_item = {
        "elem": elem,
        "priority": priority
    }
    if not queue_priority:
        queue_priority.append(enqueue_item)
        return None # Если нет queue_priority то вставляем элемент и закрываем список

    for index, current_item in enumerate(queue_priority):
        if enqueue_item["priority"] >= current_item["priority"]:
            queue_priority.insert(index, enqueue_item)
            break
    else:
        # index == len(queue_priority)-1:
        queue_priority.append(enqueue_item)
        # Если прошли всю очередь до конца и не добавили приоритет. Случай с нулевым элементом
        #Самым приоритетным


    #print(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if not queue_priority:
        return None

    return queue_priority.pop()["elem"]


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    reversed_index = -ind - 1
    return queue_priority[reversed_index]["elem"]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    queue_priority.clear()
    return None

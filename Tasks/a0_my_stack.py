"""
My little Stack
"""
from typing import Any

stack = []

def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed элемент который необходимо добавить
    :return: Nothing
    """
    stack.append(elem)
    print(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.
    Изъять элемент с вершины стека
    При отсутствии элемента вернуть None
    :return: popped element Изъятый элемент
    """
    if not stack:
        return None

    return stack.pop()


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.
    Позволяет подсмотреть элемент внутри стека без его изъятия
    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
               Индекс элемента (отсчёт начинается  с вершины стека) 0 - вершина, 1 - предпоследний элемент,...
    :return: peeked element or None if no element in this place
            Выбраный элемент. None если не стоит никакого элемента
    """
    #reversed_stack = reversed(stack)
    reversed_index = -ind -1

    try:
        stack[ind]
    except IndexError:
        return None
    return stack[reversed_index]


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    stack.clear()

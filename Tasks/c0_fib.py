def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n-1) + fib_iterative(n-2)


def fib_iterative(n: int) -> int: # O(N)
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0: # это первое число Фиббоначи
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1

    for _ in range (1, n): # либо range (n-1)
        # sum_ = a + b кустарный вариант решения
        # a = b
        # b = sum_
        a, b = b, a+b


    print(n)
    return b


#Чем отличаются итеративный Фибоначи и рекурсивный? Итеративный Фибоначи возвращает n-e
# число, а функция-генератор возвращает первые N числел Фиббоначи.

def generator_fib(n):
    if n < 0:
        raise ValueError

    a = 0
    yield a

    b = 1
    yield b

    for _ in range(1, n):  # либо range (n-1)
        a, b = b, a + b
        yield b

# Найти первые n чисел фиббоначи
# Сложность Функции генератора generator_fib
# Итеративный алгоритм fib_iterative

#_______________________________________________________________________
# Пример того зачем может понадобиться реализация через функцию генератор

N = 10
list_fin_iterative = [fib_iterative(i) for i in range(N)]
#чуть более подробное описание функции выше

# list_fin_iterative = []
# for i in range(N): ------------> сложность O(N)
#     current_number = fib_iterative(i)-----------> сложность O(N)
#     list_fin_iterative.append(current_number)-------> сложность O(N)
list_generator = [num for num in generator_fib(N-1)] # 9 потому что отсчёт идёт с нуля
#чуть более подробное описание функции выше

# generator = generator_fib(N)
# for _ in range (N):-----------> O(N)
#     current_number = next(generator)---------> O(1)

# Посмотрев на две эти реализации скажите какие сложности у 65 строки (fin_iterative) и у
# 72 строки (_generator)
# У 62 - Мы N раз запускаем итеративную функцию,
# А итеративная функция всегда начинает считать сначала. N*N = N^2

# У 63 - Линейное время О(N)
print(list_fin_iterative)
print(list_generator)
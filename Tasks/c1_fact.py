def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    print(n)
    return 0


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    prev_ = n
    for i in range(1,n):  # либо range (n-1)
        current_item =prev_ * (n-i)
        #a, b = b, b-1
        prev_ = current_item
        print(prev_)
    #print(n)
    return prev_

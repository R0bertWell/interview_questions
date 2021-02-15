def fib(n):
    """
    n = quantity of which number fibonacci the function stop
    :param n:   int
    :return:    int
    """
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)

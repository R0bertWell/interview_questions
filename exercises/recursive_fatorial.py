def fatorial(num: int) -> int:
    """
    num E Naturais ( Números *Inteiros* e *positivos* )
    :param num: int
    :return: int
    """
    if num <= 1:
        return 1
    return num*(fatorial(num-1))

print(fatorial(5))
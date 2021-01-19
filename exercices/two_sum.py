def two_sum(args, target):
    """

    :type args: List[int]
    :type target: int
    :rtype: List[int]
    """

    h = {}
    for i, value in enumerate(args):
        n = target - value
        if n not in h:
            h[value] = i
        else:
            return f'{[h[n], i]} values : {n , value}'
    return []
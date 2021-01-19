def add_2_nums(first_list, second_list):
    """
    Ex :
    input:
        first_list = [2, 4, 3]
        second_list = [5, 6, 4]
    output:
        third_list = [7, 0, 8]

    :intype first_list: List[int]
    :intype second_list: List[int]
    :rtype List[int]
    """
    first_num = int("".join(map(str, first_list)))
    second_num = int("".join(map(str, second_list)))
    result = first_num + second_num
    return list(str(result))
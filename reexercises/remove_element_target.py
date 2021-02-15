from typing import List


def remove_target(lis: List[int], target: int):
    i = 0
    while i < len(lis):
        if lis[i] == target:
            del lis[i]
        else:
            i += 1
    return lis


print(remove_target([1, 2, 3, 4, 4, 4, 5, 5, 6], 4))

from typing import List


def two_sum(lis: List[int], target: int):
    dici = {}
    for i, value in enumerate(lis):
        objetive = target - value
        if objetive in dici:
            return [dici[objetive], i]
        dici[value] = i
    return []


print(two_sum([1, 2, 3, 4, 5, 6], 7))

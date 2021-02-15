from typing import List


def remove_element(nums: List[int], val: int):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
        else:
            i += 1
    lens = len(nums)
    return lens

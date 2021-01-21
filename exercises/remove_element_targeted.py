from typing import List


def remove_element(nums: List[int], val: int):
    i = count = lens = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
            count += 1
        else:
            i += 1
    lens = len(nums)
    return lens

from typing import List


def remove_duplicate(nums: List[int]):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = 0
    i = 1
    while i < len(nums):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        i += 1
    return j + 1

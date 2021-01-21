from typing import List


def remove_duplicate(nums: List[int]):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            del nums[i+1]
        else:
            i += 1
    return len(nums)

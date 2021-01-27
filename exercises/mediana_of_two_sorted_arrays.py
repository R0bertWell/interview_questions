from typing import List


def median_of_two_arr(nums1: List[int], nums2: List[int]):
    """
    ex : Inputs : [1,2],[3,4]
    output : 2.5
    cause (2+3)/2 = 2.5, which is a median

    :param nums1: List[int]
    :param nums2: List[int]
    :return: List[int]
    """
    nums3 = nums1 + nums2
    nums3.sort()
    tam = len(nums3)
    if (tam % 2) == 1:
        middle = int(tam/2)
        return nums3[middle]
    else:
        return (nums3[int(tam/2)-1]+nums3[int((tam/2))])/2

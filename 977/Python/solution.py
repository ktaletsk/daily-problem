import pytest
import math
from typing import List
import numpy as np

def find_first_nonnegative(ar, ibegin=None, iend=None):
    if ibegin == None:
        ibegin = 0
    if iend == None:
        iend = len(ar) - 1


    if ibegin > iend:
        return -1

    # Find a middle
    m = ibegin + (iend - ibegin + 1) // 2

    # Check conditions
    if ar[m] >= 0:
        if m == 0 or ((ar[m] >= 0) != (ar[m-1] >= 0)):
            return m
        else:
            return find_first_nonnegative(ar, ibegin, m - 1)
    elif ar[m] < 0:
        return find_first_nonnegative(ar, m + 1, iend)
    else:
        return -1

def sortedSquares(nums: List[int]) -> List[int]:
    # Find the first nonnegative element
    first_nonnegative = find_first_nonnegative(nums, 0, len(nums) - 1)

    # If there are no negative elements, return the squares of the array
    if first_nonnegative == 0:
        return [el*el for el in nums]

    # If there are no positive elements, return the squares of the array
    if first_nonnegative == -1:
        return [el*el for el in nums[::-1]]

    # If there is a mix, use two pointer approach
    p1 = first_nonnegative # pointer to non-negative numbers
    p2 = p1 - 1 # pointer to negative numbers
    result = []
    while (p1 <= len(nums)-1) or (p2 >= 0):
        sq1 = nums[p1]*nums[p1] if (p1 <= len(nums)-1) else float('inf')
        sq2 = nums[p2]*nums[p2] if (p2 >= 0) else float('inf')
        if sq1 <= sq2:
            result.append(sq1)
            p1 += 1
        else:
            result.append(sq2)
            p2 -= 1
    return result

def test_all_positive():
    assert sortedSquares([1,2,3,4,5])==[1,4,9,16,25]

def test_large_random_array():
    x  = np.sort(np.random.randint(-100,100,1000))
    assert np.any(sortedSquares(x) != np.sort(np.square(x))) == False


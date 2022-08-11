from typing import List
import pytest

def binary_search(a: List, ibegin, iend, n: int):
    if ibegin > iend:
        return ibegin

    # Find a middle
    m = ibegin + (iend - ibegin + 1) // 2

    # Check 3 conditions
    if n < a[m]:
        return binary_search(a, ibegin, m - 1, n)
    elif n == a[m]:
        return m
    elif n > a[m]:
        return binary_search(a, m + 1, iend, n)
    else:
        return -1

def searchInsert(nums: List[int], target: int) -> int:
    return binary_search(nums, 0, len(nums) - 1, target)
    
def test_case():
    assert searchInsert([1,3,5,6], 5) == 2
    assert searchInsert([1,3,5,6], 2) == 1
    assert searchInsert([1,3,5,6], 7) == 4
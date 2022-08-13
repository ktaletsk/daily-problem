from typing import List
import pytest

def twoSum(numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1
    while i <= j:
        # We found the solution
        if numbers[i] + numbers[j] == target:
            return [i+1,j+1]
        # Any j for a given i will have even smaller sum
        # So we need to increase i
        elif numbers[i] + numbers[j] < target:
            i += 1
        # Any i for a given j will have even larger sum
        # We need to descrease j
        else:
            j -= 1

def test_1():
    assert twoSum([2,7,11,15], 9) == [1,2]

def test_2():
    assert twoSum([2,3,4], 6) == [1,3]

def test_3():
    assert twoSum([-1, 0], -1) == [1,2]
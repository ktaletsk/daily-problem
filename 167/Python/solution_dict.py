from typing import List
import pytest

def twoSum(numbers: List[int], target: int) -> List[int]:
    d = {}
    i = 0
    while i < len(numbers):
        if numbers[i] in d:
            return [d[numbers[i]] + 1, i + 1]
        d.update({target - numbers[i]: i})
        i += 1

def test_1():
    assert twoSum([2,7,11,15], 9) == [1,2]

def test_2():
    assert twoSum([2,3,4], 6) == [1,3]

def test_3():
    assert twoSum([-1, 0], -1) == [1,2]
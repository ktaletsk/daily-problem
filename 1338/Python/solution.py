from typing import List
import pytest


def minSetSize(arr: List[int]) -> int:
    d = {}

    for el in arr:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1

    counts = list(d.values())
    counts.sort(reverse=True)

    # Greedy
    i = 1
    sum = counts[0]
    while sum < len(arr) // 2:
        sum += counts[i]
        i += 1

    return i


def tests():
    assert minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2
    assert minSetSize([7, 7, 7, 7, 7, 7]) == 1

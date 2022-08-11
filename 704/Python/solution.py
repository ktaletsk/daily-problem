from typing import List
import numpy as np
import pytest


def binary_search(a: List, ibegin, iend, n: int):
    if ibegin > iend:
        return -1

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


def test_random_array():
    size = 500
    # Generate random sorted array of size elements
    ar = np.sort(np.random.randint(0, 10 * size, size)).tolist()

    # Search for all indices in the array
    for i in range(size):
        assert ar[binary_search(ar, 0, size - 1, ar[i])] == ar[i]


def test_val_not_in_the_list():
    ar = [1, 2, 3, 4, 5]
    assert binary_search(ar, 0, 4, 6) == -1

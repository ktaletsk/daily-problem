from typing import List
import numpy as np
import pytest


def binary_search_first_element(a: List, ibegin, iend, n: int):
    if ibegin > iend:
        return -1

    # Find a middle
    m = ibegin + (iend - ibegin + 1) // 2

    # Check 3 conditions
    if n == a[m] and (m == 0 or (a[m] != a[m - 1])):
        return m
    elif n <= a[m]:
        return binary_search_first_element(a, ibegin, m - 1, n)

    elif n > a[m]:
        return binary_search_first_element(a, m + 1, iend, n)
    else:
        return -1


def test_random_array():
    size = 500
    # Generate random sorted array of size elements
    ar = np.sort(np.random.randint(0, 10 * size, size)).tolist()

    # Search for all indices in the array
    for i in range(size):
        assert ar[binary_search_first_element(ar, 0, size - 1, ar[i])] == ar[i]


def test_val_not_in_the_list():
    ar = [1, 2, 3, 4, 5]
    assert binary_search_first_element(ar, 0, 4, 6) == -1


def test_finding_the_first_element_when_repeated():
    ar = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8]
    assert binary_search_first_element(ar, 0, len(ar) - 1, 3) == 3

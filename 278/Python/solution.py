from typing import List
from xmlrpc.client import Boolean
import pytest

bad = 4

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= bad


def binary_search_first_element(ibegin, iend):
    if ibegin > iend:
        return -1

    # Find a middle
    m = ibegin + (iend - ibegin + 1) // 2

    # Check conditions
    if isBadVersion(m) == True:
        if m == 1 or (isBadVersion(m) != isBadVersion(m - 1)):
            return m
        else:
            return binary_search_first_element(ibegin, m - 1)
    elif isBadVersion(m) == False:
        return binary_search_first_element(m + 1, iend)
    else:
        return -1


def firstBadVersion(n: int) -> int:
    return binary_search_first_element(1, n)


def test_standard():
    assert firstBadVersion(5) == 4

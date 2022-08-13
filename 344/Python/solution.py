from typing import List
import pytest

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    begin = 0
    end = len(s) - 1
    while begin < end:
        s[begin], s[end] = s[end], s[begin]
        begin += 1
        end -= 1

def test_reverse_1():
    s = ["h","e","l","l","o"]
    reverseString(s)
    assert s == ["o","l","l","e","h"]

def test_reverse_2():
    s = ["H","a","n","n","a","h"]
    reverseString(s)
    assert s == ["h","a","n","n","a","H"]
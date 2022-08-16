import pytest


def reverseWords(s: str) -> str:
    result = ""
    ibegin = 0
    iend = ibegin
    while ibegin < len(s):
        while (iend < len(s)) and (s[iend] != " "):
            iend += 1

        result += s[ibegin:iend][::-1]

        if iend < len(s):
            result += " "

        ibegin = iend + 1
        iend = ibegin

    return result


def test_lc():
    assert reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"


def test_lc():
    assert reverseWords("God Ding") == "doG gniD"

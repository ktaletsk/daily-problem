class Solution():
    def plusOne(self, digits):
        result = []
        add = 1
        for i in digits[::-1]:
            sum = i + add
            i = sum % 10
            add = sum // 10
            result.append(i)
        if add != 0:
            result.append(add)
        return result[::-1]

def test_299():
    assert Solution().plusOne([2, 9, 9]) == [3, 0, 0]

def test_0():
    assert Solution().plusOne([0]) == [1]

def test_9():
    assert Solution().plusOne([9]) == [1, 0]

def test_159():
    assert Solution().plusOne([1, 5, 9]) == [1, 6, 0]
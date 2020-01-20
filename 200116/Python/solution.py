class Solution(object):
    def findDisappearedNumbers(self, nums):
        return list(set(range(1,len(nums)+1)) - set(nums))

nums = [4, 6, 2, 6, 7, 2, 1]

def test():
    assert Solution().findDisappearedNumbers(nums) == [3, 5]
from typing import List
    
def moveZeroes(nums: List[int]) -> None:
    """Use two-pointer solution for doing the operation in-place"""
    p1 = 0 # writing
    p2 = 0 # reading
    while p2 < len(nums):
        if nums[p2] != 0:
            nums[p1] = nums[p2]
            p1 += 1
        p2 += 1
    
    while p1 < len(nums):
        nums[p1] = 0
        p1 += 1

def test_array():
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    assert nums == [1,3,12,0,0]

def test_only_zeros():
    nums = [0]
    moveZeroes(nums)
    assert nums == [0]
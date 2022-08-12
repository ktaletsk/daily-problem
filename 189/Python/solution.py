from typing import List

def reverse(nums: List[int], ibegin: int, iend: int) -> None:
    while ibegin < iend:
        nums[ibegin], nums[iend] = nums[iend], nums[ibegin]
        ibegin += 1
        iend -= 1

def rotate(nums: List[int], k: int) -> None:
    k = k % len(nums)
    reverse(nums, len(nums)-k, len(nums)-1)
    reverse(nums, 0, len(nums)-k-1)
    reverse(nums, 0, len(nums)-1)

def test_ten():
    size = 10
    shift = 3
    x = [i+1 for i in range(size)]
    rotate(x, shift)
    assert x==[(i-shift)%size+1 for i in range(size)]
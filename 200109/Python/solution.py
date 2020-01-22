def longest_consecutive(nums):
    # convert list to set (Complexity: O(n))
    s = set(nums)
    
    max_len = 0
    # Iterate through the set
    # (1) Check if element is the beginning of the set (Complexity: O(n))
    # (2) Iterate through the sequences from beginning to the end (Total complexity: O(n))
    for i in s: 
        # Check if the current element is the begging of a sequence
        if i-1 not in s:
            # Calculate sequnce length
            l = 1
            # Keep checking the next element
            while i+1 in s:
                i += 1
                l += 1
            # Update the max length if current sequnce is longer
            if l > max_len:
                max_len = l
    return max_len

def test_1():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4

def test_2():
    assert longest_consecutive([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]) == 5

def test_3():
    assert longest_consecutive([32, 15, 11, 14, 31, 33, 12, 9]) == 3
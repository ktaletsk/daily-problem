def find_continuous_k_naive(l, k):
    """
    Naive solution
    Iterate through elements of the list and build subarrays forward
    Check the sum of which sub-array as you go
    Complexity: O(n^2)
    """
    results = []
    for i in range(len(l)):
        sum = 0
        j = i
        while j<len(l):
            sum += l[j]
            if sum == k:
                results.append(l[i:j+1])
            elif sum > k:
                break
            j += 1
    return results

def find_continuous_k_efficient(l, k):
    # Build array of cumulative sums (Complexity: O(n))
    cumulative = []
    running_sum = 0
    for el in l:
        running_sum += el
        cumulative.append(running_sum)

    # Put cumulative array into dictionary (Complexity O(n))
    # Where key is the cumulative sum
    # And value is index in the cumulative and original array
    d = {0: [0]}
    for i, el in enumerate(cumulative):
        # in case if original array contains 0
        # the dictionary value needs to hold an array
        if el in d:
            d[el].append(i+1)
        else:
            d.update({el: [i+1]})

    # Iterate through elements of the original array (el1) and add predefined sum k
    # If element equal to el2 = (el1 + k) exists in the dictionary
    #  then the sequence going from d[el1]->d[el2] with predefined sum exists in the original array
    # Complexity: O(n)
    results = []
    for key in d:
        if key+k in d:
            for m in d[key]:
                for n in d[key+k]:
                    results.append(l[m:n])
    return results

def test_original():
    assert find_continuous_k_naive([1, 3, 2, 5, 7, 2], 14) == [[2, 5, 7], [5, 7, 2]]
    assert find_continuous_k_efficient([1, 3, 2, 5, 7, 2], 14) == [[2, 5, 7], [5, 7, 2]]

def test_12():
    assert find_continuous_k_naive([0, 2, 2, 4, 1, 3, 1, 6, 2, 1, 4, 4], 24) == [[2, 4, 1, 3, 1, 6, 2, 1, 4]]
    assert find_continuous_k_efficient([0, 2, 2, 4, 1, 3, 1, 6, 2, 1, 4, 4], 24) == [[2, 4, 1, 3, 1, 6, 2, 1, 4]]

def test_100():
    l = [48, 57, 28, 78, 19, 40, 77, 86, 41, 87, 23, 24, 0, 35, 0, 38, 53, 80, 44, 38, 31, 17, 46, 17,
         31, 3, 48, 94, 72, 45, 94, 66, 40, 1, 24, 95, 33, 75, 97, 51, 86, 24, 93, 20, 66,  2, 24, 49,
         26, 75,  0, 81, 24, 33, 27,  8, 89, 81, 43, 78, 89,  1, 17, 39, 92, 52, 37, 76, 91, 38,  9, 95,
         47, 51, 45, 58, 99, 27, 36, 84, 81, 30, 33, 15, 90, 86, 51, 94, 70, 24, 71, 33,  9, 50, 47, 89,
         82,  2,  2,  3]
    k = 1279
    assert find_continuous_k_naive(l, k) == [[95, 47, 51, 45, 58, 99, 27, 36, 84, 81, 30, 33, 15, 90, 86, 51, 94, 70, 24, 71, 33, 9, 50]]
    assert find_continuous_k_efficient(l, k) == [[95, 47, 51, 45, 58, 99, 27, 36, 84, 81, 30, 33, 15, 90, 86, 51, 94, 70, 24, 71, 33, 9, 50]]

def test_with_zeros():
    # Special case of 0-s in the results
    assert find_continuous_k_naive([9, 0, 6, 8, 2, 3, 5, 2, 2, 7, 6, 6], 26) == [[0, 6, 8, 2, 3, 5, 2], [6, 8, 2, 3, 5, 2]]
    assert find_continuous_k_efficient([9, 0, 6, 8, 2, 3, 5, 2, 2, 7, 6, 6], 26) == [[0, 6, 8, 2, 3, 5, 2], [6, 8, 2, 3, 5, 2]]

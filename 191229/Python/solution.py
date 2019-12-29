def find_min_max(nums):
    if nums[0]<nums[1]:
        min = nums[0]
        max = nums[1]
    else:
        min = nums[1]
        max = nums[0]

    for i in range(len(nums)-2):
        if nums[i+2] < min:
            min = nums[i+2]
        elif nums[i+2] > max:
            max = nums[i+2]

    return (min, max)

def main():
    print(find_min_max([3, 5, 1, 2, 4, 8]))

if __name__== "__main__":
    main()
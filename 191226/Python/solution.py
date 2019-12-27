def jumps(array):
    possible_jumps = min(array[0], len(array))
    return [array[i+1:] for i in range(possible_jumps)] #can jump 1 ... possible_jumps places

def jumpToEnd(nums):
    nums = [nums]
    counter = 0
    while (min([len(array) for array in nums]))>1:
        nums = [item for sublist in [jumps(array) for array in nums] for item in sublist]
        counter+=1
    return counter

def main():
    print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))

if __name__== "__main__":
    main()
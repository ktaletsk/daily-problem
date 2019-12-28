def checkIfhIndexIsAtLeast(index, publications):
    return sum([p-index>=0 for p in publications])>=index

def hIndex(publications):
    h = max(publications)
    while not checkIfhIndexIsAtLeast(h, publications):
        h=h-1
    return h

def main():
    print(hIndex([5, 3, 3, 1, 0]))

if __name__== "__main__":
    main()
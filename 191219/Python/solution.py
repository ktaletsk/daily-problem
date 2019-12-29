def getBonuses(performance):
    return [1 +
            ((1 if performance[i]>performance[i-1] else 0) if i>0 else 0) + 
            ((1 if performance[i]>performance[i+1] else 0) if i<len(performance)-1 else 0) for i in range(len(performance))]

def main():
    print(getBonuses([1, 2, 3, 2, 3, 5, 1]))

if __name__== "__main__":
    main()
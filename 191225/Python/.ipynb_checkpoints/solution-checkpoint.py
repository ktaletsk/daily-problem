from collections import defaultdict
import copy

def get_next(current, d, finish):
    flag=False
    if len(d[current])==1: 
        if d[current][0]==finish and len(d.keys())==1:
            flag= True
        else:
            new_d = copy.deepcopy(d)
            new_current = d[current][0]
            new_d.pop(current)
            flag=get_next(new_current, new_d, finish)
    elif len(d[current])>1:        
        for index, c in enumerate(d[current]):
            new_d = copy.deepcopy(d)
            new_d[current].pop(index)
            new_current = c
            flag=get_next(new_current, new_d, finish)
            
    return flag

def can_get_chained(input):
    words = [(word[0], word[-1]) for word in input]
    
    d = defaultdict(list)
    for k, v in words:
        d[k].append(v)

    #Start with any word
    start = list(d.items())[0][0]
    
    return get_next(start, d, start)

def main():
    can_get_chained(['eggs', 'karat', 'apple', 'snack', 'tuna'])

if __name__== "__main__":
    main()
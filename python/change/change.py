from itertools import combinations_with_replacement

def find_fewest_coins(coins, target):
    
    if target < 0 :
        raise ValueError("target can't be negative")
    
    if target == 0:
        return []
    
    for i in range(1, target + 1, 1):
        # do combinations with i elements
        comb = combinations_with_replacement(coins, i)

        for c in comb:
            if sum(c) == target:
                return list(c)
            
    raise ValueError("can't make target with given coins")

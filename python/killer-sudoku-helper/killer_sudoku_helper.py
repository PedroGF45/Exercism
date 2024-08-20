from itertools import combinations as comb

def combinations(target, size, exclude):
    com = comb(range(1, target + 1, 1), size)

    ans = []

    for c in com:
        if (sum(c) == target):
            excluded = False
            for i in c:
                if i in exclude:
                    excluded = True
            if excluded: 
                continue
            else:
                ans += [list(c)]

    return ans
    
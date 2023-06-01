def factors(value):
    
    if value == 1:
        return []
    
    res = []
    prime = 2

    while value > 1:
        while (value % prime == 0):
            value = int(value / prime)
            res += [prime]
        prime += 1

    return res

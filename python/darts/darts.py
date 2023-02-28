from math import sqrt

def score(x, y):
    if sqrt(x**2 + y**2) <= 1:
        return 10
    elif sqrt(x**2 + y**2) <= 5:
        return 5
    elif sqrt(x**2 + y**2) <= 10:
        return 1
    else: 
        return 0
    
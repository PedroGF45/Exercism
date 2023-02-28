from math import sqrt

def score(x, y):

    # using Pythagorean theorem to determine the value of the hypotenuse
    hypotenuse = sqrt(x**2 + y**2)
    
    if hypotenuse <= 1:
        return 10
    elif hypotenuse <= 5:
        return 5
    elif hypotenuse <= 10:
        return 1
    else: 
        return 0
    
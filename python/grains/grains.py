def square(number):
    if (number <= 64 and number > 0):
        return 2**(number -1)
    raise ValueError("square must be between 1 and 64")

def total():
    squares = 64
    i = 0
    res = 0
    while i < squares:
        res += 2**i
        i += 1
    return res

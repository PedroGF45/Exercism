def square_of_sum(number):
    i = 1
    sum = 0
    while i <= number:
        sum += i
        i += 1
    return sum**2


def sum_of_squares(number):
    i = 1
    sum = 0
    while i <= number:
        sum += i**2
        i += 1
    return sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

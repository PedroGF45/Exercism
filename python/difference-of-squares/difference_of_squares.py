def square_of_sum(number):
    i = 1
    squares_sum = 0
    while i <= number:
        squares_sum += i
        i += 1
    return squares_sum**2


def sum_of_squares(number):
    i = 1
    sum_squares = 0
    while i <= number:
        sum_squares += i**2
        i += 1
    return sum_squares


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

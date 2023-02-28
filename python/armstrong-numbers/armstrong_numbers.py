def is_armstrong_number(number):

    # converts number to a string
    string_number = str(number)

    # sum each digit each raised to the power of the total number of digits
    sum_digits = sum(map(lambda x: int(x)**len(string_number), string_number))

    # outputs true if is armstrong number
    return bool(sum_digits == number)

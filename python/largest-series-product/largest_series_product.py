def largest_product(series, size):
    
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    elif size < 0:
        raise ValueError("span must not be negative")
    elif not series.isdigit():
        raise ValueError("digits input must only contain digits")
    
    if size == 1:
        return series[0]
    if len(series) == 1:
        return int(series[0])
    
    current_index = 0
    max_product = 0

    while current_index + size - 1 < len(series):

        product = int(series[current_index])

        for digit in series[current_index + 1 : current_index + size]:

            product *= int(digit)

        if product > max_product: max_product = product

        current_index += 1

    return max_product

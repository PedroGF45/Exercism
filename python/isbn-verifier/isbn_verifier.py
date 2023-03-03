def is_valid(isbn):
    # Remove hifens and transfrom to a list
    isbn_clean = isbn.replace('-', '')
    
    # Check if all elements except last is int
    if not isbn_clean[:-1].isdigit():
        return False

    # if not 10 character, not valid
    if len(isbn_clean) != 10:
        return False

    isbn_clean = list(isbn_clean)

    # Check if last digit is 'X' or digit
    if isbn_clean[-1] == 'X':
        isbn_clean[-1] = '10'
    elif not isbn_clean[-1].isdigit():
        return False
    
    # Do the calculations
    sum_val = 0
    for i in range(10, 0, -1):
        sum_val += i * int(isbn_clean[10-i])
    
    # Check valdiation
    return sum_val % 11 == 0

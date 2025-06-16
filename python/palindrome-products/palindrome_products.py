from itertools import combinations_with_replacement

def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    _check_factors(min_factor, max_factor)

    palindromes = []
    factors = []
    list_combinations = list(combinations_with_replacement(range(min_factor, max_factor+1), 2))

    for (i, j) in list_combinations:
        if _is_palindrome(i * j):  
            if len(palindromes) == 0 or palindromes[0] < i*j:
                palindromes = [i*j]
                factors = [[i, j]]
            elif palindromes[0] == i*j:
                factors += [[i, j]]

    return palindromes[0] if len(palindromes) == 1 else None, factors


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    _check_factors(min_factor, max_factor)

    palindromes = []
    factors = []
    list_combinations = list(combinations_with_replacement(range(min_factor, max_factor+1), 2))

    for (i, j) in list_combinations:
        if _is_palindrome(i * j):  
            if len(palindromes) == 0 or palindromes[0] > i*j:
                palindromes = [i*j]
                factors = [[i, j]]
            elif palindromes[0] == i*j:
                factors += [[i, j]]

    return palindromes[0] if len(palindromes) == 1 else None, factors


def _check_factors(min_factor: int, max_factor: int):
    if min_factor > max_factor:
        raise ValueError('min must be <= max')
    
def _is_palindrome(number: int):

    if 0 < number < 10:
        return True
    
    number_str = str(number)

    for letter_index in range(int(len(number_str) / 2)):
        
        if number_str[letter_index] != number_str[(letter_index + 1) * (-1)]:
            return False
        
    return True
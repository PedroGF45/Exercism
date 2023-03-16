def prime(number):
    
    # there's no negative or 0th prime numbers
    if number < 1:
        raise ValueError('there is no zeroth prime')
    
    prime_numbers = [2]
    i = 3
    while len(prime_numbers) < number:

        # if number is not divisible by any of the antecessors in prime_numbers list than it's a prime number
        if all(map(lambda x: i % x != 0, prime_numbers)):
            prime_numbers += [i]
            i += 1
        else:
            i += 1
    
    return prime_numbers[number - 1]

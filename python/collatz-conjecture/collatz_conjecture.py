def steps(number):
    
    # if number is 0 or negative return error
    if number <= 0:
        raise ValueError('Only positive integers are allowed')
    
    steps = 0
    while number != 1:

        #if number is even divide by 2
        if number % 2 == 0:
            number /= 2
        # if number is odd
        else:
            number =  number * 3 + 1
        
        steps += 1
    
    return steps

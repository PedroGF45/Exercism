def convert(number):
    
    # check if number isn't a factor for any of the numbers
    if (number % 3 != 0 and number % 5 != 0 and number % 7 != 0):
        return str(number)

    raindrops = {
        '3': 'Pling',
        '5': 'Plang',
        '7': 'Plong'
    }

    res = ''

    for factor in raindrops:
        if number % int(factor) == 0:
            res += raindrops[factor]
    
    return res

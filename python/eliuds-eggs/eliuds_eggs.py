def egg_count(display_value):
    
    eggs = 0
    power = 0

    while (2 ** power <=  display_value):
        power += 1

    power -= 1

    while (power >= 0):
        
        if (display_value >= 2 ** power):
            display_value -= 2 ** power
            eggs += 1

        power -= 1
        
    return eggs

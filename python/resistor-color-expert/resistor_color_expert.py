COLORS = ['black',
            'brown',
            'red',
            'orange',
            'yellow',
            'green',
            'blue',
            'violet',
            'grey',
            'white']
    
TOLERANCE = {'grey': 0.05,
                'violet': 0.1,
                'blue': 0.25,
                'green': 0.5,
                'brown': 1,
                'red': 2,
                'gold': 5,
                'silver': 10}

def resistor_label(colors):

    # one label is 0 ohms
    if (len(colors)) == 1:
        return '0 ohms'
    
    if len(colors) == 4: # 4 band resistor

        # get variables
        first_color, second_color, multiplier_color, tolerance_color = colors

        # get values from its index's constants
        all_colors = f'{COLORS.index(first_color)}{COLORS.index(second_color)}'

    else: # 5 band resistors

        # get variables
        first_color, second_color, third_color, multiplier_color, tolerance_color = colors

        # get values from its index's constants
        all_colors = f'{COLORS.index(first_color)}{COLORS.index(second_color)}{COLORS.index(third_color)}'

    # get tolerance from dict
    tolerance = TOLERANCE.get(tolerance_color)

    # multiply based on constant index
    multiplier = 10 ** COLORS.index(multiplier_color)

    # get the final result with all digits
    result = int(all_colors) * multiplier

    # calculate resistance
    resistance = ''
    if result >= 10 ** 9:
        result /= 10 ** 9
        resistance = 'giga'
    elif result >= 10 ** 6:
        result /= 10 ** 6
        resistance = 'mega'
    elif result >= 10 ** 3:
        result /= 10 ** 3
        resistance = 'kilo'

    return f'{int(result) if int(result) == result else result} {resistance}ohms ±{tolerance}%'
    
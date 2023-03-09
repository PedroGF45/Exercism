def label(colors):
    colors_inventory = ['black',
                        'brown',
                        'red',
                        'orange',
                        'yellow',
                        'green',
                        'blue',
                        'violet',
                        'grey',
                        'white']
    first_color, second_color, third_color, *rest = colors

    power_label = 10**colors_inventory.index(third_color)

    resistance = int(f'{colors_inventory.index(first_color)}{colors_inventory.index(second_color)}') * power_label

    prefix = ['kilo', 'mega', 'giga']

    print(power_label)
    print(resistance)

    if resistance == 0:
        return '0 ohms'
    if int(resistance * 10 ** (-9)) == resistance * 10 ** (-9):
        prefix = prefix[2]
        return f'{int(resistance * 10 ** (-9))} {prefix}ohms'
    elif int(resistance * 10 ** (-6)) == resistance * 10 ** (-6):
        prefix = prefix[1]
        return f'{int(resistance * 10 ** (-6))} {prefix}ohms'
    elif int(resistance * 10 ** (-3)) == resistance * 10 ** (-3):
        prefix = prefix[0]
        return f'{int(resistance * 10 ** (-3))} {prefix}ohms'
    else:
        return f'{resistance} ohms'
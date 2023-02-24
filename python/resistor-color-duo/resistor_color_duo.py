def value(colors):
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
    first_color, second_color, *rest = colors
    return int(f'{colors_inventory.index(first_color)}{colors_inventory.index(second_color)}')

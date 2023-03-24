def say(number):
    
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    
    numbers_english = ['zero',
                        'one',
                        'two', 
                        'three', 
                        'four', 
                        'five', 
                        'six', 
                        'seven', 
                        'eight', 
                        'nine', 
                        'ten', 
                        'eleven', 
                        'twelve',
                        'thirt',
                        'fourt',
                        'fift',
                        'sixt',
                        'sevent',
                        'eight',
                        'ninet',
                        'twenty',
                        'hundred',
                        'thousaund',
                        'milion',
                        'bilion']

    if len(str(number)) % 3 == 0:
        break_number = [str(number)[i:i+3] for i in range(0, len(str(number)), 3)]
    else:
        break_number = [str(number)[:(len(str(number)) % 3)]] + [str(number)[i:i+3] for i in range(len(str(number)) % 3, len(str(number)), 3)]
    print(break_number)

    if number < 13 or number == 20:
        return f'{numbers_english[number]}'
    elif number > 12 and number < 20:
        return f'{numbers_english[number]}' + 'een'
    elif number > 20 and str(number)[-1] == '0':
        index = int(f'1{str(number)[0]}')
        return f'{numbers_english[index]}' + 'y'
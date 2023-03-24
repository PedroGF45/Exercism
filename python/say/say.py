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
                        'twenty']
    
    grandezas = ['', ' thousand ', ' million ', ' billion ']

    if len(str(number)) % 3 == 0:
        break_number = [str(number)[i:i+3] for i in range(0, len(str(number)), 3)]
    else:
        break_number = [str(number)[:(len(str(number)) % 3)]] + [str(number)[i:i+3] for i in range(len(str(number)) % 3, len(str(number)), 3)]

    def check_dozens(number):
        if number < 13 or number == 20:
            return f'{numbers_english[number]}'
        elif number > 12 and number < 20:
            return f'{numbers_english[number]}' + 'een'
        elif number > 20 and str(number)[-1] == '0':
            index = int(f'1{str(number)[0]}')
            return f'{numbers_english[index]}' + 'y'
        else:
            index_dozens = int(f'1{str(number)[0]}')
            index_digit = int(f'{str(number)[1]}')
            if index_dozens == 12:
                return 'twenty-' + f'{numbers_english[index_digit]}'
            if index_dozens == 14:
                return 'forty-' + f'{numbers_english[index_digit]}'
            return f'{numbers_english[index_dozens]}' + 'y-' + f'{numbers_english[index_digit]}'
    
    def check_hundred(number):
        if len(str(number)) == 3:
            return f'{numbers_english[int(str(number)[0])]} hundred {check_dozens(int(str(number)[1:]))}' 
        else:
            return check_dozens(number) 

    ans = ''
    for i in range(1, len(break_number)  + 1, 1):
        print(i)
        ans += check_hundred(int(break_number[i - 1])) + grandezas[len(break_number) - i]

    return ans

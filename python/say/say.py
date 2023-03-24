def say(number):
    
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    
    numbers_english = ['one',
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
        if (len(ans) != 0 and number == 0) or number == 0:
            return ''
        if number < 13 or number == 20:
            return f'{numbers_english[number-1]}'
        elif number > 12 and number < 20:
            return f'{numbers_english[number-1]}' + 'een'
        elif number > 20 and str(number)[-1] == '0':
            index = int(f'1{str(number-1)[0]}')
            return f'{numbers_english[index]}' + 'y'
        else:
            index_dozens = int(f'1{str(number)[0]}')-1
            index_digit = int(f'{str(number)[1]}')-1
            if index_dozens == 11:
                return 'twenty-' + f'{numbers_english[index_digit]}'
            if index_dozens == 13:
                return 'forty-' + f'{numbers_english[index_digit]}'
            return f'{numbers_english[index_dozens]}' + 'y-' + f'{numbers_english[index_digit]}'
    
    def check_hundred(number):
        if len(str(number)) == 3:
            return f'{numbers_english[int(str(number)[0])-1]} hundred {check_dozens(int(str(number)[1:]))}' 
        else:
            return check_dozens(number) 

    def check_grandeza(i):
        if i < len(break_number) and int(break_number[i]) == 0 and i != 1:
            return ''
        return grandezas[len(break_number) - i]
    
    if len(break_number) == 1 and int(break_number[0]) == 0:
        return 'zero'
    
    ans = ''
    for i in range(1, len(break_number) + 1, 1):
        ans += f'{check_hundred(int(break_number[i - 1]))}{check_grandeza(i)}'

    return ans.strip()

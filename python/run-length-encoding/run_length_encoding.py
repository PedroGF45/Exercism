from itertools import groupby

def decode(string):
    num = ''
    ans = ''
    for char in string:
        if char.isdigit():
            num += char
        elif len(num) == 0:
            ans += char
        else:
            ans += f'{int(num) * char}'
            num = ''
    return ans

def encode(string):
    str_split = ["".join(g) for k, g in groupby(string)] 
    return ''.join(f'{len(part)}{part[0]}' if len(part) > 1 else part[0] for part in str_split)
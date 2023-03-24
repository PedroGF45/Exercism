from itertools import groupby

def decode(string):
    return ''.join((int(string[i])-1) * string[i + 1] if string[i].isdigit() else string[i] for i in range(0, len(string), 1))

def encode(string):
    str_split = ["".join(g) for k, g in groupby(string)] 
    return ''.join(f'{len(part)}{part[0]}' if len(part) > 1 else part[0] for part in str_split)
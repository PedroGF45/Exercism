def decode(string):
    return ''.join((int(string[i])-1) * string[i + 1] if string[i].isdigit() else string[i] for i in range(0, len(string), 1))

def encode(string):
    
    for char in string:
        ans = ''
        if char == ans[-1]:
            count = 1
            ans += char
        else:
            ans += char

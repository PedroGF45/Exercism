import string

def cipher_text(plain_text):
    
    # normalize string
    plain_text = plain_text.translate(str.maketrans('', '', string.punctuation)).replace(' ', '').lower()

    c = 0
    r = 0
    l = len(plain_text)

    # get minimum equal values to build a square
    while (c * r < l):
        c += 1
        r += 1

    # try to decrease row values by one
    if (c * (r - 1) > l):
        r -= 1

    res = ''

    j = 0
    for i in range(c):

        k = j
        while (k < (c * r)):
            if k >= l:
                res += ' '
            else: 
                res += plain_text[k]
            k += c
            print(res)
        j += 1
        
        if i < (c - 1):
            res += ' '

        print(res)
    return res
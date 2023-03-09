import string

LETTERS = ['abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']

def encode(plain_text):
    plain_text = plain_text.translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
    ans = ''
    for letter in plain_text:
        if letter.isdigit():
            ans += letter
        elif len(ans) == 5 or (len(ans) in range(5, len(plain_text) + 1, 6)) :
            ans += ' ' + LETTERS[1][LETTERS[0].index(letter.lower())]
        else:
            ans += LETTERS[1][LETTERS[0].index(letter.lower())]
    return ans

def decode(ciphered_text):
    ciphered_text = ciphered_text.translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
    ans = ''
    for letter in ciphered_text:
        if letter.isdigit():
            ans += letter
        else:
            ans += LETTERS[0][LETTERS[1].index(letter.lower())] 
    return ans

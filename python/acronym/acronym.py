import string

def abbreviate(words):
    new_words = words.replace('-',' ').translate(str.maketrans('', '', string.punctuation)).split()
    return ''.join(map(lambda x: x[0].upper(), new_words))
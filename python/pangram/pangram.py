import string

alphabet = list(string.ascii_lowercase)

def is_pangram(sentence):
    return bool(all(map(lambda x: x in sentence.lower(), alphabet)))

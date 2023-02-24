def is_isogram(string):
    new_string = string.replace('-', '').replace(' ', '').lower()
    return bool(len(set(new_string)) == len(new_string)) # set gives unique inputs

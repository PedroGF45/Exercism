def is_isogram(string):
    new_string = string.replace('-', '').replace(' ', '').lower()
    return len(set(new_string)) == len(new_string) # set gives unique inputs

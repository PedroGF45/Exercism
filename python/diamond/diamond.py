import string

alphabet = list(string.ascii_uppercase)

def rows(letter):

    if letter == 'A':
        return ['A']
    
    # check index of the letter in the alphabet
    index = alphabet.index(letter)

    # create first and last line
    first_last_line = [' ' * index + f'{alphabet[0]}' + ' ' * index] 

    # create mid_lines
    mid_lines = list(map(lambda x: ' ' * (index - x) + f'{alphabet[x]}' + ' ' * (2 * (index + 1) - 1 - 2 * (index + 1 - x)) + f'{alphabet[x]}' + ' ' * (index - x), range(1, index + 1, 1)))
    
    # create a copy of the mid lines and reverse it
    mid_lines_reverse = mid_lines.copy()
    mid_lines_reverse.reverse()

    return first_last_line + mid_lines + mid_lines_reverse[1:] + first_last_line

def transpose(lines):
    
    lines_new = lines.split('\n')

    # check for the biggest element 
    max_len = max(map(lambda x: len(x), lines_new)) + 1

    # create a temp list to fill when transposing
    res = list(map(lambda x: '', range(max_len)))

    # do the transposing
    for row in lines_new:
        i = 0
        for column in row:
            if len(res[i]) < lines_new.index(row):
                res[i] += (' ' * (lines_new.index(row) - len(res[i]))) + column
                i += 1
            else:
                res[i] += column
                i += 1

    return '\n'.join(res).strip()

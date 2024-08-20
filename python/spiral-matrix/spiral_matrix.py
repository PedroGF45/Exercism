def spiral_matrix(size):
    
    ans_coord = {}
    last_digit = 0
    
    if size >= 2:
        if size % 2 == 0:
            key = size // 2
        else:
            key = (size + 1) // 2
    else:
        key = 1

    for j in range(key):

        # first row
        for i in range(1 + j, size + 1 - j, 1):
            print(f'({j}, {i-1}) : {last_digit + i - j}')
            ans_coord[last_digit + i - j] = (j, i - 1)
        
        last_digit += size - 2 * j

        # last column
        for i in range(1 + j, size - j, 1):
            ans_coord[last_digit + i - j] = (i, size - 1 - j)

        last_digit += size - (2*j + 1)

        # last row
        for i in range(size - 1 - j, j, -1):
            ans_coord[last_digit + (size - i) - j] = (size - 1 - j, i - 1)

        last_digit += size - (2*j + 1)

        if last_digit == size ** 2 or last_digit < 0:
            continue

        # first column
        for i in range(size - 1 - j, 1 + j, -1):
            ans_coord[last_digit + (size - i) - j] = (i - 1, j)

        last_digit += size - (2*j + 2)

    ans = [[None for _ in range(size)] for _ in range(size)] # prepare list

    for coord in ans_coord:
        x = ans_coord[coord][0]
        y = ans_coord[coord][1]
        ans[x][y] = coord

    return ans

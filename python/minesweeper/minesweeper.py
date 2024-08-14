COORDS = [(1, 0), # right 
          (1, -1), # diagonal right down
          (0, -1), # down
          (-1, -1), # diagonal left down
          (-1, 0), # left
          (-1, 1), # diagonal left up
          (0, 1), # up
          (1, 1)] # diagonal right up

def annotate(minefield) -> list:

    wrong_lenght = any(map(lambda x: len(minefield[0]) != len(minefield[x]), range(0, len(minefield), 1)))
    wrong_char = any((minefield[i][j] != ' ' and minefield[i][j] != '*') for i in range(len(minefield)) for j in range(len(minefield[0])))

    if wrong_lenght or wrong_char:
        raise ValueError("The board is invalid with current input.")
    
    values = [(x, y, minefield[x][y])
              for x in range(len(minefield))
              for y in range(len(minefield[0]))]

    for value in values:
        nr_bombs = 0
        if value[2] == ' ': # is an empty space in the board
            for coord in COORDS:
                check_mine = tuple(sum(x) for x in zip(value[:2], coord)) # check ajacent coord
                
                # check if check_mine is under board scope
                if check_mine[0] >= len(minefield) or check_mine[1] >= len(minefield[0]) or check_mine[0] < 0 or check_mine[1] < 0:
                    continue

                if minefield[check_mine[0]][check_mine[1]] == '*': # if it's a bomb
                    nr_bombs += 1 # increase nr of bombs adjacent

            # change on the board
            # strings are immutable so we need to convert to a list
            if (nr_bombs != 0):
                row = list(minefield[value[0]])
                row[value[1]] = str(nr_bombs)
                minefield[value[0]] = "".join(row)

    return minefield

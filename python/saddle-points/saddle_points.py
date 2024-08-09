def saddle_points(matrix):
    
    # if lists dont have the same size they're irregular
    if not all(map(lambda x: len(matrix[x]) == len(matrix[x+1]), range(0, len(matrix) - 1, 1))):
        raise ValueError("irregular matrix")
    
    # list for result
    ans = []
    
    # iterate over rows
    for i in range(len(matrix)):
        # iterate over columns
        for j in range(len(matrix[0])):
            # max value of a row and min value of the column
            if max(matrix[i]) == matrix[i][j] and all(map(lambda x: matrix[i][j] <= matrix[x][j], range(0, len(matrix), 1))):
                ans.append({"row": i+1, "column": j+1})

    return ans

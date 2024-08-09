NUMBERS  = [" _ | ||_|   ",
            "     |  |   ",
            " _  _||_    ",
            " _  _| _|   ",
            "   |_|  |   ",
            " _ |_  _|   ",
            " _ |_ |_|   ",
            " _   |  |   ",
            " _ |_||_|   ",
            " _ |_| _|   "]

def convert(input_grid):
    
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    if any(map(lambda x: len(input_grid[x]) % 3 != 0 , range(0, len(input_grid) - 1, 1))):
        raise ValueError("Number of input columns is not a multiple of three")

    ans = ''
    for k in range(0, len(input_grid), 4):
        for i in range(0, len(input_grid[0]), 3): # loop through columns
            number = ''
            for j in range(k, k+4, 1): # loop through rows
                number += input_grid[j][i:i+3]

            if (number in NUMBERS):
                ans += str(NUMBERS.index(number))
            else:
                ans += '?'
        
        if ((k % 4 == 0 and k != 0) or (len(input_grid) > 4 and k == 0)) and (k != len(input_grid) - 4):
            print(k)
            ans += ','

    return ans

    




        

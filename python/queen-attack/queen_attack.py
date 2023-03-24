class Queen:
    def __init__(self, row, column):
        
        # errors
        if row < 0:
            # if the row parameter is negative
            raise ValueError("row not positive")
        
        elif row > 7:
            # if the row parameter is not on the defined board
            raise ValueError("row not on board")
        
        elif column < 0:
            # if the column parameter is negative
            raise ValueError("column not positive")
        
        elif column > 7:
            # if the column parameter is not on the defined board
            raise ValueError("column not on board")
        
        self.position = (row, column)

    def can_attack(self, another_queen):
         
        if self.position == another_queen.position:
            # if both the queens are on the same location
            raise ValueError("Invalid queen position: both queens in the same square")
        
        # same row or same column or same diagonal
        return self.position[0] == another_queen.position[0] \
            or self.position[1] == another_queen.position[1] \
            or abs(self.position[0] - another_queen.position[0]) == abs(self.position[1] - another_queen.position[1])

# Globals for the directions
# Change the values as you see fit

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
     
    def move(self, commands):
        for command in commands:
            if command == 'R':
                self.move_right()
            elif command == 'L':
                self.move_left() 
            elif command == 'A':
                self.move_advance()
            else:
                raise ValueError("Wrong Command")

    def move_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        else:
            self.direction = NORTH

    def move_left(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST
        else:
            self.direction = NORTH
    
    def move_advance(self):
        if self.direction == NORTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        elif self.direction == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
        elif self.direction == EAST:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
        else:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])

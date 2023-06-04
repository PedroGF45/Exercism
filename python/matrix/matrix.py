class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split('\n')
        self.matrix = list(map(lambda x: x.split(), self.matrix))

    def row(self, index):
        row = list(self.matrix[index - 1])

        row = list(map(lambda x: int(x), row))

        return row

    def column(self, index):
        column = []
        for row in self.matrix:
            column += [row[index-1]]

        column = list(map(lambda x: int(x), column))

        return column
    
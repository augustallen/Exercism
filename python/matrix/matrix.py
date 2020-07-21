class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in row.split()] for row in matrix_string.splitlines()] # create a list of lists which corresponds to each row in the matrix
        
    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [i[index-1] for i in self.matrix]
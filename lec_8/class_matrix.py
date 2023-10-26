import random

class Matrix:
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.matrix = [[random.randint(1,50) for col in range(self.cols)] for row in range(self.rows)]
        
    def print_matrix(self):
        for row in self.matrix:
            print(row) 

    def mean_of_matrix(self):
        sum = 0
        count = len(self.matrix)*len(self.matrix[0])
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                sum += self.matrix[i][j]
        mean=sum/count
        return f"Mean of matrix is {round(mean,2)}"
    
    def sum_of_row(self,row=0):
        if row>=0 and row<len(self.matrix):
            return f"Sum of the row {row} is {sum(self.matrix[row])}"
        return f"Invalid row index"

    def avg_of_column(self,col=0):
        sum=0
        if col>=0 and col<len(self.matrix[0]):
            for row in self.matrix:
                sum+=row[col]
                avg=sum/(len(self.matrix))
            return f"Average of column {col} is {round(avg,2)}"
        return f"Invalid column index"

    def print_submatrix(self, col1,col2,row1,row2):
        submatrix=[]
        for r in range(row1,row2+1):
            sub_row=[]
            for c in range(col1,col2+1):
                sub_row.append(self.matrix[r][c])
            submatrix.append(sub_row)
        print("Submatrix is")
        for row in submatrix:
            print(row)

matrix=Matrix(3,3)
matrix.print_matrix()
print(matrix.mean_of_matrix())
print(matrix.sum_of_row(2))
print(matrix.avg_of_column(2))
matrix.print_submatrix(1,2,1,2)
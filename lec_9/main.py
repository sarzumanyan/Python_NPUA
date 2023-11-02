import random
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[random.randint(1,50) for _ in range(self.cols)] for _ in range(self.rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += str(row) + "\n"
        return matrix_str

    def __add__(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Rows and cols of matrices should be the same")
        new_matrix=[]
        for i in range(self.rows):
            new_matrix_row=[]
            for j in range(self.cols):
                new_matrix_row.append(self.matrix[i][j] + other.matrix[i][j])
            new_matrix.append(new_matrix_row)
        new_matrix_obj = Matrix(self.rows, self.cols)
        new_matrix_obj.matrix = new_matrix
        return new_matrix_obj
    
    def __sub__(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Rows and cols of matrices should be the same")
        new_matrix=[]
        for i in range(self.rows):
            new_matrix_row=[]
            for j in range(self.cols):
                new_matrix_row.append(self.matrix[i][j] - other.matrix[i][j])
            new_matrix.append(new_matrix_row)
        result_matrix = Matrix(self.rows, self.cols)
        result_matrix.matrix = new_matrix
        return result_matrix
    
    def __mul__(self,other):
        if self.cols != other.rows:
            raise ValueError("Columns of first matrix should be equal to rows of second matrix")
        new_matrix = []
        for i in range(self.rows):
            new_matrix_row = []
            for j in range(self.cols):
                sum=0
                for k in range(other.cols):
                    sum+=self.matrix[i][k]*other.matrix[k][j]
                new_matrix_row.append(sum)
            new_matrix.append(new_matrix_row)
        new_matrix_obj = Matrix(self.rows, self.cols)
        new_matrix_obj.matrix = new_matrix
        return new_matrix_obj
    
if __name__=="__main__":
    matrix_1=Matrix(3,3)
    matrix_2=Matrix(3,3)
    print(matrix_1)
    print(matrix_2)
    result_add=matrix_1+matrix_2
    print("The result of adding matrix_1 and matrix_2")
    print(result_add)
    result_sub=matrix_1-matrix_2
    print("The result of substracting matrix_1 and matrix_2")
    print(result_sub)
    result_mult=matrix_1*matrix_2
    print("The result of multiplying matrix_1 and matrix_2")
    print(result_mult)
import random

def generate_random_matrix(rows,cols):
    """ random_matrix=[]
    for _ in range(rows):
        row=[]
        for _ in range(cols):
            row.append(random.randrange(1, 100))
        random_matrix.append(row)
    return random_matrix """
    return [[random.randint(1,100) for _ in range(cols)] for _ in range(rows)]
        
def get_column_sum(matrix_2d, col_index):
    sum=0
    if 0 <= col_index < len(matrix_2d[0]):
        for i in range(len(matrix_2d)):
            print(matrix_2d[i][col_index])
            sum+=matrix_2d[i][col_index]
    else:
        print("Invalid column index.")
    return sum

def get_row_average(matrix_2d,row_index):
    avg = 0
    if 0 <= row_index < len(matrix_2d):
        for j in range(len(matrix_2d[0])):
            print(matrix_2d[row_index][j])
            avg+=matrix_2d[row_index][j]/2
    else:
        print("Invalid row index.")
    return avg

matrix_2d=generate_random_matrix(5,4)
print(matrix_2d)
col_index=int(input("Enter the index of column: "))
print(get_column_sum(matrix_2d, col_index))
row_index=int(input("Enter the index of row: "))
print(get_row_average(matrix_2d, row_index))
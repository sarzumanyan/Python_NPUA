import random

def generate_random_matrix(rows, cols):
    """ random_matrix=[]
    for _ in range(rows):
        row=[]
        for _ in range(cols):
            row.append(random.randrange(1, 100))
        random_matrix.append(row)
    return random_matrix """
    matrix = [[random.randint(1,100) for _ in range(cols)] for _ in range(rows)]
    for row in matrix:
        print(row)
    return matrix

def get_column_sum(matrix_2d, col_index):
    sum = 0
    if 0 <= col_index < len(matrix_2d[0]):
        for row in matrix_2d:
            sum += row[col_index]
        return f"Sum of column {col_index} is {sum}"
    else:
        print("Invalid column index.")


def get_row_average(matrix_2d, row_index):
    avg = 0
    if 0 <= row_index < len(matrix_2d):
        row = matrix_2d[row_index]
        avg = sum(row) / 2
        return f"Average of row {row_index} is {avg}"
    else:
        print("Invalid row index.")
    

matrix_2d = generate_random_matrix(5, 4)
col_index = int(input("Enter the index of column: "))
print(get_column_sum(matrix_2d, col_index))
row_index = int(input("Enter the index of row: "))
print(get_row_average(matrix_2d, row_index))
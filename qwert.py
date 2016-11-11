matrix1 = [[2 for column in range(3)] for row1 in range(2)]
matrix2 = [[2 for column2 in range(2)] for row2 in range(3)]
matrix3 = [[0 for column3 in range(2)] for row3 in range(2)]

for row1 in range(2):
    for column2 in range(2):
        matrix3[row1][column2] = 0
        for row2 in range(0, 3, 1):
            matrix3[row1][column2] = matrix3[row1][column2] + (matrix1[row1][row2] * matrix2[row2][column2])
print(matrix3)

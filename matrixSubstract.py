matrix = [[0 for column in range(5)] for row in range(5)]
matrix2= [[0 for column in range(5)] for row in range(5)]
matrix3=[[0 for column in range(5)] for row in range(5)]
element = 0
for row in range(5):
    for column in range(5):
        element = element + 1
        matrix[row][column]=element+10
        matrix2[row][column] = element
print(matrix)
print((matrix2))

for row in range(5):
    for column in range(5):
        matrix3[row][column]= matrix[row][column]-matrix2[row][column]
print(matrix3)

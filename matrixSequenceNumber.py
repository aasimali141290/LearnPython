matrix = [[0 for column in range(5)] for row in range(5)]
element = 0
for row in range(5):
    for column in range(5):
        element = element + 1
        matrix[row][column]=element
print(matrix)

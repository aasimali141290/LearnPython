array = [1, 2, 3, 4, 5, 6, 7]
array2 = [11, 22, 33, 44, 55, 66, 77]
f = 0
e = len(array)
g = len(array)
temp = 0
f = e
for i in range(0, e, 1):
    g = g - 1
    temp = array[i]
    array[i] = array2[g]
    array2[g] = temp

print(array)
print(array2)

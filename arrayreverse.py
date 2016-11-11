array = [1, 2, 3, 4, 5, 6, 7]
d = []
c = 0
f = 0
e = len(array)
f = e
for i in range(0, e, 1):
    f = f - 1
    temp = array[f]
    array[f] = array[i]
    array[i] = temp
    if i == f:
        break

print(array)

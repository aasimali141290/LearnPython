numItem = input('number of item in the list ')
l = int(numItem)
nameList = []
i = 0
while l > i:
    nameList.append(input())
    i += 1

for j in range(0, l, 1):
    if (j == 0):
        print("'", end='')
    if (j < l-1):
        print('' + nameList[j], end=', ')
    if (j==l-1):
        print(''+nameList[j],end="'")
    if (j == l - 2):
        print("and", end=' ')

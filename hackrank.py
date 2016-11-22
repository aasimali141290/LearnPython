set = set([])
a = 1
print('enter the name of fruit')
namefruit = input()
set.add(namefruit)
while a < 5:
    print('enter the name of fruit')
    namefruit = input()
    d = namefruit in set
    if d:
        continue
    else:
        set.add(namefruit)
        a += 1
print(set)

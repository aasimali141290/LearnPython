number = 5
a = 1
c = 1
i = 1
while i < number + 1:
    print("\n")
    a = 1
    c = 1
    while a < number+1 - i:
        print(' ', end=' ')
        a = a + 1

    while  c<i + 1:
        print(c, end=' ')
        c = c + 1
    i = i + 1

number = 5
a = 1
c = 1
i = 1
d = number - 1
while i < number + 1:
    print("\n")
    c = 1
    a = 1
    d = number -i
    while a < i:
        print(' ', end='')
        a = a + 1
    while c < number - i + 2:
        print(c, end='')
        c = c + 1

    while d > 0:
        print(d, end='')
        d = d - 1
    i = i + 1

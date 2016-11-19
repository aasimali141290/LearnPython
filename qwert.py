def readLineCharFile():
    a = 0
    file = open('C:\\Users\\aasim ali\\Downloads\\a1.txt', 'r')
    for line in file:
        for char in line:
            a += 1
    print(a)

readLineCharFile()

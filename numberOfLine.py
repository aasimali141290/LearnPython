def lineReadFile():
    a=0
    file = open('C:\\Users\\aasim ali\\Downloads\\a1.txt', 'r')
    for line in file:
        if line[:-1]:
            a+=1
    print(a)
lineReadFile()

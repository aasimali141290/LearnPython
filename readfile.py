def readFile():
    file = open('C:\\Users\\aasim ali\\Downloads\\a1.txt', 'r')
    while True:
        line = file.readline()
        if not line:
            print(line)
            break
        else:
            print(line)

def lineReadFile2():
    a = 0
    file = open('C:\\Users\\aasim ali\\Downloads\\a1.txt', 'r')
    for line in file:
        print(line)
readFile()
lineReadFile2()